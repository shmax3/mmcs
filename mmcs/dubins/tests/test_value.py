from unittest import TestCase
from numpy import isclose, pi, arccos
from ..value import minimum_time_to_point, interception_minimum_time


class TestValue(TestCase):

    def test_minimim_time_to_point(self):
        t = [1, pi/2, 3*pi/2 + 1, 2*pi + arccos(7/8) - arccos(1/4)]
        x = [0, 1, 0, 1]
        y = [1, 1, -1, 0]
        for t, x, y in zip(t, x, y):
            self.assertTrue(isclose(minimum_time_to_point(x, y), t))
            self.assertTrue(isclose(minimum_time_to_point(-x, y), t))

    def test_interception_minimum_time(self):
        self.assertTrue(isclose(interception_minimum_time(xt=lambda t: 0.0,
                                                          yt=lambda t: 2.0 + t/2.0,
                                                          r=1.0, v=0.5), 2.0))