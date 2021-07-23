from django.urls import path

from . import consumers


websocket_urlpatterns = [
    path('connect/<str:token>', consumers.ReservationConsumer.as_asgi())
]