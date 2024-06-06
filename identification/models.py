from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=11,
        null=True,
    )
    email = models.EmailField(unique=True)


    REQUIRED_FIELDS = ['email']