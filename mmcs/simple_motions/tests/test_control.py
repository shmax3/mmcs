from unittest import TestCase
from numpy import isclose, sqrt, pi
from ..control import minimum_time_control, admissible_control


class TestControl(TestCase):

    def test_minimum_time_path(self):
        x_dest, y_dest = 1, 1
        n = 100
        t, v, phi = minimum_time_control(x=x_dest, y=y_dest, n=n)
        self.assertEqual(len(t), n)
        self.assertEqual(len(v), n)
        self.assertEqual(len(phi), n)
        self.assertTrue(isclose(t[0], 0))
        self.assertTrue(isclose(t[-1], sqrt(2)))
        self.assertTrue(isclose(v[0], 1))
        self.assertTrue(all(isclose(v[0], v)))
        self.assertTrue(isclose(phi[0], pi/4))
        self.assertTrue(all(isclose(phi[0], phi)))

    def test_admissible_path(self):
        t_dest, x_dest, y_dest = 2, 1, 1
        n = 100
        t, v, phi = admissible_control(t=t_dest, x=x_dest, y=y_dest, n=n)
        self.assertEqual(len(t), n)
        self.assertEqual(len(v), n)
        self.assertEqual(len(phi), n)
        self.assertTrue(isclose(t[0], 0))
        self.assertTrue(isclose(t[-1], 2))
        self.assertTrue(isclose(v[0], sqrt(2)/2))
        self.assertTrue(all(isclose(v[0], v)))
        self.assertTrue(isclose(phi[0], pi/4))
        self.assertTrue(all(isclose(phi[0], phi)))
