from numba import vectorize
from numpy import arccos, pi, sqrt, sin, cos, arctan
from .params import tol


@vectorize
def alphaCS(x, y):
    return (1 - abs(x))**2 + y**2 - 1


@vectorize
def alphaCC(x, y):
    return (5 - (1 + abs(x))**2 - y**2) / 4 


@vectorize
def thetaCS(x, y):
    if y >= (1 - abs(x))*sqrt(alphaCS(x, y)) - tol:
        return arccos((1 - abs(x) + y*sqrt(alphaCS(x, y))) / (1 + alphaCS(x, y)))
    else:
        return 2*pi - arccos((1 - abs(x) + y*sqrt(alphaCS(x, y))) / (1 + alphaCS(x, y)))


@vectorize
def thetaCCm(x, y):
    return arccos(((1 + abs(x))*(2 - alphaCC(x, y)) - y*sqrt(1 - alphaCC(x, y)**2))
                  /((1 + abs(x))**2 + y**2))


@vectorize
def thetaCCp(x, y):
    return arccos(((1 + abs(x))*(2 - alphaCC(x, y)) + y*sqrt(1 - alphaCC(x, y)**2))
                  /((1 + abs(x))**2 + y**2))


@vectorize
def VCS(x, y):
    return thetaCS(x, y) + sqrt(alphaCS(x, y))


@vectorize
def VCCm(x, y):
    return thetaCCm(x, y) + 2*pi - arccos(alphaCC(x, y))


@vectorize
def VCCp(x, y):
    return thetaCCp(x, y) + arccos(alphaCC(x, y))


@vectorize
def xCSm(tau, t):
    return -(t - tau)*sin(tau) + cos(tau) - 1


@vectorize
def xCSp(tau, t):
    return (t - tau)*sin(tau) - cos(tau) + 1


@vectorize
def yCS(tau, t):
    return (t - tau)*cos(tau) + sin(tau)


@vectorize
def xCCm(tau, t):
    return -2*cos(tau) + cos(t - 2*tau) + 1


@vectorize
def xCCp(tau, t):
    return 2*cos(tau) - cos(t - 2*tau) - 1


@vectorize
def yCC(tau, t):
    return 2*sin(tau) + sin(t - 2*tau)


@vectorize
def rhoCC(x, y, tau, t):
    return sqrt((abs(x) - xCCp(tau, t))**2 + (y - yCC(tau, t))**2)


@vectorize
def tauCC(t, ksi):
    return (t/3 - 2*arctan(ksi)) % (2*pi)


@vectorize
def DI(x, y):
    return alphaCS(x, y) < 0 or x == 0 and y == 0


@vectorize
def DII(x, y):
    return alphaCS(x, y) >= 0 and (alphaCC(x, y) <= -1 or y <= 0) and (x != 0 or y != 0)


@vectorize
def DIII(x, y):
    return alphaCC(x, y) > -1 and y > 0 and alphaCS(x, y) >= 0 and (x != 0 or y != 0)