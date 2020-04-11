"""
The view of the board
"""
import pygame


BORDER_SIZE_HINT = .017
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)
RED = (128, 0, 0)

NOPLAYER = WHITE
PLAYER1 = BLUE
PLAYER2 = RED


def player_color(player_id):
    if player_id == 0:
        return NOPLAYER
    elif player_id == 1:
        return PLAYER1
    else:
        return PLAYER2


def in_column(position, rectangle):
    return rectangle.left <= position < rectangle.right


class BoardView:
    def __init__(self, board, screen):
        self.screen = screen
        self.board = board

        self.size_cache = None

        # Init ui_stage
        self.ui_stage = [
            [pygame.Rect(0, 0, 0, 0) for _ in range(self.board.get_size(1))]
            for _ in range(self.board.get_size(0))
        ]

    def update_sizes(self):
        if self.size_cache == self.screen.get_size():
            return
        else:
            self.size_cache = self.screen.get_size()

        # Update the size of the stage
        width, height = self.screen.get_size()
        w_border = int(width * BORDER_SIZE_HINT)
        h_border = int(height * BORDER_SIZE_HINT)
        w_squere = (width - w_border * (self.get_size(0) + 1)
                    ) // self.get_size(0)
        h_squere = (height - h_border * (self.get_size(1) + 1)
                    ) // self.get_size(1)

        for x in range(self.get_size(0)):
            for y in range(self.get_size(1)):
                self.ui_stage[x][y].left = w_border + (w_squere + w_border) * x
                self.ui_stage[x][y].bottom = \
                    height - (h_squere + h_border) * (y + 1)
                self.ui_stage[x][y].size = (w_squere, h_squere)

    def update(self):
        self.update_sizes()
        for x in range(self.get_size(0)):
            for y in range(self.get_size(1)):
                pygame.draw.rect(self.screen, player_color(self.board[x, y]),
                                 self.ui_stage[x][y])

    def get_size(self, dim):
        return self.board.get_size(dim)

    def __getitem__(self, item):
        assert 2 == len(item)
        return self.ui_stage[item[0]][item[1]]

    def column_hit(self, position):
        for x in range(self.get_size(0)):
            if in_column(position, self.ui_stage[x][0]):
                return x
        return -1
