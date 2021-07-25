from celery import shared_task
from .models import Reservation


@shared_task
def clear_reservation():
	Reservation.objects.all().delete()