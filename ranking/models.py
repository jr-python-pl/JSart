from django.db import models
from main.models import Project
from users.models import CustomUser


class Rating(models.Model):

    rvalues = ((1,1),
              (2,2),
              (3,3),
              (4,4),
              (5,5))

    rating = models.PositiveSmallIntegerField(choices=rvalues)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    who_rated = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null =False , blank=False)

    def __str__(self):
        return str(self.who_rated)