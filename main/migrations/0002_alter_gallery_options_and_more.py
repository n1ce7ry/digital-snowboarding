# Generated by Django 5.0.6 on 2024-06-04 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Фото', 'verbose_name_plural': 'Галлерея'},
        ),
        migrations.AlterModelOptions(
            name='interestingfactaboutplayer',
            options={'verbose_name': 'Интересный факт об игроке', 'verbose_name_plural': 'Интересные факты об игроке'},
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'verbose_name': 'Игрок', 'verbose_name_plural': 'Игроки'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Команда', 'verbose_name_plural': 'Команды'},
        ),
        migrations.CreateModel(
            name='GameSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата и время проведения')),
                ('location', models.CharField(max_length=255, verbose_name='Место проведения')),
                ('player_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_one', to='main.player', verbose_name='Игрок 1')),
                ('player_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_two', to='main.player', verbose_name='Игрок 2')),
            ],
        ),
    ]
