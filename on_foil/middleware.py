import json
from urllib.parse import parse_qs

from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model

from django.conf import settings
from django.db import close_old_connections

from channels.db import database_sync_to_async

from jwt import decode as jwt_decode


User = get_user_model()

@database_sync_to_async
def close_connections():
    close_old_connections()

@database_sync_to_async
def get_user(user_jwt):
    try:
        return User.objects.get(id=user_jwt)
    except User.DoesNotExist:
        return AnonymousUser()


class SocketTokenAuthMiddleware:

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):

        await close_connections()

        query_string = parse_qs(scope["query_string"].decode("utf8"))

        if 'token' not in query_string:
            scope['user'] = AnonymousUser()
            return await self.inner(scope, receive, send)

        token = query_string["token"][0]

        try:
            UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            print(e)
            return None
        else:
            decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            scope['user'] = await get_user(decoded_data['user_id'])

        return await self.inner(scope, receive, send)