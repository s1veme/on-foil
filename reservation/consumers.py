import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model

from .serializers import ReservationSerializer
from .models import Reservation

User = get_user_model()


class ReservationConsumer(AsyncJsonWebsocketConsumer):
	async def connect(self):
		user = self.scope.get('user')

		if user == AnonymousUser() or 'user' not in self.scope:
			await self.close(code=1000)
			return

		await self.accept()

		reservation = await self.get_reservation_json()
		await self._send_message(
			{
				'reservation': reservation
			},
			'give_reservation'
		)


	async def receive_json(self, content, **kwargs):
		message = await self.validate_content(content)

		if not message:
			return await self._send_message({'detail': 'pass on action'})
		action = message['action']


	@classmethod
	async def validate_content(cls, content):
		if isinstance(content, dict) \
				and isinstance(content.get('action'), str) \
				and isinstance(content.get('data'), dict):
			return content


	@database_sync_to_async
	def get_reservation_json(self):
		reservation = ReservationSerializer(
			Reservation.objects.all(),
			many=True
		)

		return reservation.data


	async def _send_message(self, data, action=None):
		await self.send_json(content={'status': 'ok', 'data': data, 'action': action})

