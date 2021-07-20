import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

import reservation.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'on_foil.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            reservation.routing.websocket_urlpatterns
        )
    )
})
