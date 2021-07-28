from celery import shared_task

from django.core.mail import EmailMessage
from django.conf import settings

from .serializers import TableSerializer

from .models import (
	Table,
	Reservation
)

from .service import (
	yesterday_date,
	generate_pdf
)


@shared_task
def clear_reservation_and_report():
	yesterday = yesterday_date()['tomorrow']

	tables = TableSerializer(
		Table.objects.filter(reservation__date=yesterday),
		many=True
	).data

	file_path, _ = generate_pdf({'reservation_data': tables})
	content = open(file_path, 'rb').read()
	Reservation.objects.filter(
		date__lte=yesterday
	).delete()

	message = EmailMessage(
		f'[ОТЧЁТ] Отчёт за {yesterday}',
		'Отчёт!',
		f'{settings.EMAIL_HOST_USER}',
		(settings.EMAIL_HOST_USER,)
	)
	message.attach(file_path, content)
	message.send()

	return True