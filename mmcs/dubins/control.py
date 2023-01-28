from numpy import where, sign, linspace, isclose, full, nan
from .special_functions import alphaCS, thetaCS, VCS, thetaCCm, thetaCCp, VCCm, VCCp
from .special_functions import DI, DII, DIII 


def minimum_time_control_to_point(x, y, n=100):
    if alphaCS(x, y) >= 0:
        tau = thetaCS(x, y) 
        t = linspace(0, VCS(x, y), n)
        s = -sign(x) if x != 0 else float(y < 0)
        return t, where(t <= tau, s, 0.0)
    else:
        tau = thetaCCm(x, y)
        t = linspace(0, VCCm(x, y), n)
        s = sign(x) if x != 0 else 1.0
        return t, where(t <= tau, s, -s)


def admissible_control_to_point(t, x, y, n=100):
    t = linspace(0, t, n)
    if (DI(x, y) or DIII(x, y)) and isclose(t[-1], VCCm(x, y)):
        tau = thetaCCm(x, y)
        s = sign(x) if x != 0 else 1.0
        return t, where(t <= tau, s, -s)
    elif (DII(x, y) or DIII(x, y)) and isclose(t[-1], VCS(x, y)):
        tau = thetaCS(x, y)
        s = -sign(x) if x != 0 else float(y < 0)
        return t, where(t <= tau, s, 0.0)
    elif DIII(x, y) and isclose(t[-1], VCCp(x, y)):
        tau = thetaCCp(x, y)
        s = sign(x) if x != 0 else 1.0
        return t, where(t <= tau, s, -s)
    else:
        # The case when (x, y) is inside the reachable set at time moment t
        # is not impemented. Thus, the function returns nan in this case.
        return t, full(n, nan)


minimum_time_control_to_point(1.0, 1.0)
admissible_control_to_point(1.0, 1.0, 1.0)