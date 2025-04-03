import datetime
from dateutil import parser

# TODO: create a new adaptable class for datetime that can be used to
# interface to the db

TIME_ZERO = parser.parse("2001-01-01 00:00:00")


def time_float_to_datetime(swin_time_float):
    return TIME_ZERO + datetime.timedelta(seconds=swin_time_float)


def datetime_string_to_time_float(swin_time_string):
    parsed_date = parser.parse(swin_time_string)
    delta = parsed_date - TIME_ZERO
    return delta.total_seconds()


def calculate_zero_time(swin_time_string, swin_time_float):
    parsed_date = parser.parse(swin_time_string)
    print(parsed_date)
    delta = datetime.timedelta(seconds=swin_time_float)
    print(parsed_date - delta)
