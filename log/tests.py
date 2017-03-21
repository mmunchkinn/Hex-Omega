from django.test import TestCase

from datetime import datetime, timedelta
from parse import *

from users.models import *
from log.Log import log

from sample_data import setup


# Create your tests here.
class LogTest(TestCase):
    def setUp(self):
        pass

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

        f = open(self.p.activitylog.content, 'r')
        logfile = f.readlines()
        number_of_lines = len(logfile)
        TestCase.assertEquals(self, number_of_lines, 2)
        f.close()
        os.remove(self.p.activitylog.content)
