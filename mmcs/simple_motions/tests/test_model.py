from unittest import TestCase
from numpy import isclose
from ..model import SimpleMotions


class TestModel(TestCase):

    def setUp(self):
        self.default = SimpleMotions()
        self.custom = SimpleMotions(v_max=2, t0=1, x0=2, y0=3)

    def test_init(self):
        self.assertEqual(self.default.v_max, 1)
        self.assertEqual(self.default.t0, 0)
        self.assertEqual(self.default.x0, 0)
        self.assertEqual(self.default.y0, 0)
        
    def test_inverse_transform(self):
        t_orig, x_orig, y_orig, v_orig = 1, 2, 3, 2
        t_canon, x_canon, y_canon, v_canon = self.custom.inverse_transform(t=t_orig,
                                                                           x=x_orig,
                                                                           y=y_orig,
                                                                           v=v_orig)
        self.assertTrue(isclose(t_canon, 0))
        self.assertTrue(isclose(x_canon, 0))
        self.assertTrue(isclose(y_canon, 0))
        self.assertTrue(isclose(v_canon, 1))

    def test_reverse_transform(self):
        t_canon, x_canon, y_canon, v_canon = 0, 0, 0, 1
        t_orig, x_orig, y_orig, v_orig  = self.custom.reverse_transform(t=t_canon,
                                                                        x=x_canon,
                                                                        y=y_canon,
                                                                        v=v_canon)
        self.assertTrue(isclose(t_orig, 1))
        self.assertTrue(isclose(x_orig, 2))
        self.assertTrue(isclose(y_orig, 3))
        self.assertTrue(isclose(v_orig, 2))