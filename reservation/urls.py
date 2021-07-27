from django.urls import path

from .views import (
	ReservationCreateAPIView,
	ReservationTimeListAPIView
)


urlpatterns = [
	path('create-reservation', ReservationCreateAPIView.as_view()),
	path('reservation-time', ReservationTimeListAPIView.as_view())
]