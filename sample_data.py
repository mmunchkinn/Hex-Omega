from users.models import *
from datetime import datetime, timedelta

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
    # !!!!!!
    p.admins.add(adm)
    p.save()

    # self.m.project.activitylog.content = self.p.activitylog.content
    print('#####' + str(p.activitylog.content))

    # Create member
    m = MemberUser(username='theseus', first_name='theseus', last_name='demigod')
    m.set_password('qwerty123')
    m.role_id = r.id
    m.project_id = p.id
    m.save()
    print('######' + str(m.project.activitylog.content))


if __name__ == '__main__':
    setup()
