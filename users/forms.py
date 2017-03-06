from django import forms
from users.models import AdminUser, Project


class AdminForm(forms.ModelForm):
    """
    Form for an admin user account
    """
    first_name = forms.CharField(widget=forms.TextInput, label="First Name")
    last_name = forms.CharField(widget=forms.TextInput, label="Last Name")
    email = forms.EmailField(widget=forms.TextInput, label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Re-enter Password")
    bio = forms.CharField(widget=forms.Textarea, label="Bio")

    class Meta:
        model = AdminUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'bio']


class ListOfProject(forms.ModelForm):
    """
    Display the list of projects that have been modified
    """
    projectID = forms.CharField(widget=forms.TextInput, label="Project ID")
    projectName = forms.CharField(widget=forms.TextInput, label="Project Name")
    projectStatus = forms.CharField(widget=forms.TextInput, label="Project Status")

    class Meta:
        model = Project
        fields = ['projectID', 'projectName', 'projectStatus']