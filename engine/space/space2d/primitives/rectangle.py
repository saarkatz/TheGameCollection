"""
Rectangle is a basic 2D primitive consisting of only a transform and a
size.
"""
from engine.space.space2d.base_member2d import BaseMember2D
from engine.space.space2d.transform import Transform
from engine.space.space2d.vector import Vector


class Rectangle(BaseMember2D):
    def __init__(self, space):
        super().__init__(space)
        self.transform = Transform()
        self.size = Vector.one()
