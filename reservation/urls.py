from django.urls import (
	path,
	re_path
)

from .views import (
	ReservationCreateAPIView,
	TableTimeListAPIView,
	ReservationListAPIView
)


urlpatterns = [
	path('create-reservation', ReservationCreateAPIView.as_view()),
	path('tables-time', TableTimeListAPIView.as_view()),
	re_path(r'^reservation-time/(?P<table>\d+)/(?P<date>\d{4}-\d{2}-\d{2})/$', ReservationListAPIView.as_view())
]