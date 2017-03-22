from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .user_form import AdminUserForm, AdminUpdateForm, MemberUpdateForm
from .models import Project, AdminUser, MemberUser, LeaderUser
from .backends import CustomUserAuth
from .login_form import LoginForm
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

"""
    These views are only for testing the models, and their access
"""


def search(request):
    errors = []
    if 'q' in request.GET:
        message = 'You searched for: {}'.format(request.GET['q'])
        message += "<br>"

        projects = Project.objects.filter(name__contains=request.GET['q'])
        if request.GET['q'] is '':
            errors.append('Enter a search term.')
            return render(request,
                          'users/search_form.html',
                          {'errors': errors})

        return render(request,
                      'users/search_form.html',
                      {
                          'errors': errors,
                          'projects': projects,
                          'query': request.GET['q']
                      }
                      )

    return render(request,
                  'users/search_form.html',
                  {'errors': errors,
                   'first': True})


def index(request):
    return render(request,
                  'users/index.html')


def login_auth_2(request):
    """
    Login page authentication using django forms.
    If easier and simpler, implement this else the
    stuff I threw together up there.
    :param request:
    :return:
    """
    if request.user.is_authenticated():
        return redirect('user_logged_in', request.user.username)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            rem = request.POST.get('rem')
            user = CustomUserAuth().authenticate(username=username, password=password)

            if user is False:
                form.errors['password'] = 'The username or password is incorrect.'
                return render(request,
                              'users/login.html',
                              {
                                  'form': form,
                                  'errors': form.errors
                              })

            if user is not None:
                print('User [{}] is logging in.'.format(user.username))
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                if rem is not None:
                    request.session.set_expiry(7200)
                else:
                    request.session.get_expire_at_browser_close()
                return redirect('user_logged_in', username=username)

    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


@login_required
def logged_in(request, username):
    if AdminUser.objects.filter(username__exact=username).count() == 1:
        user = AdminUser.objects.get(username__exact=username)
        return redirect('display_admin', username)
    elif LeaderUser.objects.filter(username__exact=username).count() == 1:
        user = LeaderUser.objects.get(username__exact=username)
    else:
        user = MemberUser.objects.get(username__exact=username)

    # fix it properly later
    # this is to just test the new functions
    return render(request,
                  'users/admin_logged_in.html',
                  {'li': True,
                   'user': user})


@login_required
def jump_ship(request):
    print('jumping ship....')
    logout(request)
    return redirect('login_page')


# The following functions are done by Claudia


@login_required
def create_admin_user(request, username):
    """
    Create an admin user.
    username/add/$
    :param username:
    :param request:
    :return:
    """
    form = AdminUserForm()
    if request.method == 'POST':
        form = AdminUserForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            bio = request.POST.get('bio')
            user = AdminUser.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                 email=email, password=password, bio=bio)
            user.set_password(password)
            user.save()
            update_session_auth_hash(request, request.user)
            return redirect('display_admin', request.user.username)
    return render(request, 'users/adminuser_form.html', {'form': form, 'errors': form.errors})


@login_required
def get_admin_detail(request, username):
    """
    Display the information of an admin user
    :param request:
    :param username:
    :return:
    """
    user = AdminUser.objects.get(username__iexact=username)
    return render(request, 'users/user_information.html', {'adminuser': user})


@login_required
def update_admin_detail(request, username):
    """
    Update the information of an admin user from "edit profile"
    :param request:
    :param username:
    :return:
    """
    user = AdminUser.objects.get(username__iexact=username)
    form_data = {'first_name': user.first_name, 'last_name': user.last_name,
                 'email': user.email, 'password': " ", 'bio': user.bio}
    form = AdminUpdateForm(request.POST, initial=form_data)
    if request.method == 'POST':
        if form.is_valid():
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            p = request.POST['password']
            if (p is not '' or p is not None) and len(p.strip()) >= 8:
                user.set_password(p)
            user.bio = request.POST.get('bio')
            user.save()
            update_session_auth_hash(request, request.user)
            return redirect('display_admin', username)

    return render(request, 'users/update_admin_form.html', {'adminuser': user, 'form': form, 'errors': form.errors})


@login_required
def update_an_admin(request, username, a):
    """
    Update an admin's information from the list of all users
    :param request:
    :param username:
    :param a:
    :return:
    """
    adm = AdminUser.objects.get(username__iexact=a)
    form_data = {'first_name': adm.first_name, 'last_name': adm.last_name,
                 'email': adm.email, 'password': " ", 'bio': adm.bio}
    form = AdminUpdateForm(request.POST, initial=form_data)
    if request.method == 'POST':
        if form.is_valid():
            adm.first_name = request.POST.get('first_name')
            adm.last_name = request.POST.get('last_name')
            adm.email = request.POST.get('email')
            p = request.POST['password']
            if (p is not '' or p is not None) and len(p.strip()) >= 8:
                adm.set_password(p)
            adm.bio = request.POST.get('bio')
            adm.save()
            update_session_auth_hash(request, request.user)
            return redirect('list_of_users', username)

    return render(request, 'users/update_admin_form.html', {'adminuser': adm, 'form': form, 'errors': form.errors})


def delete_user(request, username, d):
    """
    To delete a particular user (admin/leader/member)
    :param request:
    :param username:
    :param d:
    :return:
    """
    if AdminUser.objects.filter(username__exact=d):
        a = AdminUser.objects.get(username__exact=d)
        a.delete()
        print('admin deleted!')
    if LeaderUser.objects.filter(username__exact=d):
        l = LeaderUser.objects.get(username__exact=d)
        l.delete()
        print('leader deleted!')
    if MemberUser.objects.filter(username__exact=d):
        m = MemberUser.objects.get(username__exact=d)
        m.delete()
        print('member deleted!')
    return redirect('list_of_users', username)


def get_list_of_admins(request, username):
    """
    Display a list of admins
    /list/
    :param request:
    :param username:
    :return:
    """
    user = AdminUser.objects.get(username__iexact=username)
    admin_user_list = AdminUser.objects.order_by('pk')

    adm_paginator = Paginator(admin_user_list, 5)
    adm_page = request.GET.get('page')
    try:
        admin_list = adm_paginator.page(adm_page)
    except PageNotAnInteger:
        admin_list = adm_paginator.page(1)
    except EmptyPage:
        admin_list = adm_paginator.page(adm_paginator.num_pages)

    context = {'adminuser': user, 'admin_list': admin_list, 'page': adm_page}
    return render(request, 'users/list_of_admins.html', context)


def get_list_of_leaders(request, username):
    """
    Display a list leaders
    /list/
    :param request:
    :param username:
    :return:
    """
    user = AdminUser.objects.get(username__iexact=username)
    leader_user_list = LeaderUser.objects.order_by('pk')

    lead_paginator = Paginator(leader_user_list, 5)
    lead_page = request.GET.get('page')
    try:
        leader_list = lead_paginator.page(lead_page)
    except PageNotAnInteger:
        leader_list = lead_paginator.page(1)
    except EmptyPage:
        leader_list = lead_paginator.page(lead_paginator.num_pages)

    context = {'adminuser': user, 'leader_list': leader_list, 'page': lead_page}
    return render(request, 'users/list_of_leaders.html', context)


def get_list_of_members(request, username):
    """
    Display a list members
    /list/
    :param request:
    :param username:
    :return:
    """
    user = AdminUser.objects.get(username__iexact=username)
    member_user_list = MemberUser.objects.order_by('pk')

    mem_paginator = Paginator(member_user_list, 5)
    mem_page = request.GET.get('page')
    try:
        member_list = mem_paginator.page(mem_page)
    except PageNotAnInteger:
        member_list = mem_paginator.page(1)
    except EmptyPage:
        member_list = mem_paginator.page(mem_paginator.num_pages)

    context = {'adminuser': user, 'member_list': member_list, 'page': mem_page}
    return render(request, 'users/list_of_members.html', context)


@login_required
def get_member_detail(request, username):
    """
    Display the information of a member user
    :param request:
    :param username:
    :return:
    """
    user = MemberUser.objects.get(username__iexact=username)
    return render(request, 'users/member_information.html', {'memberuser': user})


@login_required
def edit_member_information(request, username):
    """
    Update the information of a member user
    :param request:
    :param username:
    :return:
    """
    user = MemberUser.objects.get(username__iexact=username)
    form_data = {'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email, 'password': " ", 'bio': user.bio}
    form = MemberUpdateForm(request.POST, initial=form_data)
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            p = request.POST['password']
            if (p is not '' or p is not None) and len(p.strip()) >= 8:
                user.set_password(p)
            user.bio = request.POST.get('bio')
            user.save()
            update_session_auth_hash(request, request.user)
            return redirect('display_member', username)

    return render(request, 'users/update_member_form.html', {'memberuser': user, 'form': form, 'errors': form.errors})


@login_required
def display_all_projects(request, username):
    """
    Display all projects
    :param request:
    :param username:
    :return:
    """
    project_list = Project.objects.all().order_by('status')[:5]
    return render(request, 'users/all_project_list.html', {'project_list': project_list})


@login_required
def display_open_projects(request, username):
    """
    Display a list of open projects
    :param request:
    :param username:
    :return:
    """
    open_project_list = Project.objects.filter(status='0').order_by('start_date')[:5]
    return render(request, 'users/open_project_list.html', {'open_project_list': open_project_list})


@login_required
def project_information(request, username, p):
    """
    Display a particular project information
    :param request:
    :param username:
    :param p:
    :return:
    """
    project = Project.objects.get(name__exact=p)
    return render(request, 'users/project_information.html', {'project': project})


@login_required
def view_project_log(request, username, p):
    """
    Retrieve and view a particular project log - untested
    :param request:
    :param username:
    :param p:
    :return:
    """
    project = Project.objects.get(name__exact=p)
    if AdminUser.objects.filter(username__exact=username):
        return redirect('/logs/{project.name}')
    else:
        return PermissionDenied
    return render(request, 'users/project_information.html', {'project': project})