"""
The view of the board
"""
import pygame

BORDER_SIZE_HINT = .017
COLORS = [
    (255, 255, 255),  # WHITE
    (255, 234, 181),
    (255, 213, 151),
    (255, 191, 128),
    (255, 170, 108),
    (255, 149, 90),
    (255, 128, 75),
    (255, 106, 60),
    (255, 85, 47),
    (255, 64, 34),
    (255, 43, 22),
    (255, 21, 11),
    (255, 0, 0),
]


class BoardView:
    def __init__(self, board, screen):
        pygame.font.init()
        self.screen = screen
        self.board = board
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

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
                    h_border + (h_squere + h_border) * y
                self.ui_stage[x][y].size = (w_squere, h_squere)

    def update(self):
        self.update_sizes()
        for x in range(self.get_size(0)):
            for y in range(self.get_size(1)):
                pygame.draw.rect(self.screen, COLORS[self.board[x, y]],
                                 self.ui_stage[x][y])
                if self.board[x, y] > 0:
                    text = self.font.render(str(2 ** self.board[x, y]), False,
                                            (0, 0, 0))
                    self.screen.blit(
                        text,
                        (self.ui_stage[x][y].left + self.ui_stage[x][y].w // 2,
                         self.ui_stage[x][y].top + self.ui_stage[x][y].h // 2)
                    )

    def get_size(self, dim):
        return self.board.get_size(dim)

    def __getitem__(self, item):
        assert 2 == len(item)
        return self.ui_stage[item[0]][item[1]]
