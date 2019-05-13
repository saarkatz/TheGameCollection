from linalg import Vector2
from gui import Rect

DEFAULT_RECT = Rect.from_values(0, 0, 1, 1)


class GUIObject:
    """
    Base class for GUI.
    """
    def __init__(self, parent=None):
        self.rect = Rect.copy(DEFAULT_RECT)
        self.anchor = Vector2.zeros()

        self.parent = parent

    @property
    def position(self):
        return self.rect.position

    @position.setter
    def position(self, value):
        self.rect.position = value

    def get_global_topleft(self):
        """
        Calculates the topleft position of the GUI object in real world space.
        :return: Vector2 with the global topleft of the object
        """
        position = self.rect.topleft
        if self.parent:
            position += self.parent.get_global_topleft() + self.anchor * self.parent.rect.size
        return position
