# Generated by Django 2.2.16 on 2021-08-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20210813_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(help_text='Укажите адрес для страницы жанра. Используйте только латиницу, цифры, дефисы и знаки подчёркивания', verbose_name='Адрес'),
        ),
    ]
