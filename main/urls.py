from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from main.views import Home, ContactEmail, AboutView, PortfolioView, ProjectView, ProjectFormView, AuthorsView, SuccessView



app_name = 'main'
urlpatterns = [

    path('main/', Home.as_view(), name="home"),
    path('project/<int:id>', ProjectView.as_view(), name="project_view"),
    path('portfolio/', PortfolioView.as_view(), name="portfolio"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactEmail.as_view(), name="contact"),
    path('success/', SuccessView.as_view(), name='success'),
    path('add_project/', ProjectFormView.as_view(), name="add_project"),

    #authors
    path('authors/', AuthorsView.as_view(), name="authors"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += path(
#         'django.views.static',
#         (r'^media/(?P<path>.*)',
#         'serve',
#         {'document_root': settings.MEDIA_ROOT}), )
