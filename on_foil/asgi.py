import os

from channels.routing import ProtocolTypeRouter, URLRouter
from .middleware import SocketTokenAuthMiddleware

from django.core.asgi import get_asgi_application

import reservation.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochannels.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": SocketTokenAuthMiddleware(
        URLRouter(
            reservation.routing.websocket_urlpatterns
        )
    ),
})
