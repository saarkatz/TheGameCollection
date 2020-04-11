import pygame
from Game2048.Board import Board, Direction
from Game2048.BoardView import BoardView


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
    board.add_random()
    board.add_random()

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
                direction = None
                if event.key == pygame.K_UP:
                    direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    direction = Direction.DOWN
                elif event.key == pygame.K_LEFT:
                    direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    direction = Direction.RIGHT

                if direction is not None:
                    if board.slide_board(direction):
                        board.add_random()


            # Draw the board
            screen.fill(BLACK)
            boardview.update()
            pygame.display.update()

    finally:
        pygame.quit()


if __name__ == '__main__':
    main()
