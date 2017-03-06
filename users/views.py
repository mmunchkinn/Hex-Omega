from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login

from django.contrib.auth.models import Group

from .models import Project, ActivityLog, ActionList, User, AdminUser, MemberUser, LeaderUser
from .backends import CustomUserAuth

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


def login_page(request, error):
    if error is '0':
        error = False
    else:
        error = True

    # if request.user.is_authenticated():
    #     return redirect('login_auth')

    return render(request,
                  'users/login.html',
                  {'error': error,
                   'request': request})


def login_auth(request):
    """
    Hmmm.... most of it is working. THe only qualm right now
    is if a logged in user returns to login page, and previously had
    a wrong login attempt, it continues to show the error message.
    :param request:
    :return:
    """
    # if request.user.is_authenticated():
    #     return render(request,
    #                   'users/login_auth.html',
    #                   {'li': True,
    #                    'user': request.user})

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = CustomUserAuth().authenticate(username=username, password=password)

        if user is False:
            # return render(request, 'users/login.html', {'error': True})
            return redirect('login_page', 1)

        # print(user.username, user.get_full_name(), user.password, user.has_usable_password(), user.__class__)
        if user is not None:
            print('User [{}] is logging in.'.format(user.username))
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request,
                          'users/login_auth.html',
                          {'li': True,
                           'user': user})
            # else:
            #     return render(request,
            #                   'users/login_auth.html',
            #                   {'li': False})

    else:
        return render(request, 'users/login.html', {'error': False})

