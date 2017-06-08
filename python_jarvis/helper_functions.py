import datetime, re

def convert_epoch_to_date(epoch):
    if not isinstance(epoch, long):
        return None

    return datetime.datetime.fromtimestamp(long(epoch)/1000.0)


def convert_date_to_epoch(date):
    if not isinstance(date, datetime.datetime):
        return None

    return long(date.strftime('%s'))*1000


def _validate_email(email):
    address_to_verify =email
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', address_to_verify)

    if match:
        return True
    else:
        return False
