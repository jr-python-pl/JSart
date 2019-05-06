from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Project

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user')
    list_filter = ('title', 'user')
    search_fields = ('title', 'user')


