from django import forms


class AddUserForm(forms.Form):
    project_id = forms.IntegerField(label='Project ID')
    username = forms.CharField(label='Username', max_length=10)
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    role_id = forms.IntegerField(label='Role ID')
    bio = forms.CharField(label='Bio', widget=forms.Textarea)