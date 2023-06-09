import numpy as np
from src import array


def test_normalize_vector() -> None:
    """
    Test a vector with 5 elements.
    """
    data = np.array([5, 2, -6, 2, -7])
    result = array.normalize(data, 0)
    expected = (data + 0.8) / np.sqrt(28.7)
    assert np.array_equal(result, expected)


def test_normalize_matrix() -> None:
    """
    Test a 2 x 2 matrix.
    """
    data = np.array([[-2, 5], [2, 21]])
    result = array.normalize(data, 0)
    expected = np.array([[-2 / np.sqrt(8), -8 / np.sqrt(128)],
                         [2 / np.sqrt(8), 8 / np.sqrt(128)]]).astype(np.float64)
    assert np.allclose(result, expected)


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


def test_centered_trial_average_demo() -> None:
    """
    Test the surrogate data from the code demo.
    See https://github.com/machenslab/dPCA/blob/master/python/dPCA_demo.ipynb
    """

    # Code from the demo
    N, T, S = 100, 250, 6
    noise, n_samples = 0.2, 10
    zt = (np.arange(T) / float(T))
    zs = (np.arange(S) / float(S))
    trialR = noise * np.random.randn(n_samples, N, S, T)
    trialR += np.random.randn(N)[None, :, None, None] * zt[None, None, None, :]
    trialR += np.random.randn(N)[None, :, None, None] * zs[None, None, :, None]
    R = np.mean(trialR, 0)
    R -= np.mean(R.reshape((N, -1)), 1)[:, None, None]

    # Run the test
    S = array.centered_trial_average(trialR, 0, 1)
    assert np.array_equal(R, S)
