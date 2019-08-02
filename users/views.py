from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import CustomUserCreationForm, ProfileEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import CustomUser


from django.contrib.auth import login, authenticate
# from main.forms import import MainUserCreationForm


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
        # user = request.user
        return render(request, 'users/profile.html', {'author': CustomUser.objects.get(username=username)})


class ProfileEditView(View):

    def get(self, request, username):
        user = request.user
        initial_data = {
            "cv": user.cv,
            "image": user.image,
            "email": user.email
        }

        form = ProfileEditForm(initial=initial_data)
        return render(request, 'users/profile_edit.html',
                      {'author': CustomUser.objects.get(username=username), 'form': form})

    def post(self, request):
        form = ProfileEditForm(request.POST, request.FILES)
        if form.is_valid():
            fmirror = form.save(commit=False)
            fmirror.user = request.user
            fmirror.save()

            return render(request, 'profile/profile_edit.html',
                          {'author': CustomUser.objects.get(username=fmirror.username), 'form': form})


