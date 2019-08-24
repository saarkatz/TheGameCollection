"""
Base Member 2D defines the required structure of members of the 2D
space to establish the desired space-object relationship.
That is, the space should be aware of its members and each member
should be aware of the space it's in.
"""


class BaseMember2D:
    def __init__(self, space):
        self.space = space
        space.add(self)
