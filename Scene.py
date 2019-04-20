import pygame
from Screen import Screen
from SceneChangedException import SceneChangedException


# Interface for scene object.
# TODO: Change the scene to be more managed by the main loop
class Scene:
    scene = None

    def __init__(self):
        self._caption = 'Pygame'
        self._resolution = (500, 500)
        pass

    def get_caption(self):
        return self._caption

    def set_caption(self, caption):
        self._caption = caption
        self.on_caption_change()

    def on_caption_change(self):
        pygame.display.set_caption(self.get_caption())

    def get_resolution(self):
        return self._resolution

    def set_resolution(self, resolution):
        self._resolution = resolution
        self.on_resolution_change()

    def on_resolution_change(self):
        Screen.screen = pygame.display.set_mode(self.get_resolution())

    def start(self):
        pass

    def step(self):
        pass

    def stop(self):
        pass

    @staticmethod
    def change_scene(new_scene):
        '''
        Stops the current scene and initializes the new scene given.
        :param new_scene: The class of the new scene to be initialized.
        '''
        prev_scene = Scene.scene
        if prev_scene:
            Scene.scene.stop()
        Scene.scene = new_scene()

        Scene.scene.start()
        if prev_scene:
            raise SceneChangedException
