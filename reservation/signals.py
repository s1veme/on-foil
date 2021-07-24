from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Reservation
from .serializers import ReservationSerializer


@receiver(post_save, sender=Reservation)
def check_new_reservation(sender, instance, **kwargs):
	reservation = ReservationSerializer(instance).data
	channel_layer = get_channel_layer()
	async_to_sync(channel_layer.group_send)('admin', {
		'type': 'send.data',
		'data': {
			'reservation': reservation
		},
		'action': 'add_reservation'
	})