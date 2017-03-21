# @author: Abhi Rudra
# utilities for the backend services.

from django.core.mail import send_mail, send_mass_mail
from haikunator import haikunator
from twilio.rest import TwilioRestClient
from datetime import datetime, timedelta
import _thread

sys_email = 'hex.omega@yandex.com'


def get_default_password():
    h = haikunator.Haikunator()
    return h.haikunate()


def mail_kickoff(*args, var=1, **kwargs):
    if var is 1:
        _thread.start_new_thread(send_default_password_threads, (args[0], args[1]))
    else:
        _thread.start_new_thread(send_reminder_threads, (args[0],))


def send_default_password_threads(user, password, **kwargs):
    subject = 'Password - Hex Omega Systems'
    body = 'Password for {}({}) is {}\n\n'.format(user.get_full_name(), user.username, password)
    print(password)
    body += 'Please login and change your password, under Profile->Edit Profile.\n'
    send_mail(
        subject,
        body,
        sys_email,
        [user.email],
        fail_silently=False
    )


def start_schedule_thread():
    _thread.start_new_thread(tasks_email_schedule, ())


def tasks_email_schedule():
    from users.models import Project
    for project in Project.objects.all():
        lp = []
        for task in project.actionlist.task_set.all():
            if task.est_end.date() - timedelta(days=1) == datetime.now().date():
                if task.status is not 'Completed' and task.status is not 'Unassigned':
                    l = [member.email for member in task.users.all() if member.email is not '']
                    sub = task.action_list.project.name + ' : ' + task.title
                    msg = 'This is an automated reminder to submit your deliverable before tomorrow.\n\n'
                    msg += 'Please do not reply to this mail.'
                    t = (sub, msg, sys_email, l)
                    print(t, file=open('mass_mail_log.txt', 'w+'))
                    lp.append(t)

        if len(lp) is not 0:
            # mail_kickoff(lp, var=2)
            print(lp)


def send_reminder_threads(mails, **kwargs):
    send_mass_mail(
        tuple(mails),
        fail_silently=False
    )
