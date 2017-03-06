from django.test import TestCase

from datetime import datetime, timedelta
from parse import *

from users.models import *
from log.Log import log


# Create your tests here.
class LogTest(TestCase):
    def setUp(self):
        # Create role.
        self.r = Role()
        self.r.title = 'Security Coordinator'
        self.r.save()

        # Create admin
        self.adm = AdminUser(username='admin_man', first_name='admin', last_name='man')
        self.adm.set_password('qwerty123')
        self.adm.save()

        # Create leader
        self.l = LeaderUser(username='leader_man', first_name='leader', last_name='man')
        self.l.set_password('qwerty123')
        self.l.save()

        # Create project
        self.p = Project(name='PMT')
        self.p.start_date = datetime.now()
        self.p.end_date = datetime.now() + timedelta(days=30)
        self.p.leader_id = self.l.id
        self.p.save()
        # !!!!!!
        self.p.admins.add(self.adm)
        self.p.save()

        # Create member
        self.m = MemberUser(username='theseus', first_name='theseus', last_name='demigod')
        self.m.set_password('qwerty123')
        self.m.role_id = self.r.id
        self.m.project_id = self.p.id
        self.m.save()

    def Test_log_contains_info_member(self):
        log('INFO', self.m, 'test content')
        f = open(self.p.activitylog.content, 'r')
        logfile = f.readlines()[0]
        data = parse('[{}] [{}] [{}] [{}] [{}] [{}]', logfile)
        TestCase.assertEquals(self, data[0], 'INFO')
        TestCase.assertEquals(self, data[1], self.m.username)
        TestCase.assertEquals(self, data[2], 'MEMBER')
        TestCase.assertEquals(self, data[3], self.m.project.name)
        TestCase.assertEquals(self, data[5], 'test content')
        f.flush()
        f.close()

    def Test_log_contains_warning_leader(self):
        log('WARNING', self.l, 'leader log record')
        f = open(self.p.activitylog.content, 'r')
        logfile = f.readlines()[1]
        data = parse('[{}] [{}] [{}] [{}] [{}] [{}]', logfile)
        TestCase.assertEquals(self, data[0], 'WARNING')
        TestCase.assertEquals(self, data[1], self.l.username)
        TestCase.assertEquals(self, data[2], 'LEADER')
        TestCase.assertEquals(self, data[3], self.l.project.name)
        TestCase.assertEquals(self, data[5], 'leader log record')
        f.flush()
        f.close()

    def test_log_contains_all_records(self):
        """
        We have added two records, one each for leader and admin.
        This functions asserts if the log file contains two records.
        To make it more comprehensive, after the initial assertion,
        another record is add to the log and the number of records
        are tested once again.

        It calls the previous two methods so the logs are within the same
        execution context.
        :return:
        """
        self.Test_log_contains_info_member()
        self.Test_log_contains_warning_leader()

        logfile = open(self.p.activitylog.content, 'r').readlines()
        number_of_lines = len(logfile)
        TestCase.assertEquals(self, number_of_lines, 2)
