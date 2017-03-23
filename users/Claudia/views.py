from users.views import *

from .user_form import AdminUserForm, AdminUpdateForm, MemberUpdateForm, LeaderUpdateForm


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
            password = get_default_password()
            # bio = request.POST.get('bio')
            user = AdminUser.objects.create(username=username, first_name=first_name, last_name=last_name,
                                            email=email)
            user.set_password(password)
            mail_kickoff(user, password)
            user.save()
            update_session_auth_hash(request, request.user)
            return redirect('display_admin', request.user.username)
    return render(request, 'users/adminuser_form.html', {'form': form})


@login_required
def get_admin_detail(request, username):
    """
    Display the information of an admin user
    :param request:
    :return:
    """
    user = AdminUser.objects.get(username__iexact=username)
    return render(request, 'users/user_information.html', {'adminuser': user})


# abhi's test decorator : removed from repo
# @viewing_context
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
            return redirect('list_of_admins', username)

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
        return redirect('list_of_admins', username)
    if LeaderUser.objects.filter(username__exact=d):
        l = LeaderUser.objects.get(username__exact=d)
        l.delete()
        print('leader deleted!')
        return redirect('list_of_leaders', username)
    if MemberUser.objects.filter(username__exact=d):
        m = MemberUser.objects.get(username__exact=d)
        m.delete()
        print('member deleted!')
        return redirect('list_of_members', username)


@login_required
def get_list_of_admins(request, username):
    """
    Display a list of admins
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


@login_required
def get_list_of_leaders(request, username):
    """
    Display a list leaders
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


@login_required
def update_leader(request, username, l):
    """
    Update a leader's information from the list of all leaders
    :param request:
    :param username:
    :param l:
    :return:
    """
    lead = LeaderUser.objects.get(username__iexact=l)
    form_data = {'first_name': lead.first_name, 'last_name': lead.last_name,
                 'email': lead.email, 'password': " ", 'bio': lead.bio}
    form = LeaderUpdateForm(request.POST, initial=form_data)
    if request.method == 'POST':
        if form.is_valid():
            lead.first_name = request.POST.get('first_name')
            lead.last_name = request.POST.get('last_name')
            lead.email = request.POST.get('email')
            p = request.POST['password']
            if (p is not '' or p is not None) and len(p.strip()) >= 8:
                lead.set_password(p)
            lead.bio = request.POST.get('bio')
            lead.save()
            update_session_auth_hash(request, request.user)
            return redirect('list_of_leaders', username)

    return render(request, 'users/update_leader_form.html', {'leaderuser': lead, 'form': form, 'errors': form.errors})


@login_required
def get_list_of_members(request, username):
    """
    Display a list members
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
def update_member(request, username, m):
    """
    Update a member's information from the list of all members
    :param request:
    :param username:
    :param m:
    :return:
    """
    mem = MemberUser.objects.get(username__iexact=m)
    form_data = {'first_name': mem.first_name, 'last_name': mem.last_name,
                 'email': mem.email, 'password': " ", 'bio': mem.bio}
    form = MemberUpdateForm(request.POST, initial=form_data)
    if request.method == 'POST':
        if form.is_valid():
            mem.first_name = request.POST.get('first_name')
            mem.last_name = request.POST.get('last_name')
            mem.email = request.POST.get('email')
            p = request.POST['password']
            if (p is not '' or p is not None) and len(p.strip()) >= 8:
                mem.set_password(p)
            mem.bio = request.POST.get('bio')
            mem.save()
            update_session_auth_hash(request, request.user)
            return redirect('list_of_members', username)

    return render(request, 'users/update_member_form.html', {'memberuser': mem, 'form': form, 'errors': form.errors})


@login_required
def display_all_projects(request, username):
    """
    Display all projects
    :param request:
    :param username:
    :return:
    """
    project_list = Project.objects.all().order_by('pk')
    proj_paginator = Paginator(project_list, 5)
    proj_page = request.GET.get('page')

    try:
        all_project_list = proj_paginator.page(proj_page)
    except PageNotAnInteger:
        all_project_list = proj_paginator.page(1)
    except EmptyPage:
        all_project_list = proj_paginator.page(proj_paginator.num_pages)

    return render(request, 'users/all_project_list.html', {'all_project_list': all_project_list, 'page': proj_page})


@login_required
def display_open_projects(request, username):
    """
    Display a list of open projects
    :param request:
    :param username:
    :return:
    """
    open_proj_list = Project.objects.filter(status='0').order_by('pk')
    open_proj_paginator = Paginator(open_proj_list, 5)
    open_proj_page = request.GET.get('page')

    try:
        open_project_list = open_proj_paginator.page(open_proj_page)
    except PageNotAnInteger:
        open_project_list = open_proj_paginator.page(1)
    except EmptyPage:
        open_project_list = open_proj_paginator.page(open_proj_paginator.num_pages)
    return render(request, 'users/open_project_list.html', {'open_project_list': open_project_list, 'page': open_proj_page})


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
def users_search(request, username):
    """
    Search for all users
    :param request:
    :param username:
    :return:
    """
    errors = []
    # To search for admin users
    if 'adm' in request.GET:
        if 'first_name' in request.GET:
            adminuser = AdminUser.objects.filter(first_name__contains=request.GET['first_name'])
            if request.GET['first_name'] is '':
                errors.append('Please enter a search term.')
                return render(request, 'users/users_search.html', {'errors': errors})
            context = {'adminuser': adminuser, 'errors': errors, 'query': request.GET['first_name']}
            return render(request, 'users/users_search.html', context)

    # To search for leader users
    if 'lead' in request.GET:
        if 'first_name' in request.GET:
            leaderuser = LeaderUser.objects.filter(first_name__contains=request.GET['first_name'])
            if request.GET['first_name'] is '':
                errors.append('Please enter a search term.')
                return render(request, 'users/users_search.html', {'errors': errors})
            context = {'leaderuser': leaderuser, 'errors': errors, 'query': request.GET['first_name']}
            return render(request, 'users/users_search.html', context)

    # To search for member users
    if 'mem' in request.GET:
        if 'first_name' in request.GET:
            memberuser = MemberUser.objects.filter(first_name__contains=request.GET['first_name'])
            if request.GET['first_name'] is '':
                errors.append('Please enter a search term.')
                return render(request, 'users/users_search.html', {'errors': errors})
            context = {'memberuser': memberuser, 'errors': errors, 'query': request.GET['first_name']}
            return render(request, 'users/users_search.html', context)

    return render(request, 'users/users_search.html', {'errors': errors})