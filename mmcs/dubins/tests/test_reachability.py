from unittest import TestCase
from numpy import isclose, pi
from ..reachability import planar_reachable_set, distance_to_planar_reachable_set
from ..reachability import nearest_point_to_planar_reachable_set


class TestReachability(TestCase):

    def test_planar_reachable_set(self):
        t = [0.0, 1.0, 10.0, 3*pi/2 + 1]
        x = [0.0, 0.0, 1.0, 0.0]
        y = [0.0, 1.0, 0.0, -1.0]
        for t, x, y in zip(t, x, y):
            self.assertTrue(planar_reachable_set(t, x, y))
            self.assertTrue(planar_reachable_set(t, -x, y))
        t = [0.0, 1.0, 10.0, 3*pi/2 + 1]
        x = [0.0, 0.0, 10.0, 0.0]
        y = [1.0, 2.0, 0.0, 0.0]
        for t, x, y in zip(t, x, y):
            self.assertFalse(planar_reachable_set(t, x, y))
            self.assertFalse(planar_reachable_set(t, -x, y))

    def test_distance_to_planar_reachable_set(self):
        t = [9.0, pi/2, 7.0] + [pi/2, pi/2, 3*pi/2, 3*pi/2] + [pi/2] 
        x = [0.0, 1.0, 1.0] + [2.0, 3.0, 2.0, 0.0] + [1.0]
        y = [1.0, 1.0, 0.0] + [1.0, 1.0, -2.0, -1.0] + [0.0]
        d = [0.0, 0.0, 0.0] + [1.0, 2.0, 2 - pi/2, 1.0] + [1.0]
        for t, x, y, d in zip(t, x, y, d):
            self.assertTrue(isclose(distance_to_planar_reachable_set(t, x, y), d))
            self.assertTrue(isclose(distance_to_planar_reachable_set(t, -x, y), d))

    def test_nearest_point_to_planar_reachable_set(self):
        x = [0.0, 1.0, 1.0] + [2.0, 3.0, 2.0] + [1.0]
        y = [1.0, 1.0, 0.0] + [1.0, 1.0, -2.0] + [0.0]
        t = [9.0, pi/2, 7.0] + [pi/2, pi/2, 3*pi/2] + [pi/2] 
        p = ([(0.0, 1.0), (1.0, 1.0), (1.0, 0.0)]
             + [(1.0, 1.0), (1.0, 1.0), (2.0, -pi/2)] + [(1.0, 1.0)])
        for x, y, t, (xa, ya) in zip(x, y, t, p):
            xn, yn = nearest_point_to_planar_reachable_set(t, x, y)
            self.assertTrue(isclose(xn, xa))
            self.assertTrue(isclose(yn, ya))
            xn, yn = nearest_point_to_planar_reachable_set(t, -x, y)
            self.assertTrue(isclose(xn, -xa))
            self.assertTrue(isclose(yn, ya))
        