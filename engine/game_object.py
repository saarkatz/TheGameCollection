from engine.space2d import vector


class GameObject:
    def __init__(self):
        self.children = []
        self.components = []
