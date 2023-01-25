from numba import vectorize
from numpy import pi, arccos, linspace, array, sin, cos, sqrt, cbrt, sign
from scipy.optimize import brenth

from .special_functions import VCS, VCCm, VCCp, thetaCS
from .special_functions import xCSm, xCSp, yCS, xCCp, yCC
from .special_functions import tauCC, rhoCC, DI, DII, DIII


@vectorize
def planar_reachable_set(t, x, y):
    if t == 0 and x == 0 and y == 0:
        return True
    else:
        if DI(x, y): 
            return t >= VCCm(x, y)
        else: 
            if t >= VCS(x, y):
                if DII(x, y):
                    return True
                else:
                    return t >= VCCm(x, y) or VCCp(x, y) >= t
            else:
                return False


def planar_reachable_set_boundary(t, n=100, m=100):
    if t <= 3*pi/2 + 1:
        tau1 = linspace(0, t, n)
        tau2 = array([])
    elif t <= 2*pi:
        tau1_max = brenth(lambda tau: xCSm(tau, t), pi, 3*pi/2)
        tau2_min = brenth(lambda tau: xCSm(tau, t), 3*pi/2, t)
        tau1 = linspace(0, tau1_max, int(n*tau1_max/(t - tau2_min + tau1_max)))
        tau2 = linspace(tau2_min, t, int(n*(t - tau2_min)/(t - tau2_min + tau1_max)))
    else:
        tau1_max = brenth(lambda tau: xCSm(tau, t), pi, 3*pi/2)
        tau1 = linspace(0, tau1_max, n)
        tau2 = array([])
    if t >= 2*pi + arccos(23/27):
        tau = array([])
    else:
        if t <= 2*pi:
            tau_min = 0
        else:
            tau_min = brenth(lambda tau: xCCp(tau, t), t - 2*pi, max(0, (t - pi)/3))
        tau_max = brenth(lambda tau: xCCp(tau, t), max(0, (t - pi)/3), min(t, (t + pi)/3))
        tau = linspace(tau_min, tau_max, m)
    pieces = [(xCSp(tau1, t), yCS(tau1, t)), (xCSp(tau2, t), yCS(tau2, t)),
              (xCCp(tau, t), yCC(tau, t))]
    return pieces + [(-x, y) for x, y in reversed(pieces)]


@vectorize
def distance_to_planar_reachable_set(t, x, y):
    if planar_reachable_set(t, x, y):
        return 0.0
    elif (DII(x, y) or (DIII(x, y) and VCS(x, y) >= t)) and thetaCS(x, y) <= t:
        return VCS(x, y) - t
    else:
        a = -(y + sin(t/3))
        b = 3*(1 + abs(x)) + cos(t/3)
        c = 3*y - sin(t/3)
        d = -(1 + abs(x)) + cos(t/3)
        r = rhoCC(x, y, 0., t) 
        Tau = t if t < pi/2 else pi/2
        if a == 0 and b == 0:
            tau = tauCC(t, -d/c)
            if tau <= Tau:
                return min(r, rhoCC(x, y, tau, t))
        elif a == 0:          
            D = c**2 - 4*b*d
            if D > 0:
                tau1 = tauCC(t, (-c + sqrt(D))/(2*b))
                tau2 = tauCC(t, (-c - sqrt(D))/(2*b))
                if tau1 <= Tau:
                    if tau2 <= Tau:
                        return min(r, rhoCC(x, y, tau1, t), rhoCC(x, y, tau2, t))
                    else:
                        return min(r, rhoCC(x, y, tau1, t))
                else:
                    if tau2 <= Tau:
                        return min(r, rhoCC(x, y, tau2, t))
            elif D == 0:
                if tauCC(t, -c/(2*b)) <= Tau:
                    return min(r, rhoCC(x, y, tauCC(t, -c/(2*b)), t))
        else:
            f = c/a - (b/a)**2/3 
            g = (2*(b/a)**3 - 9*b*c/a**2)/27 + d/a
            h = g**2/4 + f**3/27
            if f == 0 and g == 0 and h == 0:
                tau = tauCC(t, -cbrt(d/a))
                if tau <= Tau:
                    return min(r, rhoCC(x, y, tau, t))
            elif h <= 0:
                i = sqrt(g**2/4 - h)
                j = cbrt(i)
                k = arccos(-g/(2*i))
                tau1 = tauCC(t, 2*j*cos(k/3) - b/(3*a))
                tau2 = tauCC(t, -j*(cos(k/3) + sqrt(3)*sin(k/3)) - b/(3*a))
                tau3 = tauCC(t, -j*(cos(k/3) - sqrt(3)*sin(k/3)) - b/(3*a))
                if tau1 <= Tau:
                    if tau2 <= Tau:
                        if tau3 <= Tau:
                            return min(r, rhoCC(x, y, tau1, t), rhoCC(x, y, tau2, t), rhoCC(x, y, tau3, t))
                        else:
                            return min(r, rhoCC(x, y, tau1, t), rhoCC(x, y, tau2, t))
                    else:
                        if tau3 <= Tau:
                            return min(r, rhoCC(x, y, tau1, t), rhoCC(x, y, tau3, t))
                        else:
                            return min(r, rhoCC(x, y, tau1, t))
                else:
                    if tau2 <= Tau:
                        if tau3 <= Tau:
                            return min(r, rhoCC(x, y, tau2, t), rhoCC(x, y, tau3, t))
                        else:
                            return min(r, rhoCC(x, y, tau2, t))
                    else:
                        if tau3 <= Tau:
                            return min(r, rhoCC(x, y, tau3, t))
            else:
                tau = tauCC(t, cbrt(-g/2 + sqrt(h)) + cbrt(-g/2 - sqrt(h)) - b/(3*a))
                if tau <= Tau:
                    return min(r, rhoCC(x, y, tau, t))
        return r


def nearest_point_to_planar_reachable_set(t, x, y):
    return nx(t, x, y), ny(t, x, y)


@vectorize
def nx(t, x, y):
    if planar_reachable_set(t, x, y):
        return x
    elif (DII(x, y) or (DIII(x, y) and VCS(x, y) >= t)) and thetaCS(x, y) <= t:
        if x == 0 and y < 0:
            s = 1.0
        else:
            s = -sign(x)
        return s*xCSm(thetaCS(x, y), t)
    else:
        a = -(y + sin(t/3))
        b = 3*(1 + abs(x)) + cos(t/3)
        c = 3*y - sin(t/3)
        d = -(1 + abs(x)) + cos(t/3)
        r = rhoCC(x, y, 0., t) 
        if a == 0 and b == 0:
            tau = tauCC(t, -d/c)
            if tau > min(pi/2, t) or r <= rhoCC(x, y, tau, t):
                tau = 0.0
        elif a == 0:          
            D = c**2 - 4*b*d
            if D > 0:
                tau1 = tauCC(t, (-c + sqrt(D))/(2*b))
                tau2 = tauCC(t, (-c - sqrt(D))/(2*b))
                if tau1 > min(pi/2, t):
                    if tau2 > min(pi/2, t) or r <= rhoCC(x, y, tau2, t):
                        tau = 0.0
                    else:
                        tau = tau2
                elif tau2 > min(pi/2, t):
                    if r <= rhoCC(x, y, tau1, t):
                        tau = 0.0
                    else:
                        tau = tau1
                else:
                    min_ = min(rhoCC(x, y, tau1, t), rhoCC(x, y, tau2, t))
                    if r <= min_:
                        tau = 0.0
                    elif rhoCC(x, y, tau1, t) <= min_:
                        tau = tau1
                    else:
                        tau = tau2
            elif D == 0:
                tau = tauCC(t, -c/(2*b))
                if tau > min(pi/2, t) or r <= rhoCC(x, y, tau, t):
                    tau = 0.0
        else:
            f = c/a - (b/a)**2/3 
            g = (2*(b/a)**3 - 9*b*c/a**2)/27 + d/a
            h = g**2/4 + f**3/27
            if f == 0 and g == 0 and h == 0:
                tau = tauCC(t, -cbrt(d/a))
                if r <= rhoCC(x, y, tau, t):
                    tau = 0.0
            elif h <= 0:
                i = sqrt(g**2/4 - h)
                j = cbrt(i)
                k = arccos(-g/(2*i))
                tau1 = tauCC(t, 2*j*cos(k/3) - b/(3*a))
                tau2 = tauCC(t, -j*(cos(k/3) + sqrt(3)*sin(k/3)) - b/(3*a))
                tau3 = tauCC(t, -j*(cos(k/3) - sqrt(3)*sin(k/3)) - b/(3*a))
                if tau1 > min(pi/2, t):
                    if tau2 > min(pi/2, t):
                        if tau3 > min(pi/2, t) or r <= rhoCC(x, y, tau3, t):
                            tau = 0.0
                        else:
                            tau = tau3
                    elif tau3 > min(pi/2, t):
                        if r <= rhoCC(x, y, tau2, t):
                            tau = 0.0
                        else:
                            tau = tau2
                    else:
                        min_ = min(rhoCC(x, y, tau2, t), rhoCC(x, y, tau3, t))
                        if r <= min_:
                            tau = 0.0
                        elif rhoCC(x, y, tau2, t) <= min_:
                            tau = tau2
                        else:
                            tau = tau3
                elif tau2 > min(pi/2, t):
                    if tau3 > min(pi/2, t) or r <= rhoCC(x, y, tau3, t):
                        tau = 0.0
                    else:
                        tau = tau3
                else:
                    min_ = min(rhoCC(x, y, tau1, t), rhoCC(x, y, tau2, t), rhoCC(x, y, tau3, t))
                    if r <= min_:
                        tau = 0.0
                    elif rhoCC(x, y, tau1, t) <= min_:
                        tau = tau1
                    elif rhoCC(x, y, tau2, t) <= min_:
                        tau = tau2
                    else:
                        tau = tau3
            else:
                tau = tauCC(t, cbrt(-g/2 + sqrt(h)) + cbrt(-g/2 - sqrt(h)) - b/(3*a))
                if tau > min(pi/2, t) or r <= rhoCC(x, y, tau, t):
                    tau = 0.0
        s = sign(x) if x != 0 else 1.0
        return s*xCCp(tau, t)


@vectorize
def ny(t, x, y):
    if planar_reachable_set(t, x, y):
        return y
    elif (DII(x, y) or (DIII(x, y) and VCS(x, y) >= t)) and thetaCS(x, y) <= t:
        return yCS(thetaCS(x, y), t)
    else:
        a = -(y + sin(t/3))
        b = 3*(1 + abs(x)) + cos(t/3)
        c = 3*y - sin(t/3)
        d = -(1 + abs(x)) + cos(t/3)
        r = rhoCC(x, y, 0., t) 
        if a == 0 and b == 0:
            tau = tauCC(t, -d/c)
            if tau > min(pi/2, t) or r <= rhoCC(x, y, tau, t):
                tau = 0.0
        elif a == 0:          
            D = c**2 - 4*b*d
            if D > 0:
                tau1 = tauCC(t, (-c + sqrt(D))/(2*b))
                tau2 = tauCC(t, (-c - sqrt(D))/(2*b))
                if tau1 > min(pi/2, t):
                    if tau2 > min(pi/2, t) or r <= rhoCC(x, y, tau2, t):
                        tau = 0.0
                    else:
                        tau = tau2
                elif tau2 > min(pi/2, t):
                    if r <= rhoCC(x, y, tau1, t):
                        tau = 0.0
                    else:
                        tau = tau1
                else:
                    min_ = min(rhoCC(x, y, tau1, t), rhoCC(x, y, tau2, t))
                    if r <= min_:
                        tau = 0.0
                    elif rhoCC(x, y, tau1, t) <= min_:
                        tau = tau1
                    else:
                        tau = tau2
            elif D == 0:
                tau = tauCC(t, -c/(2*b))
                if tau > min(pi/2, t) or r <= rhoCC(x, y, tau, t):
                    tau = 0.0
        else:
            f = c/a - (b/a)**2/3 
            g = (2*(b/a)**3 - 9*b*c/a**2)/27 + d/a
            h = g**2/4 + f**3/27
            if f == 0 and g == 0 and h == 0:
                tau = tauCC(t, -cbrt(d/a))
                if r <= rhoCC(x, y, tau, t):
                    tau = 0.0
            elif h <= 0:
                i = sqrt(g**2/4 - h)
                j = cbrt(i)
                k = arccos(-g/(2*i))
                tau1 = tauCC(t, 2*j*cos(k/3) - b/(3*a))
                tau2 = tauCC(t, -j*(cos(k/3) + sqrt(3)*sin(k/3)) - b/(3*a))
                tau3 = tauCC(t, -j*(cos(k/3) - sqrt(3)*sin(k/3)) - b/(3*a))
                if tau1 > min(pi/2, t):
                    if tau2 > min(pi/2, t):
                        if tau3 > min(pi/2, t) or r <= rhoCC(x, y, tau3, t):
                            tau = 0.0
                        else:
                            tau = tau3
                    elif tau3 > min(pi/2, t):
                        if r <= rhoCC(x, y, tau2, t):
                            tau = 0.0
                        else:
                            tau = tau2
                    else:
                        min_ = min(rhoCC(x, y, tau2, t), rhoCC(x, y, tau3, t))
                        if r <= min_:
                            tau = 0.0
                        elif rhoCC(x, y, tau2, t) <= min_:
                            tau = tau2
                        else:
                            tau = tau3
                elif tau2 > min(pi/2, t):
                    if tau3 > min(pi/2, t) or r <= rhoCC(x, y, tau3, t):
                        tau = 0.0
                    else:
                        tau = tau3
                else:
                    min_ = min(rhoCC(x, y, tau1, t), rhoCC(x, y, tau2, t), rhoCC(x, y, tau3, t))
                    if r <= min_:
                        tau = 0.0
                    elif rhoCC(x, y, tau1, t) <= min_:
                        tau = tau1
                    elif rhoCC(x, y, tau2, t) <= min_:
                        tau = tau2
                    else:
                        tau = tau3
            else:
                tau = tauCC(t, cbrt(-g/2 + sqrt(h)) + cbrt(-g/2 - sqrt(h)) - b/(3*a))
                if tau > min(pi/2, t) or r <= rhoCC(x, y, tau, t):
                    tau = 0.0
        return yCC(tau, t)


planar_reachable_set(1.0, 1.0, 1.0)
planar_reachable_set_boundary(1.0)
distance_to_planar_reachable_set(1.0, 1.0, 1.0)
nearest_point_to_planar_reachable_set(1.0, 1.0, 1.0)