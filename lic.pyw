import datetime
def isExpired():
    today=datetime.date.today()
    expiry=datetime.date(2019,8,31)
    if expiry>today:
        return False
    else:
        return True
