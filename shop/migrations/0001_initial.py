# Generated by Django 5.0.6 on 2024-06-05 08:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Souvenirs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название сувенира')),
                ('image', models.ImageField(upload_to='souvenirs/', verbose_name='Фотография сувенира')),
                ('price', models.IntegerField(verbose_name='Цена сувенира')),
                ('users', models.ManyToManyField(related_name='favorite_souvenirs', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи, добавившие сувенир в избранное')),
            ],
            options={
                'verbose_name': 'Сувенир',
                'verbose_name_plural': 'Сувениры',
            },
        ),
    ]
