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

    # Claudia's sample data
    adm1 = AdminUser(username='G2503400', first_name='first', last_name='admin')
    adm1.email = 'test_admin01@example.com'
    adm1.set_password('qwerty123')
    adm1.save()

    # Claudia's sample data
    adm2 = AdminUser(username='G2503500', first_name='second', last_name='admin')
    adm2.email = 'test_admin02@example.com'
    adm2.set_password('qwerty123')
    adm2.save()

    # Claudia's sample data
    adm3 = AdminUser(username='G2503600', first_name='third', last_name='admin')
    adm3.email = 'test_admin03@example.com'
    adm3.set_password('qwerty123')
    adm3.save()

    # Create leader
    l = LeaderUser(username='69497604', first_name='leader', last_name='man')
    l.email = 'leader_man@example.com'
    l.set_password('qwerty123')
    l.save()

    # Claudia's sample data
    l2 = LeaderUser(username='69498000', first_name='first', last_name='leader')
    l2.email = 'test_leader@example.com'
    l2.set_password('qwerty123')
    l2.save()

    # Create project
    p = Project(name='PMT')
    p.start_date = datetime.now()
    p.end_date = datetime.now() + timedelta(days=30)
    p.leader_id = l.id
    p.save()
    p.admins.add(adm)
    p.save()

    # Claudia's sample data
    p2 = Project(name='PMT02')
    p2.start_date = datetime.now()
    p2.end_date = datetime.now() + timedelta(days=30)
    p2.leader_id = l2.id
    p2.save()
    p2.admins.add(adm1)
    p2.save()

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

    # Claudia's sample data
    m1 = MemberUser(username='34656000', first_name='first', last_name='member')
    m1.set_password('qwerty123')
    m1.email = 'test_member@example.com'
    m1.role_id = r.id
    m1.project_id = p.id
    m1.save()

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

    # start_schedule_thread()
    # tasks_email_schedule()


if __name__ == '__main__':
    setup()
