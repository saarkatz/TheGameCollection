import pygame
from Scene import Scene
from MainMenu import MainMenu
from Event import Event
from SceneChangedException import SceneChangedException

import logging as log
LOG_FILENAME = 'main.log'
LOG_FORMAT = '%(asctime)s:%(levelname)s:%(message)s'
LOG_LEVEL = log.DEBUG
log.basicConfig(filename=LOG_FILENAME, format=LOG_FORMAT, level=LOG_LEVEL)


# The main function. Contains the main loop of the game
def main():
    # Initialize pygame
    log.info('Starting pygame')
    pygame.init()

    game = True
    # Initialize the main menu
    # Manage possible exception in the main menu itself
    try:
        Scene.change_scene(MainMenu)
    except Exception:
        log.exception('Got exception while initializing the main menu')
        game = False

    while game:
        # Handle quit events
        Event.event = pygame.event.wait()
        if Event.event.type == pygame.QUIT:
            break
        if Event.event.type == pygame.KEYDOWN:
            if Event.event.key == pygame.K_ESCAPE or Event.event.unicode == 'q':
                break

        try:
            Scene.scene.step()
        except SceneChangedException:
            continue
        except Exception:
            log.exception('Got exception at step function')
            break

        pygame.display.update()
    else:
        try:
            Scene.scene.stop()
        except Exception:
            log.exception('Got exception while stopping scene to quit pygame')

    log.info("Quitting pygame")
    pygame.quit()


if __name__ == '__main__':
    main()
