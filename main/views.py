from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.http import HttpResponse

from users.models import CustomUser
from main.models import Project
from main.forms import ProjectForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from ranking.forms import RatingForm
from ranking.models import Rating


class Home(View):

    def get(self, request):
        return render(request, 'main/home.html')


class AuthorsView(View):

    def get(self, request):
        return render(request, 'main/authors.html', {'authors':CustomUser.objects.all()})


class PortfolioView(View):

    def get(self, request):
        return render(request, 'main/portfolio.html', {'projects':Project.objects.all()})


class ProjectView(View):

    def get(self, request, id):
        form = RatingForm()
        return render(request, 'main/project_view.html',{'projects': Project.objects.get(id=id), 'form' : form})

    def post(self, request, id):
        project1 = Project.objects.get(id=id)
        
        '''
         lines below to check if there is one or more rating given 
         for each project by one logged user
        -Mateusz-
        '''
          
        try:
            user_vote = Rating.objects.get(who_rated=request.user, project=project1 )
            user_vote = True
        except Rating.DoesNotExist:
            user_vote = False
        except Rating.MultipleObjectsReturned: 
            user_vote = True
        
        form = RatingForm(request.POST)
        if form.is_valid() and user_vote == False :
            vote_value = form.cleaned_data['rating']  # class str
            rating1 = Rating()
            rating1.rating = int(vote_value)
            rating1.project = project1
            rating1.who_rated=request.user
            rating1.save()
            
                  
            project1.average_rating = project1.mean_method()
            project1.save()

        vote = True
        return render(request, 'main/project_view.html', {'projects': Project.objects.get(id=id), 'vote': vote , 'user_vote':user_vote})


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


class AboutView(View):

    def get(self, request):
        return render(request, 'main/contact.html')


class ProjectFormView(View):

    def get(self, request):
        form = ProjectForm()
        return render(request, 'main/add_project.html', {'form': form})

    def post(self, request):
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            # form save with logged in user
            fmirror = form.save(commit=False)
            fmirror.user=request.user
            fmirror.save()
        return render(request,'main/add_project.html',{'form':form})




