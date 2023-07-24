import numpy as np


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


def min_max(data: np.ndarray, axis: int) -> np.ndarray:
    """
    Perform min-max normalization on the data along the given axis.
    :param data: An array of data.
    :param axis: The axis to normalize.
    :return: A normalized array of data.
    """
    maxima = np.max(data, axis=axis, keepdims=True)
    minima = np.min(data, axis=axis, keepdims=True)
    return (data - minima) / (maxima - minima)
