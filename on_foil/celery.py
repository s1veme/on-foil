import os

from celery import Celery
from celery.schedules import crontab

from datetime import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'on_foil.settings')

app = Celery('on_foil')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
	'reservation-tasks': {
		'task': 'reservation.tasks.clear_reservation_and_report',
		'schedule': crontab(hour=1, minute=30)
	}
}