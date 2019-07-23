"""JSart URL Configuration
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from users import views as users_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', users_views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('profile/<username>', users_views.ProfileView.as_view(), name='profile'),
    path('profile/<username>/edit', users_views.ProfileEditView.as_view(), name="profile_edit"),

    path('', include('main.urls')),
    path('', include('ranking.urls')),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

