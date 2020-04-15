import pygame

# The title of the windows
CAPTION = 'TextAdventure'

# The size of the window
SIZE = (600, 600)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(CAPTION)

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
    finally:
        pygame.quit()


if __name__ == '__main__':
    main()
