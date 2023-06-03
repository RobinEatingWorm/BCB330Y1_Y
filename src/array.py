import numpy as np


def normalize(data: np.ndarray, axis: int) -> np.ndarray:
    """
    Return an array of z-scores along the specified axis.
    :param data: An array of neuron data over time.
    :param axis: The axis of time data in the array.
    :return: An array of z-scores for each neuron.
    """

    # Subtract the means and divide the difference by the standard deviation
    mean = np.mean(data, axis=axis, keepdims=True)
    std = np.std(data, axis=axis, ddof=1, keepdims=True)
    z_scores = (data - mean) / std

    # Replace all instances of np.nan with 0
    z_scores[np.isnan(z_scores)] = 0
    return z_scores


def centered_trial_average(data: np.ndarray, trial_axis: int, neuron_axis: int) -> np.ndarray:
    """
    Compute the average of all trials in the data and return the centered
    averages.
    :param data: An array of data collected from all trials.
    :param trial_axis: The axis of trial data in the array.
    :param neuron_axis: The axis of neuron data in the array.
    :return: An array of centered trial averages.
    """

    # Find the number of neurons
    neurons = data.shape[neuron_axis]

    # Average the data over trials
    trial_average = np.mean(data, trial_axis)
    if trial_axis < neuron_axis:
        neuron_axis -= 1

    # Transpose the neuron axis to the front and collapse the other axes
    order = [neuron_axis]
    order.extend([axis for axis in range(trial_average.ndim) if axis != neuron_axis])
    collapsed_trial_average = trial_average.transpose(order).reshape((neurons, -1))

    # Compute the shape of the mean of the trial averages
    shape = [1] * trial_average.ndim
    shape[neuron_axis] = neurons

    # Center the data
    return trial_average - np.mean(collapsed_trial_average, 1).reshape(shape)
