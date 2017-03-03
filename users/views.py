from django.shortcuts import render
from django.http import HttpResponse

from .models import Project, ActivityLog, ActionList

"""
    These views are only for testing the models, and their access
"""


def search_form(request):
    return render(request, 'users/search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q'] is not '':
        message = 'You searched for: {}'.format(request.GET['q'])
        message += "<br>"
        try:
            projects = Project.objects.filter(name__contains=request.GET['q'])
            for p in projects:
                message += "Project Name: {}<br>".format(p.name)
                message += "<b>Admin(s):</b><br>"
                for a in p.admins.all():
                    message += "{}<br>".format(a)
                message += "<b>Leader:</b><br>"
                message += "{}<br>".format(p.leader)
                message += "<b>Member(s):</b><br>"
                for a in p.memberuser_set.all():
                    message += "{}<br>".format(a)
                message += "Log: {}<br>".format(p.activitylog.title)
                message += "Log ID: {}<br>".format(p.activitylog.id)
                message += "Log: {}<br>".format(p.actionlist.name)
                message += "Log ID: {}<br>".format(p.actionlist.id)
                message += "<hr><hr>"

        except Exception as e:
            message += '<b>No projects exist with this name.<br>'
            message += e.__str__()
            message += '</b>'
            message += "<hr>"
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
