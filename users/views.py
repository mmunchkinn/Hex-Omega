from django.shortcuts import render
from django.http import HttpResponse

from .models import Project, ActivityLog, ActionList

"""
    These views are only for testing the models, and their access
"""


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
