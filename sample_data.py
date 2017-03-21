from users.models import *
from datetime import datetime, timedelta

from users.utils import start_schedule_thread, tasks_email_schedule
import os


def setup():
    # Create role.
    r = Role()
    r.title = 'Security Coordinator'
    r.save()

    # Create admin
    adm = AdminUser(username='G2503472', first_name='admin', last_name='man')
    adm.email = 'admin_man@example.com'
    adm.set_password('qwerty123')
    adm.save()

    # Create leader
    l = LeaderUser(username='69497604', first_name='leader', last_name='man')
    l.email = 'leader_man@example.com'
    l.set_password('qwerty123')
    l.save()

    # Create project
    p = Project(name='PMT')
    p.start_date = datetime.now()
    p.end_date = datetime.now() + timedelta(days=30)
    p.leader_id = l.id
    p.save()
    p.admins.add(adm)
    p.save()

    # Create member
    m = MemberUser(username='56475644', first_name='Heracles', last_name='Alcmene')
    m.set_password('qwerty123')
    m.email = 'heracles@example.com'
    m.role_id = r.id
    m.project_id = p.id
    m.save()

    n = MemberUser(username='40475328', first_name='Perseus', last_name='Son of Danae')
    n.set_password('qwerty123')
    n.email = 'perseus@example.com'
    n.role_id = r.id
    n.project_id = p.id
    n.save()

    o = MemberUser(username='81343691', first_name='Apollo', last_name='Son of Leto')
    o.set_password('qwerty123')
    o.email = 'apollo@example.com'
    o.role_id = r.id
    o.project_id = p.id
    o.save()

    t = Task(status='Assigned', est_start=datetime.now() - timedelta(days=1),
             est_end=datetime.now() + timedelta(days=1), action_list=p.actionlist)
    t.actual_start = t.est_start
    t.actual_end = t.est_end
    t.title = 'Programming'
    t.save()
    t.users.add(m)
    t.users.add(n)
    t.users.add(o)
    t.users.add(l)
    t.save()

    start_schedule_thread()
    # tasks_email_schedule()


if __name__ == '__main__':
    setup()
