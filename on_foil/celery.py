import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'on_foil.settings')

app = Celery('on_foil')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
	'reservation-tasks': {
		'task': 'reservation.clear_reservation',
		'schedule': crontab(hour=1, minute=30),
	}
}