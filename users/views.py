from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group
from .add_user_form import AddUserForm
from .models import Project, AdminUser, MemberUser, LeaderUser
from .backends import CustomUserAuth
from .login_form import LoginForm


def get_current_path(request):
    return {
       'current_path': request.get_full_path()
     }


def url_context(view_func):
    def _view(request, *args, **kwargs):
        if request.user.is_admin():
            return HttpResponseRedirect({{get_current_path(request)}})

        elif request.user.is_leader():
            if {{get_current_path(request)}}.__contains__(AdminUser.username):
                    print('You are not allowed to view the admin contend!!')
            else:
                return HttpResponseRedirect({{get_current_path(request)}})

        elif request.user.is_member():
            if  {{get_current_path()}}.__contains__(AdminUser.username):
                print('You are not allowed to view the admin content!!')
            elif {{get_current_path()}}.__contains__(LeaderUser.username):
                print('You are not allowed to view the leader content!!')
            else:
                return HttpResponseRedirect({{get_current_path(request)}})
        else:
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

    return _view

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


class CreateAdminView(CreateView):
    """
    Provides a form to indicate the new admin user's detail.
    If the information indicated is valid, the page will be redirected.
    The information of the newly created admin will be displayed.
    """
    model = AdminUser
    fields = ['username', 'first_name', 'last_name', 'email', 'password', 'bio']

    #@url_context
    def get_success_url(self):
        return reverse('admin_detail', kwargs={'pk': self.object.pk})


class DisplayAdminView(generic.DetailView):
    """
    Display the information such as username, first name, last name, email and bio of the admin
    """
    model = AdminUser
    template_name = 'users/detail.html'


class UpdateAdmin(UpdateView):
    """
    Update the information of an admin.
    """
    model = AdminUser
    fields = ['first_name', 'last_name', 'email', 'bio']
    template_name = 'users/update_admin.html'

    #@url_context
    def get_success_url(self):
        return reverse('admin_detail', kwargs={'pk': self.object.pk})


class ProjectListView(generic.ListView):
    """
        work in progress - for admin to view the list of projects which have been modified
    """
    model = Project

    def get_queryset(self):
        return Project.objects.all().filter()


class CreateProjectView(generic.CreateView):

    model = Project
    fields = ['name', 'status', 'start_date', 'end_date', 'description', 'leader']

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class DisplayProjectView(generic.DetailView):

    model = Project
    template_name = 'users/projectDetail.html'


class CreateLeaderView(CreateView):

    model = LeaderUser
    fields = ['username', 'first_name', 'last_name', 'email', 'password', 'bio']

    #@url_context
    def get_success_url(self):
        return reverse('leader_detail', kwargs={'pk': self.object.pk})


class DisplayLeaderView(generic.DetailView):

    model = LeaderUser
    template_name = 'users/leaderDetail.html'


def add_member(request):
    """
    Leader will create and add member into the project
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            project_id = request.POST.get('project_id')
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            role_id = request.POST.get('role_id')
            bio = request.POST.get('bio')
            user = MemberUser.objects.create_user(project_id= project_id, username=username, first_name=first_name, last_name=last_name, email=email, password=password, role_id=role_id, bio=bio)
            user.set_password(password)
            user.save()
            return redirect('member_detail', pk=user.pk)
    else:
        form = AddUserForm()
    return render(request, 'users/add_member.html', {'form': form})


class DisplayMemberDetail(generic.DetailView):
    """
    Display the member information
    """
    model = MemberUser
    template_name = 'users/member_detail.html'