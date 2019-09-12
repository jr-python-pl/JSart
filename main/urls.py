from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import Home, ContactEmail, AboutView, PortfolioView, ProjectView, AddProjectView, AuthorsView, SuccessView,RunProjectScript
from django.utils.translation import ugettext_lazy as _


app_name = 'main'
urlpatterns = [

    path(_('main/'), Home.as_view(), name="home"),
    path(_('project/<int:id>'), ProjectView.as_view(), name="project_view"),
    path(_('run_project/<int:id>'), RunProjectScript.as_view(), name="runscript"),
    path(_('projects/'), PortfolioView.as_view(), name="portfolio"),
    path(_('about/'), AboutView.as_view(), name="about"),
    path(_('contact/'), ContactEmail.as_view(), name="contact"),
    path(_('success/'), SuccessView.as_view(), name='success'),
    path(_('add_project/'), AddProjectView.as_view(), name="add_project"),
    
    #authors
    path(_('authors/'), AuthorsView.as_view(), name="authors"),
    # urls translation with ugettext_lazy as __ doesn't work i will leave it as it is now (app works just fine)-Mateusz- 

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += path(
#         'django.views.static',
#         (r'^media/(?P<path>.*)',
#         'serve',
#         {'document_root': settings.MEDIA_ROOT}), )
