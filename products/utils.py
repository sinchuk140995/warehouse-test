import pytz

from datetime import datetime, date, time, timedelta


def get_current_day_start():
    '''Returns the midnight of the current day.'''
    current_day_start = datetime.combine(date.today(), time())
    current_day_start = pytz.utc.localize(current_day_start)
    return current_day_start


def get_last_n_days_frame(days):
    """Returns the frame of days from some day in the past
    to the midnight of the current day

    Parameters:
    days (int): A number of days will be subtracted from the current day

    Returns:
    tuple: Two UTC datetime objects which represent the start and the end
           of the frame (the start is inclusive, the end is exclusive)

    """
    current_day_start = get_current_day_start()
    last_days_start = current_day_start - timedelta(days=days)
    return last_days_start, current_day_start


def get_prev_week_frame(week_offset):
    """Returns the frame of a week in the past

    Parameters:
    week_offset (int): A number of weeks will be skipped from the current day.
                       (e.g. 1 means the previous week,
                       2 - the week before the previous)

    Returns:
    tuple: Two UTC datetime objects which represent the start and the end
           of the week (the start is inclusive, the end is exclusive)

    """
    current_day_start = get_current_day_start()
    days_after_week = current_day_start.weekday() + 7 * (week_offset - 1)
    week_finish = current_day_start - timedelta(days=days_after_week)
    week_start = week_finish - timedelta(days=7)
    return week_start, week_finish
