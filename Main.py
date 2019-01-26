import pygame
from TicTacToe import TicTacToe
from Screen import Screen
from Event import Event


# The main function. Contains the main loop of the game
def main():
    pygame.init()
    scene = TicTacToe()
    Screen.screen = pygame.display.set_mode(scene.get_resolution())
    pygame.display.set_caption(scene.caption)

    while 1:
        # Handle quit events
        Event.event = pygame.event.wait()
        if Event.event.type == pygame.QUIT:
            break
        if Event.event.type == pygame.KEYDOWN:
            if Event.event.key == pygame.K_ESCAPE or Event.event.unicode == 'q':
                break

        try:
            scene.step()
        except Exception as e:
            print(e)
            break

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
