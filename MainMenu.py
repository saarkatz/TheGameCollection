import pygame
from gui import Text, VerticalView
from linalg import Vector2
from Scene import Scene
from Screen import Screen
from Event import Event
from TicTacToe import TicTacToe

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


class MainMenu(Scene):
    def __init__(self):
        super().__init__(CAPTION, RESOLUTION)
        self.view = VerticalView((0, 0), (Screen.screen.get_width(), Screen.screen.get_height()),
                                 alignment=0.5 * Vector2.ones())

        self.view.append_object(Text('TicTacToe', size=20))
        self.view.append_object(Text('TicTacToe2', size=20))
        self.view.append_object(Text('TicTacToe3', size=20))

    def step(self):
        # Game logic
        # if Event.event.type == pygame.MOUSEBUTTONDOWN and Event.event.button == 1:
        #     if self.text.rect.collidepoint(pygame.mouse.get_pos()):
        #         Scene.change_scene(TicTacToe)
        #         return

        # Draw the board
        Screen.screen.fill(WHITE)
        pygame.draw.rect(Screen.screen, BLACK, self.view.rect, 2)
        for t in self.view.objects_list:
            pygame.draw.rect(Screen.screen, BLUE, t.parent.rect.move(t.parent.get_global_topleft()), 2)
            pygame.draw.rect(Screen.screen, RED, t.rect.move(t.get_global_topleft()), 2)
            Screen.screen.blit(t.surf, t.get_global_topleft())
