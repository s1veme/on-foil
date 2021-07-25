from aiogram import Bot

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Reservation
from .serializers import TableSerializer


bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
text_message = """
	Новая бронь!
	Имя Фамилия: {} {}
	Номер телефона: {}

	Время: {}-{}
	Дата: {}
	Столик: {}

	Вкус: {}
	Крепоксть: {}
	Забить до прихода: {}
	Пожелания: {}
"""


@receiver(post_save, sender=Reservation)
def check_new_reservation(sender, instance, **kwargs):
	reservation = TableSerializer(instance.table).data
	# hard code
	async_to_sync(bot.send_message)(
		chat_id=settings.TELEGRAM_CHAT_ID,
		text=text_message.format(
			instance.name,
			instance.surname,
			instance.phone_number,
			instance.start,
			instance.end,
			instance.table,
			instance.taste,
			instance.sturdiness,
			instance.before_arrival,
			instance.wishes
		)
	)
	channel_layer = get_channel_layer()
	async_to_sync(channel_layer.group_send)('admin', {
		'type': 'send.data',
		'data': {
			'detail': reservation
		},
		'action': 'add_reservation'
	})
