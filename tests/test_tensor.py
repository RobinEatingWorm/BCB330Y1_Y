import numpy as np

from src.tensor import centered_trial_average


def test_centered_trial_average_zero() -> None:
    """
    Test a 4D array containing 0 as its only element.
    """

    data = np.zeros((1, 1, 1, 1))
    result = centered_trial_average(data, 0, 1)
    expected = np.zeros((1, 1, 1))
    assert np.array_equal(result, expected)


def test_centered_trial_average_small() -> None:
    """
    Test a 2 x 2 x 2 x 2 array with randomly selected elements.
    """

    data = np.array([[[[6, 29], [28, 82]], [[75, 51], [81, 4]]],
                     [[[25, 5], [46, 69]], [[87, 22], [95, 23]]]])
    result = centered_trial_average(data, 2, 3)
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
    S = centered_trial_average(trialR, 0, 1)
    assert np.array_equal(R, S)
