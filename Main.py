import pygame
from Scene import Scene
from MainMenu import MainMenu
from Event import Event


# The main function. Contains the main loop of the game
def main():
    pygame.init()
    Scene.change_scene(Scene)

    game = True

    try:
        Scene.change_scene(MainMenu)
    except Exception as e:
        print(e)
        game = False

    while game:
        # Handle quit events
        Event.event = pygame.event.wait()
        if Event.event.type == pygame.QUIT:
            game = False
        if Event.event.type == pygame.KEYDOWN:
            if Event.event.key == pygame.K_ESCAPE or Event.event.unicode == 'q':
                game = False

        try:
            Scene.scene.step()
        except Exception as e:
            print(e)
            game = False

        pygame.display.update()
    else:
        try:
            Scene.scene.stop()
        except Exception as e:
            print(e)

    pygame.quit()


if __name__ == '__main__':
    main()
