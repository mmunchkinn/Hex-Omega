from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .models import Project, ActivityLog, ActionList, User

"""
    These views are only for testing the models, and their access
"""


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
                  {'errors': errors,
                   'first': True})


def index(request):
    return render(request,
                  'users/index.html')


def login(request):
    return render(request,
                  'users/login.html')


def login_auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        print(user.username, user.get_full_name(), user.password, user.has_usable_password(), user.groups)

        if user is not None:
            print('User [{}] is logged in.'.format(user.username))
            login(request)
            return render(request,
                          'users/login_auth.html',
                          {'li': True,
                           'user': user})
        else:
            return render(request,
                          'users/login_auth.html',
                          {'li': False})

    else:
        return HttpResponse('Use POST.')
