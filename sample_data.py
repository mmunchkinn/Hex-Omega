from users.models import *
from datetime import datetime, timedelta

from users.utils import start_schedule_thread, tasks_email_schedule

import os
from HexOmega.settings import BASE_DIR


def setup():
    # Create role.
    r = Role()
    r.title = 'Security Coordinator'
    r.save()

    # Create admin
    adm = AdminUser(username='admin_man', first_name='admin', last_name='man')
    adm.set_password('qwerty123')
    adm.save()

    # Create leader
    l = LeaderUser(username='leader_man', first_name='leader', last_name='man')
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
    m = MemberUser(username='theseus', first_name='theseus', last_name='demigod')
    m.set_password('qwerty123')
    m.role_id = r.id
    m.project_id = p.id
    m.save()

    n = MemberUser(username='abhishek', first_name='Abhishek', last_name='Venkatesh')
    n.set_password('qwerty123')
    n.email = 'avsv96@gmail.com'
    n.role_id = r.id
    n.project_id = p.id
    n.save()

    o = MemberUser(username='caroline', first_name='caroline', last_name='i_don\'t_know')
    o.set_password('qwerty123')
    o.email = 'carolinemary224@gmail.com'
    o.role_id = r.id
    o.project_id = p.id
    o.save()

    t = Task(status='Assigned', est_start=datetime.now() - timedelta(days=1),
             est_end=datetime.now() + timedelta(days=1), action_list=p.actionlist)
    t.actual_start = t.est_start
    t.actual_end = t.est_end
    t.title = 'Programming'
    t.save()
    t.memberuser_set.add(m)
    t.memberuser_set.add(n)
    t.memberuser_set.add(o)
    t.save()

    start_schedule_thread()
    # tasks_email_schedule()


if __name__ == '__main__':
    setup()
