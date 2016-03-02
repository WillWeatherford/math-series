"""This module runs tests in pytest to check the funtions."""


import pytest

FIB_TABLE = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (11, 89),
    (12, 144),
    (20, 6765)
]


LUCAS_TABLE = [
    (0, 2),
    (1, 1),
    (2, 3),
    (3, 4),
    (4, 7),
    (5, 11),
    (6, 18),
]


SUM_TABLE = [
    (0, 0, 1, 0),
    (0, 2, 1, 2),
    (1, 2, 1, 1),
    (11, 0, 1, 89)
]


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fibonacci_iter(n, result):
    from series import fibonacci_iter
    assert fibonacci_iter(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas_iter(n, result):
    from series import lucas_iter
    assert lucas_iter(n) == result


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fibonacci_recur(n, result):
    from series import fibonacci_recur
    assert fibonacci_recur(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas_recur(n, result):
    from series import lucas_recur
    assert lucas_recur(n) == result


@pytest.mark.parametrize('n, x, y, result', SUM_TABLE)
def test_sum_series(n, x, y, result):
    from series import sum_series
    assert sum_series(n, x, y) == result
