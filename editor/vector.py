"""
Vector is responsible for supplying the underling operations needed for
vector arithmetics.
"""
from math import sqrt, cos, sin, asin
from typing import Sequence


class Vector(Sequence):
    """Immutable vector type"""

    def __init__(self, x, y):
        self._vector = (x, y)

    @staticmethod
    def copy(vector):
        return Vector(vector[0], vector[1])

    @staticmethod
    def lin(x):
        return Vector(x, x)

    @staticmethod
    def from_polar(length, angle):
        return Vector(length * cos(angle), length * sin(angle))

    @property
    def x(self):
        return self._vector[0]

    @property
    def y(self):
        return self._vector[1]

    # TODO: Cache polar coordinates
    @property
    def r(self):
        return abs(self)

    @property
    def phi(self):
        if self.r:
            return asin(self.y / self.r)
        else:
            return 0

    # TODO: If the vector is integer type of too large a value than calculating the magnitude can raise an exception
    def magnitude(self):
        return sqrt(self.sqr_magnitude())

    def sqr_magnitude(self):
        return self.dot(self)

    def dot(self, other):
        return self.x * other[0] + self.y * other[1]

    def cross(self, other):
        return self.x * other[1] - self.y * other[0]

    def _test_type(self, obj):
        """
        Returns True if obj is of a type on which self can operate.
        """
        return isinstance(obj, Sequence) and len(obj) >= len(self)

    def __add__(self, other):
        if Vector._test_type(self, other):
            return Vector(self.x + other[0], self.y + other[1])
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if Vector._test_type(self, other):
            return Vector(self.x - other[0], self.y - other[1])
        elif isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if Vector._test_type(self, other):
            return Vector(other[0] - self.x, other[1] - self.y)
        else:
            return NotImplemented

    def __mul__(self, other):
        if Vector._test_type(self, other):
            return Vector(self.x * other[0], self.y * other[1])
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __pow__(self, power, modulo=None):
        if Vector._test_type(self, power):
            if modulo:
                if Vector._test_type(self, modulo):
                    return Vector(self.x ** power[0] % modulo[0],
                                  self.y ** power[1] % modulo[1])
                else:
                    return Vector(self.x ** power[0] % modulo,
                                  self.y ** power[1] % modulo)
            else:
                return Vector(self.x ** power[0], self.y ** power[1])
        elif isinstance(power, (int, float)):
            if modulo:
                if Vector._test_type(self, modulo):
                    return Vector(self.x ** power % modulo[0],
                                  self.y ** power % modulo[1])
                else:
                    return Vector(self.x ** power % modulo,
                                  self.y ** power % modulo)
            else:
                return Vector(self.x ** power, self.y ** power)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if Vector._test_type(self, other):
            return Vector(self.x / other[0], self.y / other[1])
        elif isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other)
        else:
            return NotImplemented

    def __floordiv__(self, other):
        if Vector._test_type(self, other):
            return Vector(self.x // other[0], self.y // other[1])
        elif isinstance(other, (int, float)):
            return Vector(self.x // other, self.y // other)
        else:
            return NotImplemented

    def __mod__(self, other):
        if Vector._test_type(self, other):
            return Vector(self.x % other[0], self.y % other[1])
        elif isinstance(other, (int, float)):
            return Vector(self.x % other, self.y % other)
        else:
            return NotImplemented

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return self.magnitude()

    def __iter__(self):
        return iter(self._vector)

    def __getitem__(self, item):
        return self._vector[item]

    def __len__(self):
        return 2

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self._vector == other._vector
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self._vector)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '{0}({1}, {2})'.format(self.__class__.__name__, self.x, self.y)

    @staticmethod
    def one():
        return Vector(1, 1)

    @staticmethod
    def second():
        return Vector(1, -1)

    @staticmethod
    def zero():
        return Vector(0, 0)

    @staticmethod
    def right():
        return Vector(1, 0)

    @staticmethod
    def up():
        return Vector(0, 1)

    def int(self):
        return Vector(int(self.x), int(self.y))