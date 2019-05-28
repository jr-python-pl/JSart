from django import forms as main_forms
from django.core.validators import EmailValidator, URLValidator
from main.models import User, Project
from django.contrib.auth import forms


class MainUserCreationForm(forms.UserCreationForm):
    email = main_forms.EmailField(required=True, label='Email')
    cv = main_forms.CharField(widget=main_forms.Textarea(attrs={'rows': 5, 'cols': 35}), label='Coś o sobie...')
    image = main_forms.ImageField(required=False)

    class Meta(forms.UserCreationForm.Meta):
        model = User


class ProjectForm(main_forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','thumbnail','description','body']
