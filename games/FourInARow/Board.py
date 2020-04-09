"""
The model of the four in a row game
"""


class Board:
    def __init__(self):
        self.stage = [[0] * 6 for _ in range(7)]
        self.column = [0 for _ in range(7)]

    def get_size(self, dim):
        if dim == 0:
            return 7
        else:
            return 6

    def __getitem__(self, item):
        assert 2 == len(item)
        return self.stage[item[0]][item[1]]

    def __setitem__(self, key, value):
        assert 2 == len(key)
        self.stage[key[0]][key[1]] = value

    def set_column(self, player, column):
        if self.column[column] < self.get_size(1):
            self.stage[column][self.column[column]] = player
            self.column[column] += 1
            return True
        else:
            return False
