from django import forms
from users.models import AdminUser, Project


class ListOfProject(forms.ModelForm):
    """
    Display the list of projects that have been modified
    """
    CHOICES = ('Open', 'Closed')
    projectID = forms.CharField(widget=forms.TextInput, label="Project ID")
    projectName = forms.CharField(widget=forms.TextInput, label="Project Name")
    projectStatus = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, label="Project Status")

    class Meta:
        model = Project
        fields = ['projectID', 'projectName', 'projectStatus']