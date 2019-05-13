from CallbackProperty import make_callback
import pygame
from Screen import Screen
from SceneChangedException import SceneChangedException


# Interface for scene object.
# TODO: Change the scene to be more managed by the main loop
@make_callback('caption', lambda value: pygame.display.set_caption(value))
@make_callback('resolution', lambda value: Screen.set_screen(pygame.display.set_mode(value)))
class Scene:
    """
    A Scene is responsible for the execution of a given game loop.
    """
    scene = None

    def __init__(self, caption, resolution):
        self._init_caption()
        self._init_resolution()

        self.caption = caption
        self.resolution = resolution

    def on_resolution_change(self):
        Screen.screen = pygame.display.set_mode(self.get_resolution())

    def start(self):
        """
        The start function is called once whenever the scene is entered.
        If an exception occurs in this function
        """
        # TODO: Finish the documentation here
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
