from django.test import TestCase
from users.models import AdminUser
from users.Claudia.user_form import AdminUserForm


class AdminModelTest(TestCase):
    def setUp(self):
        adm01 = AdminUser.objects.create_user(username='12341234', first_name='Aaron', last_name='Hotchner', email='aaron_hotchner@gmail.com', phone='88770000')
        adm01.save()
        adm02 = AdminUser.objects.create_user(username='22334455', first_name='Megan', last_name='Smith', email='megan_smith@gmail.com', phone='98701122')
        adm02.save()

    def test_phone_max_length(self):
        user = AdminUser.objects.get(pk=2)
        max_length = user._meta.get_field('phone').max_length
        self.assertEquals(max_length, 15)