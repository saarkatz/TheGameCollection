from abc import ABC, abstractmethod
from engine.space2d import Vector


class UiBase(ABC):
    def __init__(self, transform, size=Vector.one()):
        self.transform = transform
        self._size = None
        self.size = size

        self.left_children = []
        self.right_children = []

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = Vector(abs(value[0]), abs(value[1]))

    def _draw(self, screen):
        for child in self.left_children:
            child._draw(screen)

        self.draw(screen)

        for child in self.right_children:
            child._draw(screen)

    @abstractmethod
    def draw(self, screen):
        pass
