from numba import vectorize
from numpy import nan

from .special_functions import alphaCS, VCS, VCCm
from .reachability import distance_to_planar_reachable_set


@vectorize
def minimum_time_to_point(x, y):
    return VCS(x, y) if alphaCS(x, y) >= 0 else VCCm(x, y)


@vectorize
def tau(t, x, y, r, v):
    d = distance_to_planar_reachable_set(t, x, y)
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

minimum_time_to_point(1.0, 1.0)
tau(1.0, 1.0, 1.0, 1.0, 1.0)