from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.http import HttpResponse

from main.models import User, Project
from main.forms import MainUserCreationForm

class Home(View):
    # Home view
    def get(self, request):
        return render(request, 'main/home.html')
        # return HttpResponse("HOME PAGE")


class SignUPView(View):
    # Creating a new user
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = MainUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('main:home'))
        return render(request, 'registration/signup.html', {'form': form})
