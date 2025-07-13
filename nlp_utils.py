from dateparser.search import search_dates
from datetime import datetime

def extract_datetime(text):
    results = search_dates(text, settings={
        'PREFER_DATES_FROM': 'future',
        'RELATIVE_BASE': datetime.now(),
        'RETURN_AS_TIMEZONE_AWARE': False,
        'TIMEZONE': 'UTC',
        'PARSERS': ['absolute-time', 'relative-time', 'timestamp', 'custom-formats']
    })
    return [r[1] for r in results] if results else []


