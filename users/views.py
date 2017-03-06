from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import AdminForm
from .models import Project, ActivityLog, ActionList, AdminUser

"""
    These views are only for testing the models, and their access
"""


class CreateAdminView(CreateView):
    """
    work in progress
    """
    model = AdminUser
    fields = ['first_name', 'last_name', 'email', 'bio']


class ProjectListView(generic.ListView):
    """
        work in progress - for admin to view the list of projects which have been modified
    """
    model = Project

    def get_queryset(self):
        return Project.objects.all().filter()


def add_admin_form(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            bio = form.cleaned_data['bio']
            adminuser = AdminUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, bio=bio)
            adminuser.save()
            return
    else:
        form = AdminForm()
    return render(request, 'users/adminuser_form.html', {'form': form})


def search_form(request):
    return render(request, 'users/search_form.html')


def search(request):
    errors = []
    if 'q' in request.GET:
        message = 'You searched for: {}'.format(request.GET['q'])
        message += "<br>"

        projects = Project.objects.filter(name__contains=request.GET['q'])
        # for p in projects:
        #     message += "Project Name: {}<br>".format(p.name)
        #     message += "<b>Admin(s):</b><br>"
        #     for a in p.admins.all():
        #         message += "{}<br>".format(a)
        #     message += "<b>Leader:</b><br>"
        #     message += "{}<br>".format(p.leader)
        #     message += "<b>Member(s):</b><br>"
        #     for a in p.memberuser_set.all():
        #         message += "{}<br>".format(a)
        #     message += "Log: {}<br>".format(p.activitylog.title)
        #     message += "Log ID: {}<br>".format(p.activitylog.id)
        #     message += "Log: {}<br>".format(p.actionlist.name)
        #     message += "Log ID: {}<br>".format(p.actionlist.id)
        #     message += "<hr><hr>"
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
                  {'errors': errors})
