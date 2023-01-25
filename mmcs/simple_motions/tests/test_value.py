from unittest import TestCase
from numpy import isclose, sqrt
from ..value import minimum_time, interception_minimum_time


class TestValue(TestCase):

    def test_minimum_time(self):
        t = [1, sqrt(2)]
        x = [0, 1]
        y = [1, 1]
        for t, x, y in zip(t, x, y):
            self.assertTrue(isclose(minimum_time(x, y), t))

    def test_interception_minimum_time(self):
        self.assertTrue(isclose(interception_minimum_time(xt=lambda t: 0.0,
                                                          yt=lambda t: 2.0 + t/2.0,
                                                          r=1.0, v=0.5), 2.0))