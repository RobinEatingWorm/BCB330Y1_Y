import numpy as np
import src.array as array


def test_centered_trial_average_zero() -> None:
    """
    Test a 4D array containing 0 as its only element.
    """

    data = np.zeros((1, 1, 1, 1))
    result = array.centered_trial_average(data, 0, 1)
    expected = np.zeros((1, 1, 1))
    assert np.array_equal(result, expected)


def test_centered_trial_average_small() -> None:
    """
    Test a 2 x 2 x 2 x 2 array with randomly selected elements.
    """

    data = np.array([[[[6, 29], [28, 82]], [[75, 51], [81, 4]]],
                     [[[25, 5], [46, 69]], [[87, 22], [95, 23]]]])
    result = array.centered_trial_average(data, 2, 3)
    print(result)
    expected = np.array([[[-38.375, 19.875], [22.625, -8.125]],
                         [[-19.875, 1.375], [35.625, -13.125]]])
    assert np.array_equal(result, expected)
