from django.db import models
from main.models import Project

class Rating(models.Model):

    rvalues = ((1,1),
              (2,2),
              (3,3),
              (4,4),
              (5,5))

    rating = models.PositiveSmallIntegerField(choices=rvalues)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE) (import user)

    def __str__(self):
        return str(self.rating)