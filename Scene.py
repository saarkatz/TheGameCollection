

# Interface for scene object.
# TODO: Change the scene to be more managed by the main loop
class Scene:
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
