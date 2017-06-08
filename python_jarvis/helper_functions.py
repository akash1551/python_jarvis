import datetime, re

def convert_epoch_to_date(epoch):
    if not isinstance(epoch, long):
        return None

    return datetime.datetime.fromtimestamp(long(epoch)/1000.0) if epoch else None


def _validate_email(email):
    address_to_verify =email
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', address_to_verify)

    if match:
        return True
    else:
        return False
