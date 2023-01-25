from numba import vectorize
from numpy import pi, linspace, sin, cos, sqrt, isclose
from .params import tol


@vectorize
def reachable_set(t, x, y):
    r = sqrt(x**2 + y**2)
    return r < t + tol


def reachable_set_boundary(t, n=100):
    phi = linspace(0, 2*pi, n)
    return t*cos(phi), t*sin(phi)


@vectorize
def distance_to_reachable_set(t, x, y):
    r = sqrt(x**2 + y**2)
    if r < t + tol:
        return 0.0
    else:
        return r - t


def nearest_point_to_reachable_set(t, x, y):
    return nx(t, x, y), ny(t, x, y)


@vectorize
def nx(t, x, y):
    r = sqrt(x**2 + y**2)
    if r <= t:
        return x
    else:
        return x*t/r


@vectorize
def ny(t, x, y):
    r = sqrt(x**2 + y**2)
    if r <= t:
        return y
    else:
        return y*t/r


reachable_set(1.0, 1.0, 1.0)
distance_to_reachable_set(1.0, 1.0, 1.0)
nearest_point_to_reachable_set(1.0, 1.0, 1.0)