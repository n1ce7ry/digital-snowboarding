from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Souvenirs(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название сувенира')
    image = models.ImageField(upload_to='souvenirs/', verbose_name='Фотография сувенира')
    price = models.IntegerField(verbose_name='Цена сувенира')
    users = models.ManyToManyField(
        User,
        related_name='favorite_souvenirs',
        verbose_name='Пользователи, добавившие сувенир в избранное',
        blank=True,
    )


    class Meta:
        verbose_name = 'Сувенир'
        verbose_name_plural = 'Сувениры'


    def __str__(self) -> str:
        return self.name