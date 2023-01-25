from dataclasses import dataclass


@dataclass
class SimpleMotions:
    v_max: float = 1.0
    t0: float = 0.0
    x0: float = 0.0
    y0: float = 0.0

    def inverse_transform_t(self, t):
        return self.v_max*(t - self.t0)

    def inverse_transform_x(self, x):
        return x - self.x0

    def inverse_transform_y(self, y):
        return y - self.y0 

    def inverse_transform_v(self, v):
        return v/self.v_max

    def inverse_transform(self, t, x, y, v):
        return (self.inverse_transform_t(t),
                self.inverse_transform_x(x),
                self.inverse_transform_y(y),
                self.inverse_transform_v(v))

    def reverse_transform_t(self, t):
        return self.t0 + t/self.v_max

    def reverse_transform_x(self, x):
        return x + self.x0 

    def reverse_transform_y(self, y):
        return y + self.y0 

    def reverse_transform_v(self, v):
        return v*self.v_max

    def reverse_transform(self, t, x, y, v):
        return (self.reverse_transform_t(t),
                self.reverse_transform_x(x),
                self.reverse_transform_y(y),
                self.reverse_transform_v(v))