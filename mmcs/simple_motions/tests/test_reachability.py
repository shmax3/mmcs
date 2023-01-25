from unittest import TestCase
from numpy import isclose, pi, sqrt
from ..reachability import reachable_set, distance_to_reachable_set
from ..reachability import nearest_point_to_reachable_set


class TestReachability(TestCase):

    def test_reachable_set(self):
        x = [0.0, 0.0, 1.0, 0.0]
        y = [0.0, 1.0, 0.0, -1.0]
        t = [0.0, 1.0, 10.0, 2.0]
        for x, y, t in zip(x, y, t):
            self.assertTrue(reachable_set(t, x, y))
            self.assertTrue(reachable_set(t, -x, y))
            self.assertTrue(reachable_set(t, x, -y))
            self.assertTrue(reachable_set(t, -x, -y))
        x = [0.0, 0.0, 10.0, 1.0]
        y = [1.0, 2.0, 0.0, 0.0]
        t = [0.0, 1.0, 9.0, 0.0]
        for x, y, t in zip(x, y, t):
            self.assertFalse(reachable_set(t, x, y))
            self.assertFalse(reachable_set(t, -x, y))
            self.assertFalse(reachable_set(t, x, -y))
            self.assertFalse(reachable_set(t, -x, -y))

    def test_distance_to_reachable_set(self):
        x = [0.0, 1.0, 2.0, 1.0] 
        y = [0.0, 1.0, 0.0, 1.0] 
        t = [0.0, 2.0, 1.0, 0.0] 
        d = [0.0, 0.0, 1.0, sqrt(2)] 
        for x, y, t, d in zip(x, y, t, d):
            self.assertTrue(isclose(distance_to_reachable_set(t, x, y), d))
            self.assertTrue(isclose(distance_to_reachable_set(t, -x, y), d))
            self.assertTrue(isclose(distance_to_reachable_set(t, x, -y), d))
            self.assertTrue(isclose(distance_to_reachable_set(t, -x, -y), d))

    def test_nearest_point_to_reachable_set(self):
        x = [0.0, 1.0, 0.0, 2.0]
        y = [0.0, 0.0, 3.0, 2.0] 
        t = [0.0, 0.0, 1.0, sqrt(2)] 
        p = [(0.0, 0.0), (0.0, 0.0), (0.0, 1.0), (1.0, 1.0)] 
        for x, y, t, (xa, ya) in zip(x, y, t, p):
            xn, yn = nearest_point_to_reachable_set(t, x, y)
            self.assertTrue(isclose(xn, xa))
            self.assertTrue(isclose(yn, ya))
            xn, yn = nearest_point_to_reachable_set(t, -x, y)
            self.assertTrue(isclose(xn, -xa))
            self.assertTrue(isclose(yn, ya))
            xn, yn = nearest_point_to_reachable_set(t, x, -y)
            self.assertTrue(isclose(xn, xa))
            self.assertTrue(isclose(yn, -ya))
            xn, yn = nearest_point_to_reachable_set(t, -x, -y)
            self.assertTrue(isclose(xn, -xa))
            self.assertTrue(isclose(yn, -ya))
        