import datetime
import logging

_logger = logging.getLogger(__name__)

DATE_PATTERNS = ["%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%d-%m-%Y", "%Y%m%d", ]


def get_date_from_format(date_str, date_patterns=None):
    date_patterns = date_patterns or DATE_PATTERNS
    for pattern in date_patterns:
        try:
            return datetime.datetime.strptime(date_str, pattern).date()
        except Exception as e:
            _logger.debug('%s', e)
    return None


def mining_date(date, silent=False):
    if isinstance(date, str):
        date = get_date_from_format(date)
        if date:
            return date
        else:
            if silent:
                return
            raise Exception(
                '"date" must be type of date, datetime or date '
                'compatible string')
    elif isinstance(date, datetime.datetime):
        return date.date()
    elif isinstance(date, datetime.date):
        return date
    else:
        if silent:
            return
        raise Exception(
            '"date" must be type of date, datetime or date '
            'compatible string')
