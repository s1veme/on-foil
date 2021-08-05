import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model

from django.db.models.signals import post_save
from django.dispatch import receiver

from .serializers import TableSerializer
from .models import Table


User = get_user_model()


class ReservationConsumer(AsyncJsonWebsocketConsumer):
	
	async def connect(self):
		user = self.scope.get('user')
		
		if user == AnonymousUser() or 'user' not in self.scope:
			await self.close(code=1000)
			return

		await self.channel_layer.group_add('admin', self.channel_name)
		await self.accept()

		reservation = await self.get_reservation_json()
		await self._send_message(
			{
				'reservation': reservation
			},
			'give_reservation'
		)

	async def receive_json(self, content):
		await self.channel_layer.group_send(self.model, {
			'type': 'send.data',
			'data': content
		})

	async def send_data(self, event):
		content = await self.validate_content(event)
		await self.send_json(content={
			'status': 'ok',
		 	'data': content['data'],
		 	'action': content['action']
			}
		)

	@classmethod
	async def validate_content(cls, content):
		if isinstance(content, dict) \
				and isinstance(content.get('action'), str) \
				and isinstance(content.get('data'), dict):
			return content

	@database_sync_to_async
	def get_reservation_json(self):
		reservation = TableSerializer(
			Table.objects.all(),
			many=True
		)

		return reservation.data

	async def _send_message(self, data, action=None):
		await self.send_json(content={'status': 'ok', 'data': data, 'action': action})

	async def disconnect(self, close_code):
		await self.channel_layer.group_discard(
			'admin',
			self.channel_name
		)


