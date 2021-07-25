import datetime
from django.db import models
from django.core.validators import MaxValueValidator


class Table(models.Model):
	notes = models.TextField(
		'Заметка',
		blank=True,
		null=True
	)

	def __str__(self):
		return str(self.id)


class Reservation(models.Model):
	table = models.ForeignKey(
		Table,
		on_delete=models.PROTECT,
		verbose_name='Столик',
	)
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
		default=datetime.date.today
	)
	taste = models.CharField(
		'Вкус',
		max_length=4096,
		blank=True,
		null=True
	)
	sturdiness = models.PositiveSmallIntegerField(
		'Крепкость',
		default=1,
		validators=[
			MaxValueValidator(10)
		],
		blank=True,
		null=True
	)
	wishes = models.TextField(
		'Пожелания',
		blank=True,
		null=True
	)
	before_arrival = models.BooleanField(
		'Забить до прихода',
		default=False,
	)

	def __str__(self):
		return f'{self.name} {self.surname}'