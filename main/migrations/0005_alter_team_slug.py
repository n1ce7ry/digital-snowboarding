# Generated by Django 5.0.6 on 2024-06-08 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_team_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Слаг'),
        ),
    ]
