"""
The model of the four in a row game
"""
import random


class Direction:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


def get_direction(direction):
    if direction in (Direction.UP, Direction.LEFT):
        return 0, 1, 4, 1
    else:
        return 3, 2, -1, -1


class Board:
    def __init__(self):
        self.stage = [[0] * 4 for _ in range(4)]

    def get_size(self, dim):
        return 4

    def __getitem__(self, item):
        assert 2 == len(item)
        return self.stage[item[0]][item[1]]

    def __setitem__(self, key, value):
        assert 2 == len(key)
        self.stage[key[0]][key[1]] = value

    def slide_board_left_right(self, direction):
        slided = False
        start, end, step = direction[1:]
        for i in range(self.get_size(1)):
            index = direction[0]
            for j in range(start, end, step):
                if self.stage[j][i] > 0:
                    if self.stage[index][i] == self.stage[j][i]:
                        self.stage[index][i] += 1
                        self.stage[j][i] = 0
                        index += step
                        slided = True
                    elif self.stage[index][i] == 0:
                        self.stage[index][i] = self.stage[j][i]
                        self.stage[j][i] = 0
                        index += step
                        slided = True
                    elif index + step != j:
                        index += step
                        self.stage[index][i] = self.stage[j][i]
                        self.stage[j][i] = 0
                        slided = True
                    else:
                        index += step
        return slided

    def slide_board_up_down(self, direction):
        slided = False
        start, end, step = direction[1:]
        for i in range(self.get_size(0)):
            index = direction[0]
            for j in range(start, end, step):
                if self.stage[i][j] > 0:
                    if self.stage[i][index] == self.stage[i][j]:
                        self.stage[i][index] += 1
                        self.stage[i][j] = 0
                        index += step
                        slided = True
                    elif self.stage[i][index] == 0:
                        self.stage[i][index] = self.stage[i][j]
                        self.stage[i][j] = 0
                        index += step
                        slided = True
                    elif index + step != j:
                        index += step
                        self.stage[i][index] = self.stage[i][j]
                        self.stage[i][j] = 0
                        slided = True
                    else:
                        index += step
        return slided

    def slide_board(self, direction):
        if direction in (Direction.UP, Direction.DOWN):
            return self.slide_board_up_down(get_direction(direction))
        elif direction in (Direction.LEFT, Direction.RIGHT):
            return self.slide_board_left_right(get_direction(direction))

    def generate_empty_positions(self):
        for i in range(self.get_size(0)):
            for j in range(self.get_size(1)):
                if self.stage[i][j] == 0:
                    yield i, j

    def get_empty_positions(self):
        return list(self.generate_empty_positions())

    def add_random(self):
        positions = self.get_empty_positions()
        if not positions:
            return False
        pos = random.choice(positions)
        self.stage[pos[0]][pos[1]] = 1
        return True
