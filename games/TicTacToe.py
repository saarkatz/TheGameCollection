import pygame

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
TOPRIGHT_CORNER = ((RESOLUTION[0] - BOARD_SIZE[0]) // 2,
                   (RESOLUTION[1] - BOARD_SIZE[1]) // 2)
SQUERE_SIZE = ((BOARD_SIZE[0] - BORDER_SIZE[0] * 4) // 3,
               (BOARD_SIZE[1] - BORDER_SIZE[1] * 4) // 3)

# Player constants
NOPLAYER = WHITE
PLAYER1 = BLUE
PLAYER2 = RED


# The main function. Contains the main loop of the game
def main():
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption(CAPTION)

    # The model of the board
    board = [
        [NOPLAYER, NOPLAYER, NOPLAYER],
        [NOPLAYER, NOPLAYER, NOPLAYER],
        [NOPLAYER, NOPLAYER, NOPLAYER]
    ]

    # The view of the board
    board_view = [
        [
            pygame.Rect(
                TOPRIGHT_CORNER[0] + BORDER_SIZE[0] + (
                        SQUERE_SIZE[0] + BORDER_SIZE[0]) * i,
                TOPRIGHT_CORNER[1] + BORDER_SIZE[1] + (
                        SQUERE_SIZE[1] + BORDER_SIZE[1]) * j,
                SQUERE_SIZE[0], SQUERE_SIZE[1]
            ) for i in range(3)
        ] for j in range(3)
    ]

    turn = 1

    try:
        while True:
            # Handle quit events
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    break

            # Game logic
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == NOPLAYER and \
                                board_view[i][j].collidepoint(
                                    *pygame.mouse.get_pos()):
                            if turn % 2 == 1:
                                board[i][j] = PLAYER1
                            else:
                                board[i][j] = PLAYER2
                            turn += 1

            # Draw the board
            screen.fill(PURPLE)
            pygame.draw.rect(screen, BLACK,
                             [TOPRIGHT_CORNER[0], TOPRIGHT_CORNER[1],
                              BOARD_SIZE[0], BOARD_SIZE[1]])
            for i in range(3):
                for j in range(3):
                    pygame.draw.rect(screen, board[i][j], board_view[i][j])
            pygame.display.update()

    finally:
        pygame.quit()


if __name__ == '__main__':
    main()
