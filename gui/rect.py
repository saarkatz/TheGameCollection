from typing import Sequence
from linalg import Vector2


class Rect(Sequence):
    """
    Rectangle object
    """
    def __init__(self, position, size, pivot=Vector2.zeros()):
        self._position = None
        self._size = None
        self._pivot = None

        self.position = position
        self.size = size
        self.pivot = pivot

    @staticmethod
    def copy(rect):
        return Rect.from_values(rect[0], rect[1], rect[2], rect[3])

    @staticmethod
    def from_values(right, top, width, height, pivot=Vector2.zeros()):
        return Rect(Vector2(right + width * pivot[0], top + height * pivot[1]), Vector2(width, height), pivot)

    @property
    def x(self):
        return self.position.x - self.size.x * self.pivot.x

    @x.setter
    def x(self, value):
        self.position = Vector2(self.size.x * self.pivot.x + value, self.position.y)

    @property
    def y(self):
        return self.position.y - self.size.y * self.pivot.y

    @y.setter
    def y(self, value):
        self.position = Vector2(self.position.x, self.size.y * self.pivot.y + value)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if isinstance(value, Vector2):
            self._position = value
        else:
            self._position = Vector2.copy(value)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, Vector2):
            self._size = value
        else:
            self._size = Vector2.copy(value)

    @property
    def pivot(self):
        return self._pivot

    @pivot.setter
    def pivot(self, value):
        if isinstance(value, Vector2):
            self._pivot = value
        else:
            self._pivot = Vector2.copy(value)

    @property
    def left(self):
        return self.x
    @property
    def right(self):
        return self.x + self.size[0]
    @property
    def top(self):
        return self.y
    @property
    def bottom(self):
        return self.y + self.size[1]

    @property
    def topleft(self):
        return self.left, self.top
    @property
    def topright(self):
        return self.right, self.top
    @property
    def bottomleft(self):
        return self.left, self.bottom
    @property
    def bottomright(self):
        return self.right, self.bottom

    @property
    def centerx(self):
        return self.x + self.size.x * 0.5
    @property
    def centery(self):
        return self.y + self.size.y * 0.5
    @property
    def center(self):
        return self.centerx, self.centery
    @property
    def midtop(self):
        return self.centerx, self.top
    @property
    def midbottom(self):
        return self.centerx, self.bottom
    @property
    def midleft(self):
        return self.left, self.centery
    @property
    def midright(self):
        return self.right, self.centery

    @property
    def width(self):
        return self.size.x
    @property
    def height(self):
        return self.size.y

    def move(self, offset):
        rect = Rect.copy(self)
        rect.position = offset
        return rect

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.size[0]
        elif item == 3:
            return self.size[1]
        else:
            raise IndexError('Rect index out of range')

    def __len__(self):
        return 4

    def __str__(self):
        return '{0}({1}, {2}, {3}, {4}, pivot={5})'.format(self.__class__.__name__, *self, tuple(self.pivot))

    def __repr__(self):
        return '{0}({1}, {2}, pivot={3})'.format(self.__class__.__name__, self.position, self.size, self.pivot)


if __name__ == '__main__':
    r1 = Rect.from_values(0, 0, 1, 1)
    r2 = Rect((0, 1), (1, 2), pivot=(0, 0))
    print(r1)
    print(r2)
    print(r2.x, r2.size.x)
    print(r2.center)
    r2.size = (10, 13)
    print(r2)
    print(r2.center)
    r2.pivot = (0.5, 0.5)
    print(r2)
    print(r2.center)
    # r2.top = 5
    # print(r2.top)
    # print({v: getattr(r2, v) for v in ('x', 'y', 'size', 'top', 'bottom', 'left', 'right')})
    # r2.size = (2, 3)
    # print(r2)
    # print({v: getattr(r2, v) for v in ('x', 'y', 'size', 'top', 'bottom', 'left', 'right')})
    # r2.x += 1
    # print(r2)
    # print({v: getattr(r2, v) for v in ('x', 'y', 'size', 'top', 'bottom', 'left', 'right')})
    # r2.top += 1
    # print(r2)
    # print({v: getattr(r2, v) for v in ('x', 'y', 'size', 'top', 'bottom', 'left', 'right')})
