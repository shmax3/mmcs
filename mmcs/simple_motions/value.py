from numba import vectorize, njit
from numpy import nan, sqrt
from .reachability import distance_to_reachable_set


@vectorize
def minimum_time(x, y):
    return sqrt(x**2 + y**2)


@njit
def tau(t, x, y, r, v):
    d = distance_to_reachable_set(t, x, y)
    if d > r:
        return t + (d - r)/(1 + v)
    else:
        return t


def interception_minimum_time(xt, yt, r, v, n=nan):
    t = 0.0
    t_prev = nan
    i = 0
    while t_prev != t and not i >= n:
        t_prev = t
        t = tau(t, xt(t), yt(t), r, v) 
        i += 1
    return t


minimum_time(1.0, 1.0)
tau(1.0, 1.0, 1.0, 1.0, 1.0)