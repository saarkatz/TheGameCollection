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
    def zero():
        return Vector(0, 0)

    @staticmethod
    def right():
        return Vector(1, 0)

    @staticmethod
    def up():
        return Vector(0, 1)


if __name__ == '__main__':
    print('Testing Vector class... ', end='')

    # Initialization
    v1 = Vector(3, 4)
    t1 = Vector(3, 4)
    t2 = Vector(3, 3)
    assert v1.x == 3 and v1.y == 4
    # Equality
    assert v1 == t1
    assert not t1 == t2
    # Set equality
    assert len({v1, t1, t2}) == 2

    # Representation
    assert 'Vector(3, 4)' == repr(v1)

    # Add number
    v2 = v1 + 1
    t1 = 1 + v1
    assert v2 is not v1
    assert v2.x == t1.x == 4 and v2.y == t1.y == 5
    # Add vector
    v3 = v1 + v2
    t2 = v1 + (4, 5)
    assert v3 is not v1 and v3 is not v2
    assert v3.x == 7 and v3.y == 9
    assert t2 == v3

    # Sub number
    v4 = v2 - 1
    assert v4 == v1
    # Sub vector
    v5 = v3 - v2
    assert v5 == v1

    # Multiply number
    v6 = v1 * 2
    t1 = 2 * v1
    assert v6.x == 6 and v6.y == 8
    assert v6 == t1
    # Multiply vector
    v7 = v1 * v2
    assert v7.x == 12 and v7.y == 20

    # Power number
    v8 = v1 ** 2
    v9 = v1 ** 2 % 5
    assert v8.x == 9 and v8.y == 16
    assert v9.x == 4 and v9.y == 1
    # Power vector
    v10 = v1 ** v1
    v11 = v1 ** v1 % 7
    assert v10.x == 27 and v10.y == 256
    assert v11.x == 6 and v11.y == 4

    # True div number
    v12 = v1 / 2
    assert v12.x == 1.5 and v12.y == 2.0
    # True div vector
    v13 = v10 / v2
    assert v13.x == 27 / 4 and v13.y == 256 / 5

    # floor div number
    v14 = v1 // 2
    assert v14.x == 1 and v14.y == 2
    # True div vector
    v15 = v10 // v2
    assert v15.x == 6 and v15.y == 51

    # Modulo number
    v16 = v10 % 7
    assert v16 == v11
    # Modulo vector
    v17 = v10 % v2
    assert v17.x == 3 and v17.y == 1

    # Modulo floor div sum
    assert v2 * v15 + v17 == v10

    # Addition auxiliary
    v18 = v1
    v18 += 1
    assert v18 == v2
    assert v18 is not v1

    # From polar
    from math import pi

    v19 = Vector.from_polar(1, pi / 2)
    v20 = Vector.from_polar(2, pi)
    assert v19.x < 1e-10 and v19.y == 1
    assert v20.x == -2 and v20.y < 1e-10

    print('Done!')
