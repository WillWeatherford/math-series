"""This module defines functions that implement mathematical series.

fibonacci_iter(n):
    Return the nth value in the fibonacci series by iteration.

    >>> fibonacci_iter(2)
    1

lucas_iter(n)
    Return the nth value in the lucas series by iteration.
    
    >>>lucas_iter(2)
    3

fibonacci_recur(n):
    Return the nth value in the fibonacci series by recursion.

    >>> fibonacci_recur(2)
    1

lucas_recur(n)
    Return the nth value in the lucas series by recursion.
    
    >>>lucas_recur(2)
    3
"""


def fibonacci_iter(n):
    """Return the nth value in the fibonacci series by iteration."""
    f = []
    for x in range(n + 1):
        if x == 0:
            f.append(x)
        elif x == 1:
            f.append(x)
        else:
            f.append(f[-1] + f[-2])
    return f[-1]


def lucas_iter(n):
    """Return the nth value in the lucas series by iteration."""
    f = []
    for x in range(n + 1):
        if x == 0:
            f.append(2)
        elif x == 1:
            f.append(1)
        else:
            f.append(f[-1] + f[-2])
    return f[-1]


def fibonacci_recur(n):
    """Return the nth value in the fibonacci series by recursion."""
    if n == 0 or n == 1:
        return n
    return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)


def lucas_recur(n):
    """Return the nth value of lucas series by recursion."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas_recur(n - 1) + lucas_recur(n - 2)


def sum_series(n, x=0, y=1):
    """Return the nth of a summative series by recursion."""
    if n == 0:
        return x
    elif n == 1:
        return y
    return sum_series(n - 1) + sum_series(n - 2)


if __name__ == '__main__':
    print(__doc__)
