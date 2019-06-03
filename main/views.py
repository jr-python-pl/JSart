from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView,FormView
from django.http import HttpResponse

from main.models import User, Project
from main.forms import MainUserCreationForm,ProjectForm, ContactForm
from django.core.mail import send_mail, BadHeaderError


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

    def get(self, request, username):
        # user = request.user
        return render(request, 'profile/profile.html' ,{'author':User.objects.get(username=username)})

class ProfileEdit(View):
    
    

    def get(self, request, username):
        
        user = request.user
        initial_data = {
            "cv" : user.cv,
            "image":user.image,
            "email":user.email
        }
       
        form = MainUserCreationForm(initial=initial_data)
        return render(request, 'profile/profile_edit.html' ,{'author':User.objects.get(username=username),'form':form})
    def post(self, request):
        form = MainUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'profile/profile_edit.html' ,{'author':User.objects.get(username=username),'form':form})


class ProjectView(View):

    def get(self, request, id):
        return render(request, 'main/project_view.html',{'projects':Project.objects.get(id=id)})


class ContactEmail(View):

    def get(self, request):
        form = ContactForm()
        return render(request, 'main/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['admin@example.com', 'innyemail@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect(reverse('main:success'))

        return render(request, 'main/contact.html', {'form': form})


class SuccessView(View):

    def get(self, request):
        return HttpResponse('Success! Thank you for your message.')


class About(View):

    def get(self, request):
        return render(request, 'main/contact.html')


class ProjectFormView(View):

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
