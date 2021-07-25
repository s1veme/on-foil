from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from bot.management.commands.bot import bot

from .models import Reservation
from .serializers import TableSerializer


@receiver(post_save, sender=Reservation)
def check_new_reservation(sender, instance, **kwargs):
	reservation = TableSerializer(instance.table).data
	async_to_sync(
		bot.send_message(
			811495961,
			text='hello'
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
