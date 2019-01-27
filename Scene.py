import pygame
from Screen import Screen


# Interface for scene object.
# TODO: Change the scene to be more managed by the main loop
class Scene:
    scene = None

    def __init__(self):
        self.caption = 'Pygame'
        self.resolution = (500, 500)
        pass

    def get_caption(self):
        return self.caption

    def get_resolution(self):
        return self.resolution

    def start(self):
        pass

    def step(self):
        pass

    def stop(self):
        pass

    # Change the scenes
    @staticmethod
    def change_scene(new_scene):
        if Scene.scene:
            Scene.scene.stop()
        Scene.scene = new_scene()

        Screen.screen = pygame.display.set_mode(Scene.scene.get_resolution())
        pygame.display.set_caption(Scene.scene.caption)

        Scene.scene.start()
