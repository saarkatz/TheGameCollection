"""
Transform is responsible for all the spatial meta data an object in the space would need.
"""
from engine.space.space2d import Vector


class Transform:
    def __init__(self):
        position = Vector(0, 0)
        rotation = 0
        scale = Vector(0, 0)

