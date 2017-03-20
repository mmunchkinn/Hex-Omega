from django.core.mail import send_mail
from HexOmega import settings
from haikunator import haikunator
import _thread


def get_default_password():
    h = haikunator.Haikunator()
    return h.haikunate()


def send_default_password(user, password, **kwargs):
    _thread.start_new_thread(send_default_password_threads, (user, password))


def send_default_password_threads(user, password, **kwargs):
    subject = 'Password - Hex Omega Systems'
    body = 'Password for {}({}) is {}\n\n'.format(user.get_full_name(), user.username, password)
    print(password)
    body += 'Please login and change your password, under Profile->Edit Profile.\n'
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False
    )
