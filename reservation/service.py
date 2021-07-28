import os

from io import BytesIO

from django.template.loader import get_template
from django.template import Context

from xhtml2pdf import pisa

from datetime import datetime, timedelta

from django.conf import settings


def yesterday_date():
	date_format = '%Y-%m-%d'
	today = datetime.now()
	tomorrow = today - timedelta(days=1)
	return {
		'tomorrow': tomorrow.strftime(date_format),
	}


def today_date():
	date_format = '%d-%m-%Y'
	today = datetime.now()
	return {
		'today': today.strftime(date_format),
	}


def check_difference_time(start, end):
	FMT = '%H:%M'
	tdelta = datetime.strptime(end, FMT) - datetime.strptime(start, FMT)

	if tdelta >= timedelta(hours=1, minutes=30):
		return True
	return False


def fetch_pdf_resources(uri, rel):
	if uri.find(settings.MEDIA_URL) != -1:
		path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
	elif uri.find(settings.STATIC_URL) != -1:
		path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
	else:
		path = None
	return path


def generate_pdf(params: dict):
	yesterday = yesterday_date()
	file_path = f'{settings.BASE_DIR}/reports/{yesterday["tomorrow"]}.pdf'

	params.update(yesterday)

	template = get_template('reservation/pdf.html')
	html = template.render(params)

	with open(file_path, 'wb+') as file:
		pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), file,
																   encoding='utf-8',
																   link_callback=fetch_pdf_resources)

	return file_path, True

