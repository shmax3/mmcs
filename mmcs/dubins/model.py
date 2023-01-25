from dataclasses import dataclass
from numpy import pi, sin, cos


@dataclass
class DubinsCar:
    v: float = 1.0
    u_max: float = 1.0
    t0: float = 0.0
    x0: float = 0.0
    y0: float = 0.0
    phi0: float = pi/2

    def __post_init__(self):
        self.r_min = self.v/self.u_max

    def inverse_transform_t(self, t):
        return self.u_max*(t - self.t0)

    def inverse_transform_x(self, x, y):
        return ((x - self.x0)*sin(self.phi0)
                - (y - self.y0)*cos(self.phi0))/self.r_min

    def inverse_transform_y(self, x, y):
        return ((x - self.x0)*cos(self.phi0)
                + (y - self.y0)*sin(self.phi0))/self.r_min

    def inverse_transform_phi(self, phi):
        return pi/2 - self.phi0 + phi

    def inverse_transform_u(self, u):
        return u/self.u_max

    def inverse_transform(self, t, x, y, phi, u):
        return (self.inverse_transform_t(t),
                self.inverse_transform_x(x, y),
                self.inverse_transform_y(x, y),
                self.inverse_transform_phi(phi),
                self.inverse_transform_u(u))

    def reverse_transform_t(self, t):
        return self.t0 + t/self.u_max

    def reverse_transform_x(self, x, y):
        return self.x0 + self.r_min*(x*sin(self.phi0) + y*cos(self.phi0))

    def reverse_transform_y(self, x, y):
        return self.y0 + self.r_min*(y*sin(self.phi0) - x*cos(self.phi0))

    def reverse_transform_phi(self, phi):
        return self.phi0 + phi - pi/2

    def reverse_transform_u(self, u):
        return u*self.u_max

    def reverse_transform(self, t, x, y, phi, u):
        return (self.reverse_transform_t(t),
                self.reverse_transform_x(x, y),
                self.reverse_transform_y(x, y),
                self.reverse_transform_phi(phi),
                self.reverse_transform_u(u))