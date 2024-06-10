from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название команды')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    logo = models.ImageField(upload_to='team_logos/', verbose_name='Логотип команды')
    team_photo= models.ImageField(upload_to='team_photos/', verbose_name='Фото команды')
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
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    birthday = models.DateField(verbose_name='Дата рождения')
    nationality = models.CharField(max_length=255, verbose_name='Гражданство')
    city = models.CharField(max_length=255, verbose_name='Город')
    height = models.PositiveSmallIntegerField(verbose_name='Рост')
    weight = models.PositiveSmallIntegerField(verbose_name='Вес')
    quote = models.CharField(max_length=500, verbose_name='Цитата')
    photo = models.ImageField(upload_to='player_photos/', blank=True, null=True, verbose_name='Фото игрока')
    label_photo = models.ImageField(upload_to='player_label_photos/', verbose_name='Дополнительное фото игрока')
    label_team_photo = models.ImageField(upload_to='player_label_team_photos/', verbose_name='Фото игрока для страницы команды')
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
        verbose_name = 'Интересный факт об игроке'
        verbose_name_plural = 'Интересные факты об игроке'

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
        verbose_name_plural = 'Галерея'

    def __str__(self) -> str:
        return f'Фотография №{self.id}'


class GameSchedule(models.Model):
    player_one = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        verbose_name='Игрок 1',
        related_name='player_one',
    )
    player_two = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        verbose_name='Игрок 2',
        related_name='player_two',
    )
    date = models.DateTimeField(verbose_name='Дата и время проведения')
    location = models.CharField(max_length=255, verbose_name='Место проведения')

    class Meta:
        verbose_name = 'Матч'
        verbose_name_plural = 'Расписание игр'

    def __str__(self) -> str:
        return f'{self.player_one} VS {self.player_two} (Дата: {self.date}, Место: {self.location})'