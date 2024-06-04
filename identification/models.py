from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomUser(AbstractUser):
    phone = models.IntegerField(
        verbose_name='Телефон',
        validators=[MaxValueValidator(11)],
        null=True,
    )