import datetime, re
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives


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


def send_email(email, title, message):
    if customer.user.email:
        send_mail(
            title, # Subject
            message, # Message
            '', # From email  # no need to specify. automatically used from settings.py
            [customer.user.email], # recipient_list
            fail_silently=False, # If set False, will raise Exception
        )

    return True

