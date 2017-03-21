import datetime

def convert_epoch_to_date(epoch):
    if not epoch:
        return None

    return datetime.datetime.fromtimestamp(long(epoch)/1000.0) if epoch else None
