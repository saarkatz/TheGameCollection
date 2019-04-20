import pygame
from Screen import Screen
from SceneChangedException import SceneChangedException


# Interface for scene object.
# TODO: Change the scene to be more managed by the main loop
class Scene:
    """
    A Scene is responsible for the execution of a given game loop.
    """
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
        """
        The start function is called once whenever the scene is entered.
        If an exception occurs in this function
        """
        pass

    def step(self):
        """
        The step function is called at each frame of the main loop.
        """
        pass

    def stop(self):
        """
        The stop function is called when the scene is left.
        """
        pass

    @staticmethod
    def change_scene(new_scene):
        """
        Stops the current scene and initializes the new scene given.
        :param new_scene: The class of the new scene to be initialized.
        :raises SceneChangedException: Only if Scene.scene is not None. Indicates to the main loop that the scene has
         changed and the loop should be reset.
        """
        prev_scene = Scene.scene
        if prev_scene:
            Scene.scene.stop()
            Scene.scene = None
        scene = new_scene()
        scene.start()

        # The current scene is only changed if scene.start was successful.
        Scene.scene = scene
        if prev_scene:
            raise SceneChangedException
