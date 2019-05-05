import pygame
from Scene import Scene
from Screen import Screen
from Event import Event
from TicTacToe import TicTacToe
from CallbackProperty import make_callback

# The title of the windows
CAPTION = 'The Game Collection'
# The resolution of the windows
RESOLUTION = (500, 500)

# Colors for use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 128)
RED = (128, 0, 0)

DEFAULT_RECT = pygame.Rect(0,0,10,10)


@make_callback('position', lambda self, value: setattr(self.rect, self.anchor, value))
class ViewObject:
    def __init__(self, parent=None):
        self._init_position()
        self.rect = DEFAULT_RECT
        self.anchor = 'topleft'

        self.position = (0, 0)
        self.parent = parent

    def get_real_position(self):
        position = list(self.position)
        if self.parent:
            parent_position = self.parent.get_real_position()
            position[0] += parent_position[0]
            position[1] += parent_position[1]
        return position


class Panel(ViewObject):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.child = None


class VerticalView(ViewObject):
    def __init__(self, position, size, parent=None):
        super().__init__(parent=parent)
        self.position = position
        self.rect.size = size
        self.objects_list = []

    def _update_positions(self):
        if len(self.objects_list) == 0:
            return
        height = self.rect.size[1] / len(self.objects_list)
        for i, panel in enumerate(self.objects_list):
            panel.position = (self.position[0], self.position[1] + i * height)
            panel.rect.size = (self.rect.size[0], height)

    def append_object(self, obj):
        panel = Panel(self)
        panel.anchor = 'bottomright'
        obj.parent = panel
        self.objects_list.append(obj)
        self._update_positions()


class Text(ViewObject):
    def __init__(self, text, size=20, color=BLACK, font='freesansbold.ttf', parent=None):
        super().__init__(parent=parent)
        self.font = pygame.font.Font(font, size)
        self.surf = self.font.render(text, True, color)
        self.rect = self.surf.get_rect()


class MainMenu(Scene):
    def __init__(self):
        super().__init__(CAPTION, RESOLUTION)
        self.large_text = pygame.font.Font('freesansbold.ttf', 100)
        self.text_surf = self.large_text.render('TicTacToe', True, BLACK)
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = ((Screen.screen.get_width() / 2), (Screen.screen.get_height()/ 2))

    def start(self):
        Screen.screen.fill(WHITE)

    def step(self):
        # Game logic
        if Event.event.type == pygame.MOUSEBUTTONDOWN and Event.event.button == 1:
            if self.text_rect.collidepoint(pygame.mouse.get_pos()):
                Scene.change_scene(TicTacToe)
                return

        # Draw the board
        Screen.screen.blit(self.text_surf, self.text_rect)
