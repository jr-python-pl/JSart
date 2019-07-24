from django import forms as main_forms
from django.core.validators import EmailValidator, URLValidator
from main.models import Project


class ProjectForm(main_forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','thumbnail','description','body']


class ContactForm(main_forms.Form):
    email = main_forms.EmailField(required=True)
    subject = main_forms.CharField(required=True)
    message = main_forms.CharField(widget=main_forms.Textarea, required=True)        
