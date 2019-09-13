from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from .forms import CustomUserCreationForm, ProfileEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser

from django.contrib.auth import login, authenticate
# from main.forms import import MainUserCreationForm


class ChangePasswordView(PasswordChangeView):
    success_url = reverse_lazy('password-change-done')
    template_name = 'users/password_change.html'

class ChangePasswordDone(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'

class ResetPasswordView(PasswordResetView):
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    template_name = 'users/password_reset_form.html'


class RegisterView(View):

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.username = form.cleaned_data.get('username')
            new_user.email = form.cleaned_data.get('email')
            new_user.cv = form.cleaned_data.get('cv')
            # new_user.image = form.cleaned_data.get('image')
            new_user.save()
            # # authenticate and login new user
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            messages.success(request, f'Your Account has been created! You are now able to log in')
            return redirect(reverse('login'))
        return render(request, 'users/register.html', {'form': form})


class ProfileView(View):

    # @login_required
    def get(self, request, username):
        return render(request, 'users/profile.html', {'author': CustomUser.objects.get(username=username)})


class ProfileEditView(View):

    def get(self, request, username):
       
        form = ProfileEditForm(instance=request.user)
        return render(request, 'users/profile_edit.html',
                      {'author': CustomUser.objects.get(username=username), 'form': form})

    def post(self, request, username):
        form = ProfileEditForm(request.POST, request.FILES,instance=request.user)
        if form.is_valid():
            fmirror = form.save(commit=False)
            fmirror.user = request.user
            fmirror.save()
            
            
            messages.success(request, f'Your Profile has been updated !')
            
        return render(request, 'users/profile_edit.html',{'author': CustomUser.objects.get(username=username), 'form': form})


