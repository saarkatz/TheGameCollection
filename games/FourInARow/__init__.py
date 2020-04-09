import pygame
from FourInARow.Board import Board
from FourInARow.BoardView import BoardView


# The title of the windows
CAPTION = 'FourInARow'

# The size of the window
SIZE = (600, 600)

BLACK = (0, 0, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(CAPTION)

    # The model of the board
    board = Board()

    # The view of the board
    boardview = BoardView(board, screen)

    turn = 0

    try:
        # The game loop
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
                x, _ = pygame.mouse.get_pos()
                column = boardview.column_hit(x)
                if column > -1 and board.set_column(1 + turn % 2, column):
                    turn += 1

            # Draw the board
            screen.fill(BLACK)
            boardview.update()
            pygame.display.update()

    finally:
        pygame.quit()


if __name__ == '__main__':
    main()