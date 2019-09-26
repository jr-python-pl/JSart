from django.shortcuts import render
from django.views import View
from main.models import Project


class RankingView(View):

    def get(self, request):
        top_projects = Project.objects.all().order_by('-average_rating')[:10]
        return render(request, 'ranking/ranking.html', {'projects': top_projects})
