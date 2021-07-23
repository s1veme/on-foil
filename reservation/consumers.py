import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from django.contrib.auth import get_user_model


User = get_user_model()

class ReservationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope["user"]
        await self.accept()  


    @database_sync_to_async
    def get_user(self, pk):
        user = User.objects.get(id=pk)
        return user


    async def _send_message(self, data):
        await self.send_json(content={'status': 'ok', 'data': data,})

