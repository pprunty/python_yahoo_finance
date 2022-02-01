from datetime import datetime, timedelta

import custom_logger

logger = custom_logger.init_logger()


def get_time_in_hr_mins():
    """
    A simple function which returns the time in hours and mins as an integer.
    ex. 15:46 or 3:46pm = 1546

    :return the time now.
        """
    now = datetime.now()
    return int(now.strftime('%H%M'))


def get_time_in_hr_mins():
    """
    A simple function which returns the time in hours and mins as an integer.
    ex. 15:46 or 3:46pm = 1546

    :return the time now.
        """
    now = datetime.now()
    return int(now.strftime('%H%M'))


def get_time_in_std_format():
    """
    A simple function which returns the time in standard format.
    ex. 2016-06-12 18:56:10

    :return the time now.
        """
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')


def get_open_time_in_std_format():
    """
    A simple function which returns the time in standard format.
    ex. 2016-06-12 18:56:10

    :return the time now.
        """
    now = datetime.now()

    return now.strftime('%Y-%m-%d 09:30:00')


def get_time_in_file_std_format(offset=0):
    """
    A simple function which returns the time in standard format for file timestamp
    formatting.
    ex. 2016_06_12 18:56:10

    :return the time now.
        """
    today = datetime.now()
    now = today - timedelta(days=offset)
    return now.strftime('%Y_%m_%d')
