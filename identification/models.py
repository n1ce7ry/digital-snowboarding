from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(
        verbose_name='Номер телефона',
        max_length=11,
    )
    email = models.EmailField(unique=True, verbose_name='Электронная почта')

    REQUIRED_FIELDS = ['email']