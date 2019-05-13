import pygame
from gui.gui_object import GUIObject
from gui import Rect

# Colors for use
# TODO: Normalize colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 128)
RED = (128, 0, 0)


class Text(GUIObject):
    """
    Text GUI object.
    """
    def __init__(self, text, size=20, color=BLACK, font='freesansbold.ttf', parent=None):
        super().__init__(parent=parent)
        self.font = pygame.font.Font(font, size)
        self.surf = self.font.render(text, True, color)
        self.rect = Rect.copy(self.surf.get_rect())
