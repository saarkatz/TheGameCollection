import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('TicTacToe')

    black = (0, 0, 0)
    white = (255, 255, 255)

    try:
        while 1:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    break
            screen.fill((255 / 2, 0, 255 / 2))
            pygame.draw.rect(screen, black, [100, 100, 400, 400])
            for i in range(3):
                for j in range(3):
                    pygame.draw.rect(screen, white, [110 + 130*i, 110 + 130*j, 120, 120])
            pygame.display.flip()
    finally:
        pygame.quit()


if __name__ == '__main__':
    main()
