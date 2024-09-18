from django.forms import ModelForm, Form
from django import forms
from .models import Client, Project, User


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class ProjectForm(ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Project
        fields = '__all__'
