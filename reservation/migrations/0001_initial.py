# Generated by Django 3.2.5 on 2021-07-25 06:01

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Заметка')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('name', models.CharField(max_length=128, verbose_name='Имя')),
                ('surname', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('start', models.TimeField(verbose_name='Начало брони')),
                ('end', models.TimeField(verbose_name='Конец брони')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата')),
                ('taste', models.CharField(blank=True, max_length=4096, null=True, verbose_name='Вкус')),
                ('sturdiness', models.PositiveSmallIntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Крепкость')),
                ('wishes', models.TextField(blank=True, null=True, verbose_name='Пожелания')),
                ('before_arrival', models.BooleanField(default=False, verbose_name='Забить до прихода')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reservation.table', verbose_name='Столик')),
            ],
        ),
    ]
