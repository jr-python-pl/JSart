from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _



def image_dir_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/authors_pictures/auth_id<id>_<filename>
    dir_name = "authors_pictures"
    return f'{dir_name}/user_id{instance.user.id}_{filename}'


class CustomUser(AbstractUser):

    email = models.EmailField(_('email adress'), unique=True)
    cv = models.TextField(_("Few words about you..."), blank=True)
    image = models.ImageField(upload_to=image_dir_path, null=True, blank=True)

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'
        ordering = ['username']

    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.username



