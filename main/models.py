from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название команды')
    logo = models.ImageField(upload_to='team_logos/', verbose_name='Логотип команды')
    full_name = models.CharField(max_length=300, verbose_name='Полное название команды')
    country = models.CharField(max_length=100, verbose_name='Страна команды')
    captain = models.CharField(max_length=255, verbose_name='Капитан команды')
    year_of_foundation = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(9999)],
        verbose_name='Год основания',
    )
    interesting_fact = models.CharField(max_length=500, verbose_name='Интересный факт о команде')


    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class Player(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Полное имя')
    birthday = models.DateField(verbose_name='Дата рождения')
    nationality = models.CharField(max_length=255, verbose_name='Гражданство')
    city = models.CharField(max_length=255, verbose_name='Город')
    height = models.PositiveSmallIntegerField(verbose_name='Рост')
    weight = models.PositiveSmallIntegerField(verbose_name='Вес')
    quote = models.CharField(max_length=500, verbose_name='Цитата')
    photo = models.ImageField(upload_to='player_photos/', verbose_name='Фото игрока')
    label_photo = models.ImageField(upload_to='player_label_photos/', verbose_name='Дополнительное фото игрока')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Команда игрока')
    

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


    def __str__(self) -> str:
        return self.full_name


class InterestingFactAboutPlayer(models.Model):
    fact = models.CharField(max_length=255, verbose_name='Интересный факт')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='Игрок')
    

    class Meta:
        verbose_name = 'Интересный факт о игроке'
        verbose_name_plural = 'Интересные факты о игроке'


    def __str__(self) -> str:
        return self.fact


class Gallery(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        verbose_name='Игрок связанный с фото',
        null=True, blank=True,
    )
    photo = models.ImageField(upload_to='gallery/', verbose_name='Фото')
    

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Галлерея'


    def __str__(self) -> str:
        return f'Фотография №{self.id}'