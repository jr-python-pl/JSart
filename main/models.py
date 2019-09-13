from django.db import models
from users.models import CustomUser
from django.utils.translation import ugettext_lazy as _


class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="author")
    title = models.CharField(max_length=128, default=_('Untitled'), verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("description"), blank=True)
    body = models.TextField(verbose_name=_("script body") ,null =False , blank=False )
    thumbnail = models.ImageField(verbose_name=_("thumbnail"),upload_to='thumbs/', blank = False , null = False )
    average_rating = models.DecimalField(default=0, max_digits=4, decimal_places=2)


    def __str__(self):
        return f'Project: {self.title}, Author: {self.user}'

    def mean_method(self):
        suma = 0
        for pr in self.rating_set.all():
            suma += pr.rating
        try:
            suma / self.rating_set.all().count()
        except ZeroDivisionError:
            return 0
        return suma / self.rating_set.all().count()


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
