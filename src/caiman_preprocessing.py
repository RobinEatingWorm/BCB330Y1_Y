import caiman as cm
from caiman.base.movies import movie

import numpy as np


def copy_data(orig: str, src: str) -> None:
    """
    Copy TIFF data to another directory.
    :param orig: The path to the data's original location.
    :param src: The path to where the data should be copied.
    """

    # Load the data and then save it
    cm.load(orig).save(src)


def find_local_max(data: np.ndarray, threshold: int, radius: int) -> list:
    """
    Given an array of ordered data, use a heuristic to find possible local
    maxima.
    :param data: A 1-D array of ordered data.
    :param threshold: The threshold which all local maxima should be above.
    :param radius: The number of points to check around potential local maxima.
    :return: A list containing the indices to local maxima.
    """

    # Initialize an empty list to store indices to local maxima
    local_max = []

    # Loop over each point in the data
    for i in range(len(data)):

        # Check if the point is no less than the threshold
        if data[i] < threshold:
            continue
        crit = True

        # Make sure the point is no less than all other points in the radius
        for j in range(-radius, radius + 1):
            if data[i] < data[i + j]:
                crit = False
                break

        # If the two conditions are met, the point is potentially a local maximum
        if crit:
            local_max.append(i)

    # Return all indices found
    return local_max


def replace_rows(data: movie, data_proxy: np.ndarray, index: int, channel_threshold: int,
                 correction_threshold: int, correction_radius: int) -> None:
    """
    Replace affected rows around the given index in the image data.
    :param data: The original calcium imaging data.
    :param data_proxy: An edited version of the original data used for determining which
    rows to replace.
    :param index: An index to a frame in the data.
    :param channel_threshold: The threshold for determining whether the frame
    displays the correct color channel for correction.
    :param correction_threshold: The threshold for determining whether a row is
    affected.
    :param correction_radius: The number of frames to correct around the given frame.
    """

    # Get the range of frames to potentially correct
    lb, ub = index - correction_radius, index + correction_radius + 1

    # Store the most recent pixel rows that are correct
    last_known_good_config = data[lb]

    # Iterate through frames from oldest to newest
    for i in range(lb, ub):

        # Check if the frame is the correct color channel
        if not np.nanmean(data_proxy[i], axis=(0, 1)) > channel_threshold:
            continue

        # Calculate the mean fluorescence of each row in the frame
        frame_row_means = np.nanmean(data_proxy[i], axis=1)

        # For each row, replace or save it depending on the correction threshold
        for j in range(frame_row_means.size):
            if frame_row_means[j] > correction_threshold:
                data[i, j] = last_known_good_config[j]
            else:
                last_known_good_config[j] = data[i, j]
