from celery import shared_task

from .service import (
	yesterday_date,
)

from .models import Reservation


@shared_task
def clear_reservation_and_report():
	Reservation.objects.filter(
		date=yesterday_date
	).delete()