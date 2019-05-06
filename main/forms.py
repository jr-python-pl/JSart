from django import forms
from django.core.validators import EmailValidator, URLValidator
from main.models import User, Project
from django.contrib.auth import forms


class MainUserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
