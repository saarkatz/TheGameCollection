import pygame
import time

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

# board rows and columns
ROWS = 3
COLUMNS = 3

# The shape of the board
BOARD_SIZE = (400, 400)
BORDER_SIZE = (10, 10)
TOPRIGHT_CORNER = ((RESOLUTION[0] - BOARD_SIZE[0]) / 2, (RESOLUTION[1] - BOARD_SIZE[1]) / 2)
SQUERE_SIZE = ((BOARD_SIZE[0] - BORDER_SIZE[0] * 4) / 3, (BOARD_SIZE[1] - BORDER_SIZE[1] * 4) / 3)

# Player constants
NOPLAYER = 0
PLAYER1 = 1
PLAYER2 = 2

# player colors
NOPLAYER_COLOR = WHITE
PLAYER1_COLOR = BLUE
PLAYER2_COLOR = RED
PLAYER_COLORS = (NOPLAYER_COLOR, PLAYER1_COLOR, PLAYER2_COLOR)

# TODO: ask players what are they're names, and print the winners name at the end (instead of "player 1/2")
WINNING_MESSAGE = 'Congratulations {0} you are the winner!!!'
FONT = 'Comic Sans MS'
FONT_SIZE = 15


# TODO: understand why this function doesn't work...
# Check if current player won the game
def is_win(curr_player, board, curr_row, curr_col):
    """
    check if one of the players won
    :param curr_player: current player (1 or 2)
    :param board: current board state
    :param curr_row: current row
    :param curr_col: current column
    :return: True if winn, False if not
    """
    curr_color = PLAYER1_COLOR
    if curr_player == PLAYER2:
        curr_color = PLAYER2_COLOR

    # count number of cells in a row/ column of the same player
    count = 0

    # check current row
    for column in range(COLUMNS):
        if not board[curr_row][column] == curr_color:
            break
        else:
            count += 1

    # if all cell in the row where the player's color - the player won
    if count == COLUMNS:
        print("wow!!!")
        return True

    # now - check column
    count = 0
    for row in range(ROWS):
        if not board[curr_col][row] == curr_color:
            break
        else:
            count += 1

    # if all cell in the column where the player's color - the player won
    if count == ROWS:
        print("wowww!!!")
        return True

    return False


def update_screen(screen, board, board_view):
    # Draw the board
    screen.fill(PURPLE)
    pygame.draw.rect(screen, BLACK, [TOPRIGHT_CORNER[0], TOPRIGHT_CORNER[1],
                                     BOARD_SIZE[0], BOARD_SIZE[1]])
    for i in range(ROWS):
        for j in range(COLUMNS):
            pygame.draw.rect(screen, PLAYER_COLORS[board[i][j]], board_view[i][j])
    pygame.display.update()


# The main function. Contains the main loop of the game
def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption(CAPTION)

    # The model of the board
    board = [
        [NOPLAYER for _ in range(COLUMNS)] for _ in range(ROWS)
    ]

    # The view of the board
    board_view = [
        [
            pygame.Rect(
                TOPRIGHT_CORNER[0] + BORDER_SIZE[0] + (SQUERE_SIZE[0] + BORDER_SIZE[0]) * i,
                TOPRIGHT_CORNER[1] + BORDER_SIZE[1] + (SQUERE_SIZE[1] + BORDER_SIZE[1]) * j,
                SQUERE_SIZE[0], SQUERE_SIZE[1]
            ) for i in range(COLUMNS)
        ] for j in range(ROWS)
    ]

    turn = 1

    victory = False
    try:
        while not victory:
            # Handle quit events
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    break

            # Game logic
            # when button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # TODO: why is it like that?
                for i in range(ROWS):
                    for j in range(COLUMNS):
                        player = turn % 2

                        if board[i][j] == NOPLAYER and board_view[i][j].collidepoint(pygame.mouse.get_pos()):
                            if player == 1:
                                board[i][j] = PLAYER1
                            else:
                                board[i][j] = PLAYER2
                            turn += 1
                            if is_win(player, board, i, j):
                                if player == 1:
                                    screen.fill(PLAYER1_COLOR)
                                    winner = "player 1"
                                else:
                                    screen.fill(PLAYER2_COLOR)
                                    winner = "player 2"
                                winning_font = pygame.font.SysFont(FONT, FONT_SIZE)
                                winning_text = winning_font.render(WINNING_MESSAGE.format(winner), False, (0, 0, 0))
                                screen.blit(winning_text, (0, 0))
                                pygame.display.update()
                                victory = True
                                time.sleep(5)

            # show regular updated board
            if not victory:
                update_screen(screen, board, board_view)

    finally:
        pygame.quit()


if __name__ == '__main__':
    main()
