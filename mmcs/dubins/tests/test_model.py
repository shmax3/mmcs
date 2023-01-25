from unittest import TestCase
from numpy import isclose, pi
from ..model import DubinsCar 


class TestModel(TestCase):

    def setUp(self):
        self.default = DubinsCar() 
        self.custom = DubinsCar(v=2, u_max=1, t0=1, x0=2, y0=2, phi0=3*pi/4)

    def test_default(self):
        self.assertTrue(isclose(self.default.v, 1))
        self.assertTrue(isclose(self.default.u_max, 1))
        self.assertTrue(isclose(self.default.t0, 0))
        self.assertTrue(isclose(self.default.x0, 0))
        self.assertTrue(isclose(self.default.y0, 0))
        self.assertTrue(isclose(self.default.phi0, pi/2))
        self.assertTrue(isclose(self.default.r_min, 1))

    def test_inverse_transform(self):
        t_o, x_o, y_o, phi_o, u_o = 1, 2, 2, 3*pi/4, 1
        t_c, x_c, y_c, phi_c, u_c = self.custom.inverse_transform(t=t_o,
                                                                  x=x_o,
                                                                  y=y_o,
                                                                  phi=phi_o,
                                                                  u=u_o)
        self.assertTrue(isclose(t_c, 0))
        self.assertTrue(isclose(x_c, 0))
        self.assertTrue(isclose(y_c, 0))
        self.assertTrue(isclose(phi_c % (2*pi), pi/2))
        self.assertTrue(isclose(u_c, 1))

    def test_reverse_transform(self):
        t_c, x_c, y_c, phi_c, u_c = 0, 0, 0, pi/2, 1
        t_o, x_o, y_o, phi_o, u_o = self.custom.reverse_transform(t=t_c,
                                                                  x=x_c,
                                                                  y=y_c,
                                                                  phi=phi_c,
                                                                  u=u_c)
        self.assertTrue(isclose(t_o, 1))
        self.assertTrue(isclose(x_o, 2))
        self.assertTrue(isclose(y_o, 2))
        self.assertTrue(isclose(phi_o % (2*pi), 3*pi/4))
        self.assertTrue(isclose(u_o, 1))