import pygame
from Hangman.Board import WordList, HangmanLogic
from Hangman.BoardView import BoardView

# The title of the windows
CAPTION = 'Hangman'

# The size of the window
SIZE = (600, 600)

BLACK = (0, 0, 0)
COLORS = {"black": (0, 0, 0), "darkgray": (70, 70, 70), "gray": (128, 128, 128), "lightgray": (200, 200, 200),
          "white": (255, 255, 255), "red": (255, 0, 0),
          "darkred": (128, 0, 0), "green": (0, 255, 0), "darkgreen": (0, 128, 0), "blue": (0, 0, 255),
          "navy": (0, 0, 128), "darkblue": (0, 0, 128),
          "yellow": (255, 255, 0), "gold": (255, 215, 0), "orange": (255, 165, 0), "lilac": (229, 204, 255),
          "lightblue": (135, 206, 250), "teal": (0, 128, 128),
          "cyan": (0, 255, 255), "purple": (150, 0, 150), "pink": (238, 130, 238), "brown": (139, 69, 19),
          "lightbrown": (222, 184, 135), "lightgreen": (144, 238, 144),
          "turquoise": (64, 224, 208), "beige": (245, 245, 220), "honeydew": (240, 255, 240),
          "lavender": (230, 230, 250), "crimson": (220, 20, 60)}


def main():
    # initiate the game
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(CAPTION)

    # The model of the board
    word_list = WordList("Words/words.txt")
    hangman_logic = HangmanLogic(word_list.get_random_word(), 6)

    # The view of the board
    boardview = BoardView(hangman_logic, screen, "Images", "Sounds")

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
            screen.fill(COLORS["white"])
            boardview.update()
            pygame.display.update()

    finally:
        pygame.quit()


if __name__ == '__main__':
    main()
