from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

from django.contrib.auth import forms as forms2


# CustomUserCreationForm and CustomUserChangeForm are new versions of forms for CustomUser
# do not change


class CustomUserCreationForm(UserCreationForm):

    # email = forms.EmailField(required=True, label='Email')
    # cv = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 35}), label='Coś o sobie...')
    # image = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'cv']



class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ['username', 'email', 'cv']

# ==============================================

class CustomUserRegisterForm(UserCreationForm):

    email = forms.EmailField(required=True, label='Email')
    cv = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 35}), label='Coś o sobie...')
    image = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'cv']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['cv','email','image']

