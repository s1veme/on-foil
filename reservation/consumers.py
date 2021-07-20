import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ReservationConsumer(AsyncWebsocketConsumer):

	async def connect(self):
		self.item_id = 1

		await self.channel_layer.group_add(
			self.item_id,
			self.channel_name
		)
  
	
	async def disconnect(self):
		await self.channel_layer.discard(
			self.item_id,
			self.channel_name
		)