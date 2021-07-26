from datetime import datetime, timedelta


def yesterday_date(request):
    date_format = '%d.%m.%Y'
    today = datetime.now()
    tomorrow = today - timedelta(days=1)
    return {
            'tomorrow': tomorrow.strftime(date_format)
           }