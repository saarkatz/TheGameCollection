import pygame
from Scene import Scene
from Screen import Screen
from Event import Event

# The title of the windows
CAPTION = 'TicTacToe'
# The resolution of the windows
RESOLUTION = (600, 600)

# Colors for use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 128)
RED = (128, 0, 0)

# The shape of the board
BOARD_SIZE = (400, 400)
BORDER_SIZE = (10, 10)
TOPRIGHT_CORNER = ((RESOLUTION[0] - BOARD_SIZE[0]) / 2, (RESOLUTION[1] - BOARD_SIZE[1]) / 2)
SQUERE_SIZE = ((BOARD_SIZE[0] - BORDER_SIZE[0] * 4) / 3, (BOARD_SIZE[1] - BORDER_SIZE[1] * 4) / 3)

# Player constants
NOPLAYER = WHITE
PLAYER1 = BLUE
PLAYER2 = RED


# The main function. Contains the main loop of the game
class TicTacToe(Scene):
    def __init__(self):
        super(TicTacToe, self).__init__()
        self.caption = CAPTION
        self.resolution = RESOLUTION

        # The model of the board
        self.board = [
            [NOPLAYER, NOPLAYER, NOPLAYER],
            [NOPLAYER, NOPLAYER, NOPLAYER],
            [NOPLAYER, NOPLAYER, NOPLAYER]
        ]

        # The view of the board
        self.board_view = [
            [
                pygame.Rect(
                    TOPRIGHT_CORNER[0] + BORDER_SIZE[0] + (SQUERE_SIZE[0] + BORDER_SIZE[0]) * i,
                    TOPRIGHT_CORNER[1] + BORDER_SIZE[1] + (SQUERE_SIZE[1] + BORDER_SIZE[1]) * j,
                    SQUERE_SIZE[0], SQUERE_SIZE[1]
                ) for i in range(3)
            ] for j in range(3)
        ]

        self.turn = 1

    def step(self):
        # Game logic
        # TODO: Change the way events are handled
        if Event.event.type == pygame.MOUSEBUTTONDOWN and Event.event.button == 1:
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == NOPLAYER and \
                            self.board_view[i][j].collidepoint(pygame.mouse.get_pos()):
                        if self.turn % 2 == 1:
                            self.board[i][j] = PLAYER1
                        else:
                            self.board[i][j] = PLAYER2
                        self.turn += 1

        # Draw the board
        # TODO: Change the way the screen is accessed
        Screen.screen.fill(PURPLE)
        pygame.draw.rect(Screen.screen, BLACK, [TOPRIGHT_CORNER[0], TOPRIGHT_CORNER[1],
                                         BOARD_SIZE[0], BOARD_SIZE[1]])
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(Screen.screen, self.board[i][j], self.board_view[i][j])
