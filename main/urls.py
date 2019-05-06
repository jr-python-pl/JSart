from django.urls import path
from django.contrib.auth import views as auth_views

from main.views import Home, SignUPView

app_name = 'main'
urlpatterns = [
    path('main/', Home.as_view(), name="home"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': ''}, name="logout"),
    path('signup/', SignUPView.as_view(), name="signup"),

]


