from django.test import TestCase
from users.models import AdminUser
from users.user_form import AdminUserForm


# Create your tests here.
class AdminModelTest(TestCase):
    def setUp(self):
        test_user1 = AdminUser.objects.create_user(username='12341234', first_name='Jack', last_name='Tan', email='jack_tan@gmail.com')
        test_user1.save()

    def test_first_name_label(self):
        user = AdminUser.objects.get(pk=2)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_first_name_max_length(self):
        user = AdminUser.objects.get(pk=2)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 30)

    def test_last_name_label(self):
        user = AdminUser.objects.get(pk=2)
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_last_name_max_length(self):
        user = AdminUser.objects.get(pk=2)
        max_length = user._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 30)


class AdminUserFormTest(TestCase):
    def test_adminuser_form_username_field(self):
        username = "12345678900"
        first_name = "Mary"
        last_name = "Jones"
        email = "mary_jones@gmail.com"
        password = "qwerty123"
        bio = "Test"
        form_data = {'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password, 'bio': bio}
        form = AdminUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_adminuser_form_password_field(self):
        username = "12345678"
        first_name = "Mary"
        last_name = "Jones"
        email = "mary_jones@gmail.com"
        password = "12345"
        bio = "Test"
        form_data = {'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password, 'bio': bio}
        form = AdminUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_adminuser_form(self):
        username = "12345678"
        first_name = "Mary"
        last_name = "Jones"
        email = "mary_jones@gmail.com"
        password = "qwerty123"
        bio = "Test"
        form_data = {'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password, 'bio': bio}
        form = AdminUserForm(data=form_data)
        self.assertTrue(form.is_valid())