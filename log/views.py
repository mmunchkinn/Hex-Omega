from django.shortcuts import render, HttpResponse

from users.models import Project

from .parse_to_html import parse_log
from yattag import Doc


# Create your views here.
def test(request, username, project):
    proj = Project.objects.get(name__exact=project)

    doc, tag, text = Doc().tagtext()
    with tag('h3', id='main-title'):
        text(project)

    p = parse_log(proj)
    return render(request, 'log/test.html',
                  {'log_data': p.test(),
                   'project_title': doc.getvalue(),
                   'title': proj.name,
                   'section': 'Log'
                   })
