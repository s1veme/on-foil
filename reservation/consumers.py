import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ReservationConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.item_id = 1
        await self.channel_layer.group_add(
            self.item_id,
            self.channel_name
        )
        await self.accept()  
    
    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.item_id,
            self.channel_name
        )