from log.Log import Log

from users.models import *


def create_roles():
    roles = [
        'Secretary',
        'Communications Manager',
        'Software Coordinator',
        'Security Coordinator',
        'Librarian',
        'Others'
    ]
    for r in roles:
        role = Role()
        role.title = r
        role.save()


def create_admin():
    adm = AdminUser()
    adm.username = 'S32147836'
    adm.set_password('admin@password')
    adm.email = 'admin@example.com'
    adm.save()


def create_leader():
    lead = LeaderUser()
    lead.username = '33344456'
    lead.set_password('leader_password')
    lead.save()


def create_actionlist():
    pass
