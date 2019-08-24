from engine.space.space2d.base_member2d import BaseMember2D


class Space2D:
    def __init__(self):
        self.members = []

    def add(self, member: BaseMember2D):
        self.members.append(member)
