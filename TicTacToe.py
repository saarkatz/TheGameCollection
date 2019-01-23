import pygame

CAPTION = 'TicTacToe'
RESOLUTION = (600, 600)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 128)
RED = (128, 0, 0)

BOARD_SIZE = (400, 400)
BORDER_SIZE = (10, 10)
TOPRIGHT_CORNER = ((RESOLUTION[0] - BOARD_SIZE[0]) / 2, (RESOLUTION[1] - BOARD_SIZE[1]) / 2)
SQUERE_SIZE = ((BOARD_SIZE[0] - BORDER_SIZE[0] * 4) / 3, (BOARD_SIZE[1] - BORDER_SIZE[1] * 4) / 3)

NOPLAYER = WHITE
PLAYER1 = BLUE
PLAYER2 = RED


def main():
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption(CAPTION)

    board = [
        [NOPLAYER, NOPLAYER, NOPLAYER],
        [NOPLAYER, NOPLAYER, NOPLAYER],
        [NOPLAYER, NOPLAYER, NOPLAYER]
    ]

    board_view = [
        [
            pygame.Rect(
                TOPRIGHT_CORNER[0] + BORDER_SIZE[0] + (SQUERE_SIZE[0] + BORDER_SIZE[0]) * i,
                TOPRIGHT_CORNER[1] + BORDER_SIZE[1] + (SQUERE_SIZE[1] + BORDER_SIZE[1]) * j,
                SQUERE_SIZE[0], SQUERE_SIZE[1]
            ) for i in range(3)
        ] for j in range(3)
    ]

    try:
        while 1:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    break

            screen.fill(PURPLE)
            pygame.draw.rect(screen, BLACK, [TOPRIGHT_CORNER[0], TOPRIGHT_CORNER[1],
                                             BOARD_SIZE[0], BOARD_SIZE[1]])
            for i in range(3):
                for j in range(3):
                    pygame.draw.rect(screen, board[i][j], board_view[i][j])
            pygame.display.update()
    finally:
        pygame.quit()


if __name__ == '__main__':
    main()
