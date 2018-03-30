from datetime import datetime

def fix_datetime(dt_str):
    """
    2018-03-30 07:38:23+00:00
    to
    2018-03-30 15:38:23
    """
    if not dt_str:
        return str(datetime.now().replace(microsecond=0))
    dt = datetime.strptime(dt_str[:-3] + dt_str[-2:], "%Y-%m-%d %H:%M:%S%z")
    return str(dt.astimezone().replace(tzinfo=None))
