"""JSart URL Configuration
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', users_views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),

    path('password_change/', users_views.ChangePasswordView.as_view(), name="password-change"),
    path('password_change/done/', users_views.ChangePasswordDone.as_view(), name="password-change-done"),

    path('password_reset/', users_views.ResetPasswordView.as_view(
        template_name='users/password_reset_form.html'), name="password_reset"),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name="password_reset_done"),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name="password_reset_complete"),

    path('profile/<username>/', users_views.ProfileView.as_view(), name='profile'),
    path('profile/<username>/edit/', users_views.ProfileEditView.as_view(), name="profile_edit"),

    path('', include('main.urls')),
    path('', include('ranking.urls')),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

