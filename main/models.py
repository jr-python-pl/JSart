from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    cv = models.TextField(verbose_name="Coś o sobie...", blank=True)
    image = models.ImageField(upload_to='authors_pictures/',null=True, blank=True)

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'
        ordering = ['username']

    def __str__(self):
        return self.username


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="author")
    title = models.CharField(max_length=128, default='Untitled', verbose_name="Title")
    description = models.TextField(verbose_name="description", blank=True)
    body = models.TextField(verbose_name="script body" ,null =False , blank=False )
    thumbnail = models.ImageField(upload_to='thumbs/', blank = False, null = False )




    def __str__(self):
        return f'Project: {self.title}, Author: {self.user}'


# class Comment(models.Model):
#     comment = models.TextField(verbose_name="Komentarz")
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Projekt")
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Użytkownik")
#     adding_date = models.DateTimeField(auto_now_add=True, verbose_name="Data/godzina dodania")
#     last_modified = models.DateTimeField(auto_now=True, verbose_name="Data/godzina edycji")
#
#
#     def __str__(self):
#         return f'{self.comment}, Użytkowni: {self.user}'
