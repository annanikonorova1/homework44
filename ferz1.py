import random
from copy import copy


class FerziBoard:
    def __init__(self, length: int):
        self.length = length
        self.board = []
        self.all_variants = []
        self._place_next_ferz(0)

    def _can_we_place(self, row: int, num: int):
        for i, value in enumerate(self.board):
            if value == num or (i - row) == (value - num) or (i - row) == (num - value):
                return False
        return True

    def _place_next_ferz(self, row: int):
        if row == self.length:
            self.all_variants.append(copy(self.board))
        else:
            for col in range(self.length):
                if self._can_we_place(row, col):
                    self.board.append(col)
                    self._place_next_ferz(row + 1)
                    self.board.pop()