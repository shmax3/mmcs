from unittest import TestCase
from numpy import isclose, pi, arccos
from ..control import minimum_time_control_to_point, admissible_control_to_point


class TestControl(TestCase):

    def test_minimum_time_control_to_point(self):
        x_dest, y_dest = 2, 1
        n = 100
        t, u = minimum_time_control_to_point(x=x_dest, y=y_dest, n=n)
        self.assertEqual(len(t), n)
        self.assertEqual(len(u), n)
        self.assertTrue(isclose(t[0], 0))
        self.assertTrue(isclose(u[0], -1))
        self.assertTrue(isclose(t[-1], 1 + pi/2))
        self.assertTrue(isclose(u[-1], 0))
        t, u = minimum_time_control_to_point(x=-x_dest, y=y_dest, n=n)
        self.assertEqual(len(t), n)
        self.assertEqual(len(u), n)
        self.assertTrue(isclose(t[0], 0))
        self.assertTrue(isclose(u[0], +1))
        self.assertTrue(isclose(t[-1], 1 + pi/2))
        self.assertTrue(isclose(u[-1], 0))
        x_dest, y_dest = 1, 0
        n = 100
        t, u = minimum_time_control_to_point(x=x_dest, y=y_dest, n=n)
        self.assertEqual(len(t), n)
        self.assertEqual(len(u), n)
        self.assertTrue(isclose(t[0], 0))
        self.assertTrue(isclose(u[0], +1))
        self.assertTrue(isclose(t[-1], 2*pi + arccos(7/8) - arccos(1/4)))
        self.assertTrue(isclose(u[-1], -1))
        t, u = minimum_time_control_to_point(x=-x_dest, y=y_dest, n=n)
        self.assertEqual(len(t), n)
        self.assertEqual(len(u), n)
        self.assertTrue(isclose(t[0], 0))
        self.assertTrue(isclose(u[0], -1))
        self.assertTrue(isclose(t[-1], 2*pi + arccos(7/8) - arccos(1/4)))
        self.assertTrue(isclose(u[-1], +1))

    def test_admissible_control_to_point(self):
        t_dest, x_dest, y_dest = 1 + pi/2, 2, 1
        n = 100
        t, u = admissible_control_to_point(t=t_dest, x=x_dest, y=y_dest, n=n)
        self.assertEqual(len(t), n)
        self.assertEqual(len(u), n)
        self.assertTrue(isclose(t[0], 0))
        self.assertTrue(isclose(u[0], -1))
        self.assertTrue(isclose(t[-1], t_dest))
        self.assertTrue(isclose(u[-1], 0))
        t, u = admissible_control_to_point(t=t_dest, x=-x_dest, y=y_dest, n=n)
        self.assertEqual(len(t), n)
        self.assertEqual(len(u), n)
        self.assertTrue(isclose(t[0], 0))
        self.assertTrue(isclose(u[0], +1))
        self.assertTrue(isclose(t[-1], t_dest))
        self.assertTrue(isclose(u[-1], 0))
        t_dest, x_dest, y_dest = 2*pi + arccos(7/8) - arccos(1/4), 1, 0
        n = 100
        t, u = admissible_control_to_point(t=t_dest, x=x_dest, y=y_dest, n=n)
        self.assertEqual(len(t), n)
        self.assertEqual(len(u), n)
        self.assertTrue(isclose(t[0], 0))
        self.assertTrue(isclose(u[0], +1))
        self.assertTrue(isclose(t[-1], t_dest))
        self.assertTrue(isclose(u[-1], -1))
        t, u = admissible_control_to_point(t=t_dest, x=-x_dest, y=y_dest, n=n)
        self.assertEqual(len(t), n)
        self.assertEqual(len(u), n)
        self.assertTrue(isclose(t[0], 0))
        self.assertTrue(isclose(u[0], -1))
        self.assertTrue(isclose(t[-1], t_dest))
        self.assertTrue(isclose(u[-1], +1))