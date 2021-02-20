from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


def get_upload_path(instance, filename):
    return f'user_avatars/{instance.username}/{filename}'


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email
