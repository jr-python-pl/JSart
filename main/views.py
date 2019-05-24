from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView,FormView
from django.http import HttpResponse

from main.models import User, Project
from main.forms import MainUserCreationForm,ProjectForm

class Home(View):

    def get(self, request):
        return render(request, 'main/home.html')
    
class Authors(View):

    def get(self, request):
        return render(request, 'main/authors.html' ,{'authors':User.objects.all()})    

class Portfolio(View):

    def get(self, request):
        return render(request, 'main/portfolio.html' ,{'projects':Project.objects.all()})

class Profile(View):

    def get(self, request):
        user = request.user
        return render(request, 'profile/profile.html' ,{'projects':Project.objects.filter(user=user)})


class ProjectView(View):

    def get(self, request, id):
        return render(request, 'main/project_view.html',{'projects':Project.objects.get(id=id)})




class Contact(View):

    def get(self, request):
        
        return render(request, 'main/contact.html')



class About(View):

    def get(self, request):
        return render(request, 'main/contact.html')


class ProjectForm(View):

    def get(self, request):
        form = ProjectForm()
        return render(request, 'profile/add_project.html', {'form': form})
    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'profile/add_project.html',{'form':form})




class SignUPView(View):
    # Creating a new user
    def get(self, request):
        form = MainUserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = MainUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.email = form.cleaned_data.get('email')
            new_user.cv = form.cleaned_data.get('cv')
            new_user.image = form.cleaned_data.get('image')
            new_user.save()
            # authenticate and login new user
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('main:home'))
        return render(request, 'registration/signup.html', {'form': form})
