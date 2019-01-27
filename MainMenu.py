import pygame
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


# The main function. Contains the main loop of the game
class MainMenu(Scene):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.caption = CAPTION
        self.resolution = RESOLUTION

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
