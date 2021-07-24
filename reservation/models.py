from django.db import models
from django.core.validators import MaxValueValidator


class Reservation(models.Model):
	phone_number = models.CharField(
		'Номер телефона',
		max_length=20
	)
	name = models.CharField(
		'Имя',
		max_length=128
	)
	surname = models.CharField(
		'Фамилия',
		max_length=128
	)
	start = models.TimeField(
		'Начало брони',
     	auto_now=False,
      	auto_now_add=False,
    )
	end = models.TimeField(
		'Конец брони',
     	auto_now=False,
      	auto_now_add=False,
    )
	date = models.DateField(
		'Дата',
	)
	taste = models.CharField(
		'Вкус',
		max_length=4096
	)
	sturdiness = models.PositiveSmallIntegerField(
		'Крепкость',
		default=1,
		validators=[
			MaxValueValidator(10)
		]
	)
 	wishes = models.TextField(
		'Пожелания'
	)
	before_arrival = models.BooleanField(
		'Забить до прихода',
		default=False
	)