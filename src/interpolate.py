import numpy as np
from scipy.interpolate import interp1d

from src.datetime import datetime_to_frame


def interpolate(data: np.ndarray, interval_n: int, time_start: np.datetime64, time_end: np.datetime64,
                frame_start: int, frame_end: int, image_fr: float) -> np.ndarray:
    """
    Perform linear interpolation on part of the data.
    :param data: The entire array of data.
    :param interval_n: The number of frames to interpolate in the interval.
    :param time_start: A np.datetime64 containing the time of the first frame.
    :param time_end: A np.datetime64 containing the time of the last frame.
    :param frame_start: The index of the first frame in the interval.
    :param frame_end: The index of the last frame in the interval.
    :param image_fr: The frame rate of imaging.
    :return: An array containing interpolated data for the specified interval.
    """

    # Calculate the unit of time to use as a step size
    time_unit = (time_end - time_start) / (interval_n - 1)

    # Generate evenly spaced times
    times_interpol = np.arange(time_start, time_end, time_unit)

    # Handle the edge case where the last time to be interpolated evaluates to the end time
    if times_interpol.size < interval_n:
        times_interpol = np.append(times_interpol, time_end)

    # Convert the times into frames
    frames_interpol = datetime_to_frame(times_interpol, time_start, frame_start, image_fr)

    # Create a function to interpolate the time series
    x = np.arange(frame_start, frame_end + 1)
    y = data[:, x]
    f = interp1d(x, y, axis=1)

    # Return the interpolated values
    return f(frames_interpol)


def stitch(data: np.ndarray, time_elapsed: list[int, int], frame_start: int,
           frame_end: int, image_fr: float) -> tuple[np.ndarray, np.ndarray]:
    """
    Concatenate frames from the beginning and end of a certain interval. The
    frames at the end of the interval are translated such that the last frame
    from the beginning has the same value as the first frame at the end.
    :param data: The entire array of data.
    :param time_elapsed: A list of two integers. The first one is the number of
        seconds to keep after the start of the interval, and the second is the
        number of seconds to keep before the end of the interval.
    :param frame_start: The index of the first frame in the interval.
    :param frame_end: The index of the last frame in the interval.
    :param image_fr: The frame rate of imaging.
    :return: A tuple containing an array of frames from the beginning and end
        of the interval joined together and an array of distances used for
        translation, respectively.
    """

    # Calculate the number of frames needed from the beginning and end of the interval
    n_frames_from_start = round(time_elapsed[0] * image_fr)
    n_frames_to_end = round(time_elapsed[0] * image_fr)

    # Calculate the distance to translate frames near the end
    distance = data[:, frame_start + n_frames_from_start - 1] - data[:, frame_end - n_frames_to_end + 1]
    distance = np.expand_dims(distance, axis=1)

    # Get frames from the start and translate frames from the end
    interval_start = data[:, frame_start:frame_start + n_frames_from_start]
    interval_end = data[:, frame_end - n_frames_to_end + 1:frame_end + 1] + distance

    # Concatenate frames from the beginning and end of the interval
    return np.concatenate((interval_start, interval_end), axis=1), distance


def truncate(data: np.ndarray, interval_n: int, frame_start: int) -> np.ndarray:
    """
    Truncate data to the specified number of frames after the starting frame.
    :param data: The entire array of data.
    :param interval_n: The number of frames to keep in the interval.
    :param frame_start: The index of the first frame in the interval.
    :return: An array containing truncated data.
    """

    # Truncate the data to the specified number of frames
    return data[:, frame_start:frame_start + interval_n]
