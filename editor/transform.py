"""
Transform is responsible for all the spatial meta data an object in the
space would need.
"""
from engine.space2d import Vector


class Transform:
    def __init__(self):
        self.position = Vector.zero()
        self.rotation = 0
        self.scale = Vector.one()
