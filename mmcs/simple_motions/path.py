from numpy import sqrt, linspace, nan, full
from .params import tol


def minimum_time_path(x, y, n=100):
    r = sqrt(x**2 + y**2)
    t = linspace(0, r, n)
    return t, x*t/r, y*t/r

def admissible_path(t, x, y, n=100):
    r = sqrt(x**2 + y**2)
    t = linspace(0, t, n)
    if r < t[-1] + tol:
        return t, x*t/t[-1], y*t/t[-1]
    else:
        return t, full(n, nan), full(n, nan)