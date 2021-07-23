import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from django.contrib.auth import get_user_model


User = get_user_model()

class ReservationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.token = self.scope['url_route']['kwargs']['token']

        if 'user' not in self.scope:
            await self._send_message({'detail': 'Authorization failed'})
            await self.close(code=1000)
            return

        await self.accept()  


    @database_sync_to_async
    def get_user(self, pk):
        user = User.objects.get(id=pk)
        return user


    async def _send_message(self, data):
        await self.send_json(content={'status': 'ok', 'data': data,})


    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.item_id,
            self.channel_name
        )

