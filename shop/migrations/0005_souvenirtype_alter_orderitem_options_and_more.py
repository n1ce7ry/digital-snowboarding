# Generated by Django 5.0.6 on 2024-06-07 12:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order_phone_alter_order_created_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SouvenirType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Тип сувенира')),
            ],
            options={
                'verbose_name': 'Тип сувенира',
                'verbose_name_plural': 'Типы сувениров',
            },
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
        migrations.AddField(
            model_name='souvenir',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.souvenirtype', verbose_name='Тип сувенира'),
        ),
    ]
