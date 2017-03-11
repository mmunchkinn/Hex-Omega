from django.shortcuts import render, HttpResponse

from users.models import Project

from .parse_to_html import parse_log
from yattag import Doc


# Create your views here.
def test(request):
    p = Project.objects.get(name__exact='PMT')

    doc, tag, text = Doc().tagtext()
    with tag('h3', id='main-title'):
        # enter project.name here
        text('PMT')

    p = parse_log(p)
    return render(request, 'log/test.html',
                  {'log_data': p.test(),
                   'project_title': doc.getvalue()
                   })
