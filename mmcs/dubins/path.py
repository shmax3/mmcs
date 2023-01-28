from numpy import pi, where, sign, linspace, sin, cos, isclose, full, nan
from .special_functions import alphaCS, thetaCS, thetaCCm, thetaCCp, VCS, VCCm, VCCp
from .special_functions import xCSm, yCS, xCCp, yCC, DI, DII, DIII


def markov_path(x, y, n=100):
    if alphaCS(x, y) >= 0:
        tau = thetaCS(x, y)
        t = linspace(0, VCS(x, y), n)
        s = -sign(x) if x != 0 else float(y < 0)
        return (t, s*where(t < tau, cos(t) - 1, xCSm(tau, t)),
                where(t < tau, sin(t),  yCS(tau, t)),
                where(t < tau, pi/2 + s*t, pi/2 + s*tau))
    else:
        tau = thetaCCm(x, y)
        t = linspace(0, VCCm(x, y), n)
        s = sign(x) if x != 0 else 1.0
        return (t, s*where(t < tau, cos(t) - 1,  xCCp(tau, t)),
                where(t < tau, sin(t),  yCC(tau, t)),
                where(t < tau, pi/2 + s*t, pi/2 + 2*s*tau - s*t))


def admissible_path_to_point(t, x, y, n=100):
    t = linspace(0, t, n)
    if (DI(x, y) or DIII(x, y)) and isclose(t[-1], VCCm(x, y)):
        tau = thetaCCm(x, y)
        s = sign(x) if x != 0 else 1.0
        return (t, s*where(t < tau, cos(t) - 1,  xCCp(tau, t)),
                where(t < tau, sin(t),  yCC(tau, t)),
                where(t < tau, pi/2 + s*t, pi/2 + 2*s*tau - s*t))
    elif (DII(x, y) or DIII(x, y)) and isclose(t[-1], VCS(x, y)):
        tau = thetaCS(x, y)
        s = -sign(x) if x != 0 else float(y < 0)
        return (t, s*where(t < tau, cos(t) - 1, xCSm(tau, t)),
                where(t < tau, sin(t),  yCS(tau, t)),
                where(t < tau, pi/2 + s*t, pi/2 + s*tau))
    elif DIII(x, y) and isclose(t[-1], VCCp(x, y)):
        tau = thetaCCp(x, y)
        s = sign(x) if x != 0 else 1.0
        return (t, s*where(t < tau, cos(t) - 1,  xCCp(tau, t)),
                where(t < tau, sin(t),  yCC(tau, t)),
                where(t < tau, pi/2 + s*t, pi/2 + 2*s*tau - s*t))
    else:
        # The case when (x, y) is inside the reachable set at time moment t
        # is not impemented. Thus, the function returns nan in this case.
        return t, full(n, nan), full(n, nan), full(n, nan)


markov_path(0.0, 1.0)
admissible_path_to_point(1.0, 1.0, 1.0)