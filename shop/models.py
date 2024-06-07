from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Souvenir(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название сувенира')
    image = models.ImageField(upload_to='souvenirs/', verbose_name='Фотография сувенира')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена сувенира')
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
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Клиент')
    first_name = models.CharField(max_length=255, verbose_name='Имя покупателя')
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона')
    address = models.CharField(max_length=455, verbose_name='Адрес')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Итоговая сумма')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    paid = models.BooleanField(default=False, verbose_name='Оплата заказа')

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return f'{self.user} оформил заказ на сумму {self.total_price}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Заказ')
    souvenir = models.ForeignKey(Souvenir, related_name='order_items', on_delete=models.PROTECT, verbose_name='Сувернир')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity