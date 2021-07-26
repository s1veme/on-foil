from django.urls import path

from .views import ReservationCreateAPIView, TestPDF


urlpatterns = [
	path('create-reservation', ReservationCreateAPIView.as_view()),
	path('test', TestPDF.as_view())
]