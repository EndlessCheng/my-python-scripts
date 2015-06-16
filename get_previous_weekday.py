from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_previous_weekday(dayname):
    today = datetime.today()
    today_weekday = today.weekday()
    day_no = weekdays.index(dayname)
    print day_no
    target_date = today - timedelta(7 - (day_no - today_weekday))
    return target_date


if __name__ == '__main__':
    print(get_previous_weekday('Monday'))
