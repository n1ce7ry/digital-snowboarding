from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Souvenir(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название сувенира')
    image = models.ImageField(upload_to='souvenirs/', verbose_name='Фотография сувенира')
    price = models.FloatField(verbose_name='Цена сувенира')
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


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    souvenirs = models.ManyToManyField(
        Souvenir,
        verbose_name='Заказанные сувениры',
        related_name='order',
    )
    first_name = models.CharField(max_length=255, verbose_name='Имя покупателя')
    address = models.CharField(max_length=455, verbose_name='Адрес')
    total_price = models.FloatField(verbose_name='Итоговая сумма')
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    def __str__(self) -> str:
        return f'{self.user} оформил заказ'