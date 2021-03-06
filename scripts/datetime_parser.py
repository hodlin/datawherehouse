import re
from datetime import time, date, timedelta, datetime


def to_time(time_str=''):
    _time = []
    extracted = re.findall(r'..?', time_str[::-1])
    for i in range(3):
        try:
            _time.append(int(extracted[0][::-1]))
            del extracted[0]
        except ValueError:
            _time.append(0)
        except IndexError:
            _time.append(0)
    return time(*_time[::-1])


def to_timedelta(time_str=''):
    return timedelta(seconds=int(time_str))


def to_date(date_str=''):
    _date = []
    # print(str(date_str))
    year, month_day = re.findall(r'....?', str(date_str))
    month, day = re.findall(r'..?', month_day)
    return date(year=int(year), month=int(month), day=int(day))


def to_seconds(time_str=''):
    _time = to_time(time_str)
    _time = _time.hour * 3600 + _time.minute * 60 + _time.second
    return _time


def to_decimal_time(time_str=''):
    _time = to_time(time_str)
    _time = _time.hour + _time.minute / 60 + _time.second / 3600
    return _time


def to_datetime(date_str='', time_str='', date_dt=None, time_dt=None):
    if date_dt and time_dt:
        _date = date_dt
        _time = time_dt
    else:
        _date = to_date(date_str)
        _time = to_time(time_str)
    return datetime(year=_date.year, month=_date.month, day=_date.day,
                    hour=_time.hour, minute=_time.minute, second=_time.second)


if __name__ == '__main__':
    print(to_time(time_str='102'))
    print(to_date(date_str='20160101'))
    print(to_decimal_time(time_str='183000'))

