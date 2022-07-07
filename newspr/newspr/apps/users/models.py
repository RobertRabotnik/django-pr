from django.db import models
from django.contrib.auth.models import AbstractUser
from traitlets import default

# Create your models here.

class CustomUser(AbstractUser):
    image = models.ImageField('Аватар',upload_to='images/avatar/',blank=True,default='images/avatar/avatar_default.jpg')

    class Meta:
        app_label = 'users'

