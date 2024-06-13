from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Hall(models.Model):
    name = models.CharField(max_length=355, verbose_name='Площадка')
    rows = models.PositiveIntegerField(verbose_name='Количество рядов')
    columns = models.PositiveIntegerField(verbose_name='Количество мест в каждом ряду')
    price_per_seat = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за одно место')

    class Meta:
        verbose_name = 'Площадка'
        verbose_name_plural = 'Площадки'

    def __str__(self) -> str:
        return self.name


class Seat(models.Model):
    row = models.PositiveIntegerField(verbose_name='Ряд')
    column = models.PositiveIntegerField(verbose_name='Место')
    hall = models.ForeignKey(Hall, on_delete=models.PROTECT, verbose_name='Площадка')
    booked_by = models.ForeignKey(User,
                                  on_delete=models.PROTECT,
                                  blank=True, null=True,
                                  verbose_name='Забронированно пользователем')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        verbose_name = 'Забронированное место'
        verbose_name_plural = 'Забронированные места'

    def __str__(self) -> str:
        return f'{self.row} ряд, {self.column} место'


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Клиент', null=True, blank=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя покупателя')
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона')
    game = models.ForeignKey('main.GameSchedule', on_delete=models.PROTECT, verbose_name='Игра')
    booked_seat = models.ForeignKey(Seat, on_delete=models.CASCADE, verbose_name='Забронированное место')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    def __str__(self) -> str:
        if self.user:
            return f'Билет #{self.id} куплен пользователем {self.user.username}'
        else:
            return f'Билет #{self.id} куплен анонимным пользователем'