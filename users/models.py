from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='profile_image', blank=True, verbose_name='Изображения профиля')
    moneybag_id = models.TextField(blank=False, null=False, verbose_name='Идентификатор счета')
