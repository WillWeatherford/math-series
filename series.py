""" This module defines functions that implement mathematical series."""


def fibonacci_iter(n):
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
    if n == 0 or n == 1:
        return n
    return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)


def lucas_recur(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas_recur(n - 1) + lucas_recur(n - 2)
