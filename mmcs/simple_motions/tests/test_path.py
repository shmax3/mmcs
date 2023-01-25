from unittest import TestCase
from numpy import isclose, sqrt, isnan
from ..path import minimum_time_path, admissible_path


class TestPath(TestCase):

    def test_minimum_time_path(self):
        x_dest, y_dest = 2, 1
        n = 100
        t, x, y = minimum_time_path(x=x_dest, y=y_dest, n=n)
        self.assertEqual(len(t), n)
        self.assertEqual(len(x), n)
        self.assertEqual(len(y), n)
        self.assertTrue(isclose(t[0], 0))
        self.assertTrue(isclose(x[0], 0))
        self.assertTrue(isclose(y[0], 0))
        self.assertTrue(isclose(t[-1], sqrt(5)))
        self.assertTrue(isclose(x[-1], x_dest))
        self.assertTrue(isclose(y[-1], y_dest))

    def test_admissible_path(self):
        t_dest, x_dest, y_dest = 5, 2, 1
        n = 100
        t, x, y = admissible_path(t=t_dest, x=x_dest, y=y_dest, n=n)
        self.assertEqual(len(t), n)
        self.assertEqual(len(x), n)
        self.assertEqual(len(y), n)
        self.assertTrue(isclose(t[0], 0))
        self.assertTrue(isclose(x[0], 0))
        self.assertTrue(isclose(y[0], 0))
        self.assertTrue(isclose(t[-1], t_dest))
        self.assertTrue(isclose(x[-1], x_dest))
        self.assertTrue(isclose(y[-1], y_dest))
        t_dest, x_dest, y_dest = 1, 2, 1
        n = 100
        t, x, y = admissible_path(t=t_dest, x=x_dest, y=y_dest, n=n)
        self.assertEqual(len(t), n)
        self.assertEqual(len(x), n)
        self.assertEqual(len(y), n)
        self.assertTrue(isclose(t[0], 0))
        self.assertTrue(isclose(t[-1], t_dest))
        self.assertTrue(all(isnan(x)))
        self.assertTrue(all(isnan(y)))