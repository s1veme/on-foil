import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'on_foil.settings')

app = Celery('on_foil')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
