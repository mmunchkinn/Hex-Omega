from users.models import *
from datetime import datetime, timedelta

import os
from HexOmega.settings import BASE_DIR


def setup():
    # Create role. - abhi
    r = Role()
    r.title = 'Security Coordinator'
    r.save()

    # Create admin - abhi
    adm = AdminUser(username='admin_man', first_name='admin', last_name='man')
    adm.set_password('qwerty123')
    adm.save()

    #Claudia's sample data
    adm1 = AdminUser(username='admin01', first_name='first', last_name='admin')
    adm1.set_password('qwerty123')
    adm1.save()

    # Claudia's sample data
    adm2 = AdminUser(username='admin02', first_name='second', last_name='admin')
    adm2.set_password('qwerty123')
    adm2.save()

    # Claudia's sample data
    adm3 = AdminUser(username='admin03', first_name='third', last_name='admin')
    adm3.set_password('qwerty123')
    adm3.save()

    # Claudia's sample data
    adm4 = AdminUser(username='admin04', first_name='fourth', last_name='admin')
    adm4.set_password('qwerty123')
    adm4.save()

    # Claudia's sample data
    adm5 = AdminUser(username='admin05', first_name='fifth', last_name='admin')
    adm5.set_password('qwerty123')
    adm5.save()

    # Create leader - abhi
    l = LeaderUser(username='leader_man', first_name='leader', last_name='man')
    l.set_password('qwerty123')
    l.save()

    # Claudia's sample data
    l2 = LeaderUser(username='leader_01', first_name='first', last_name='leader')
    l2.set_password('qwerty123')
    l2.save()

    # Create project - abhi
    p = Project(name='PMT')
    p.start_date = datetime.now()
    p.end_date = datetime.now() + timedelta(days=30)
    p.leader_id = l.id
    p.save()
    # !!!!!!
    p.admins.add(adm)
    p.save()

    # self.m.project.activitylog.content = self.p.activitylog.content - abhi
    print('#####' + str(p.activitylog.content))

    # Create member - abhi
    m = MemberUser(username='theseus', first_name='theseus', last_name='demigod')
    m.set_password('qwerty123')
    m.role_id = r.id
    m.project_id = p.id
    m.save()
    print('######' + str(m.project.activitylog.content))

    # Claudia's sample data
    m1 = MemberUser(username='theseus01', first_name='first', last_name='member')
    m1.set_password('qwerty123')
    m1.role_id = r.id
    m1.project_id = p.id
    m1.save()


if __name__ == '__main__':
    setup()
