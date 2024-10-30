from datetime import datetime

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def convert_str_to_datetime(datetime_str: str) -> datetime:
    return datetime.strptime(datetime_str, DATE_FORMAT)
