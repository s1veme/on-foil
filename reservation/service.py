import os

from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

from datetime import datetime, timedelta

from django.conf import settings


# copy-past function in on_foil.context_processors
def yesterday_date():
    date_format = '%d-%m-%Y'
    today = datetime.now()
    tomorrow = today - timedelta(days=1)
    return tomorrow.strftime(date_format)


def fetch_pdf_resources(uri, rel):
    if uri.find(settings.MEDIA_URL) != -1:
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
    elif uri.find(settings.STATIC_URL) != -1:
        path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
    else:
        path = None
    return path


def generate_pdf(params: dict):
	template = get_template('reservation/pdf.html')
	html = template.render(params)

	file_name = yesterday_date()

	with open(str(settings.BASE_DIR) + f'/reports/{file_name}.pdf', 'wb+') as file:
		pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), file,
		                                                           encoding='utf-8',
		                                                           link_callback=fetch_pdf_resources)

	return file_name, True

