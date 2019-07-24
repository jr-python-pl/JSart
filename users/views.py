from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib import messages
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

            # new_user = form.save()
            # new_user.email = form.cleaned_data.get('email')
            # new_user.cv = form.cleaned_data.get('cv')
            # new_user.image = form.cleaned_data.get('image')
            # new_user.save()
            # # authenticate and login new user
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            # return redirect(reverse('main:home'))
        # return render(request, 'registration/signup.html', {'form': form})

# class SignUPView(View):
#     # Creating a new user
#     def get(self, request):
#         form = MainUserCreationForm()
#         return render(request, 'registration/signup.html', {'form': form})
#
#     def post(self, request):
#         form = MainUserCreationForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             new_user.email = form.cleaned_data.get('email')
#             new_user.cv = form.cleaned_data.get('cv')
#             new_user.image = form.cleaned_data.get('image')
#             new_user.save()
#             # authenticate and login new user
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect(reverse('main:home'))
#         return render(request, 'registration/signup.html', {'form': form})
#
#
#

