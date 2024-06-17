# Generated by Django 5.0.6 on 2024-06-17 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_gameschedule_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
            ],
            options={
                'verbose_name': 'Почта',
                'verbose_name_plural': 'Почтовые адреса для рассылки',
            },
        ),
    ]
