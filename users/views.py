from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse
from .models import Project, ActivityLog, ActionList, AdminUser, MemberUser
from .add_user_form import AddUserForm

"""
    These views are only for testing the models, and their access
"""


class CreateAdminView(CreateView):
    """
    Provides a form to indicate the new admin user's detail.
    If the information indicated is valid, the page will be redirected.
    The information of the newly created admin will be displayed.
    """
    model = AdminUser
    fields = ['username', 'first_name', 'last_name', 'email', 'password', 'bio']

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

    def get_success_url(self):
        return reverse('admin_detail', kwargs={'pk': self.object.pk})


class ProjectListView(generic.ListView):
    """
        work in progress - for admin to view the list of projects which have been modified
    """
    model = Project

    def get_queryset(self):
        return Project.objects.all().filter()


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
            user.save()
            return redirect('member_detail', pk=user.pk)
    else:
        form = AddUserForm()
    return render(request, 'users/add_member.html', {'form':form})


class DisplayMemberDetail(generic.DetailView):
    """
    Display the member information
    """
    model = MemberUser
    template_name = 'users/member_detail.html'