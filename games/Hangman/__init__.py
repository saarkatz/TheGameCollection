import pygame
from Hangman.Board import Board, Direction
from Hangman.BoardView import BoardView

# The title of the windows
CAPTION = 'Hangman'

# The size of the window
SIZE = (600, 600)

BLACK = (0, 0, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(CAPTION)

    # The model of the board
    board = Board()
    board.add_random()
    board.add_random()

    # The view of the board
    boardview = BoardView(board, screen)

    try:
        # The game loop
        while True:
            # Handle quit events
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break

                # Game logic
                letter = event.unicode.lower()

            # Draw the board
            screen.fill(BLACK)
            boardview.update()
            pygame.display.update()

    finally:
        pygame.quit()


if __name__ == '__main__':
    main()
