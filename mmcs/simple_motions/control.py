from numpy import linspace, sqrt, arctan2, full, nan
from .params import tol


def minimum_time_control(x, y, n=100):
    r = sqrt(x**2 + y**2)
    t = linspace(0, r, n)
    return t, 0*t + 1, arctan2(y/r, x/r) + t*0


def admissible_control(t, x, y, n=100):
    r = sqrt(x**2 + y**2)
    t = linspace(0, t, n)
    if r < t[-1] + tol:
        return t, r/t[-1] + 0*t, arctan2(y/r, x/r) + 0*t
    else:
        return t, full(n, nan), full(n, nan)