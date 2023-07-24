import numpy as np

import re


def add_frames_to_datetime(time_start: np.datetime64, frames: int, fr: float) -> np.datetime64:
    """
    Return the time after adding the specified number of frames to the start
    time.
    :param time_start: A np.datetime64 containing the start time.
    :param frames: The number of frames to add.
    :param fr: The frame rate.
    :return: A np.datetime64 containing the time after adding the frames to
    the start time.
    """

    # Find the elapsed time (in microseconds) using the frames
    time_elapsed = np.timedelta64(np.int64(frames / fr * (10 ** 6)), 'us')

    # Add the elapsed time to the start time
    return time_start + time_elapsed


def datetime_to_frame(time_curr: np.datetime64, time_start: np.datetime64, frame_start: int, fr: float) -> np.float64:
    """
    Convert a time to a frame number using a starting time and starting frame as reference.
    :param time_curr: The time to convert to a frame number.
    :param time_start: The reference start time.
    :param frame_start: The frame number of the reference start time.
    :param fr: The frame rate.
    :return: A np.float64 containing the frame number (which may be a decimal).
    """

    # Find the elapsed time (in seconds) by comparing the two times
    time_elapsed = (time_curr - time_start) / np.timedelta64(1, 's')

    # Add the elapsed time to the reference frame
    return frame_start + time_elapsed * fr


def image_desc_to_datetime(image_desc: str) -> np.datetime64:
    """
    Extract time information from an image description of a TIFF file frame.
    :param image_desc: A string containing information on a frame of a TIFF
    file.
    :return: A np.datetime64 containing the time of the frame.
    """

    # Find the time of the first frame
    time_start_str = re.search(r'epoch = (?P<time_start>.*)\n', image_desc).group('time_start')
    time_start = timestamp_to_datetime(np.array(eval(time_start_str)))

    # Find the time elapsed between the first and current frames
    time_change_str = re.search(r'frameTimestamps_sec = (?P<time_change>.*)\n', image_desc).group('time_change')
    time_change = np.timedelta64(np.int64(eval(time_change_str) * (10 ** 6)), 'us')

    # Add the times together
    return time_start + time_change


def timestamp_to_datetime(timestamp: np.ndarray) -> np.datetime64:
    """
    Convert a timestamp into a np.datetime64 rounded to the nearest
    microsecond.
    :param timestamp: An array containing the year, month, day, hour,
    minute, and second in that order.
    :return: A np.datetime64 representation of the timestamp.
    """

    # Initialize an empty string
    time_str = ''

    # Initialize a hash map of symbols used in the string
    symbols = {0: '-', 1: '-', 2: 'T', 3: ':', 4: ':'}

    # Loop over each time unit
    for i in range(len(timestamp)):

        # Get the current time unit
        unit = timestamp[i]

        # Round to the nearest microsecond if the unit is second
        if i == 5:
            unit = np.round(unit, decimals=6)
        else:
            unit = np.int64(unit)

        # Convert the unit into a string
        unit_str = str(unit)

        # Append a zero to the front if the unit is less than 10
        if unit < 10:
            unit_str = '0' + unit_str

        # Add the unit followed by a corresponding symbol to the string
        time_str += unit_str
        if i in symbols:
            time_str += symbols[i]

    # Use the string in a np.datetime64
    return np.datetime64(time_str)
