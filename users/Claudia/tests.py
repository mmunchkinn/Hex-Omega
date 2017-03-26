from django.test import TestCase
from users.models import AdminUser
from users.Claudia.user_form import AdminUserForm


class AdminModelTest(TestCase):
    def setup(self):
        test_user1 = AdminUser.objects.create_user(username='12341234', first_name='Jack', last_name='Tan', email='jack_tan@gmail.com')
        test_user1.save()
        test_user2 = AdminUser.objects.create_user(username='22334455', first_name='Megan', last_name='Smith', email='megan_smith@gmail.com')
        test_user2.save()