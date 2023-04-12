import functools

import numpy as np


class Life:
    def __init__(self, width=5, height=4):
        self.width = width
        self.height = height
        self.life = np.random.randint(2, size=(height, width))
        self.run_game()

    def count_neighbours(self, x, y):
        neighbours_sum = 0
        if x - 1 > 0:
            neighbours_sum += self.life[y, x - 1]
            if y - 1 > 0:
                neighbours_sum += self.life[y - 1, x - 1]
            if y + 1 < self.height:
                neighbours_sum += self.life[y + 1, x - 1]
        if x + 1 < self.width:
            neighbours_sum += self.life[y, x + 1]
            if y - 1 > 0:
                neighbours_sum += self.life[y - 1, x + 1]
            if y + 1 < self.height:
                neighbours_sum += self.life[y + 1, x + 1]
        if y - 1 > 0:
            neighbours_sum += self.life[y - 1, x]
        if y + 1 < self.height:
            neighbours_sum += self.life[y + 1, x]
        return neighbours_sum

    def turn(self):
        for i in range(self.height):
            for j in range(self.width):
                current_neighbours = self.count_neighbours(j, i)
                if current_neighbours < 2 or current_neighbours > 3:
                    self.life[i, j] = 0
                elif current_neighbours == 3:
                    self.life[i, j] = 1
        self.show_board()

    def show_board(self):
        print(self.life)

    def run_game(self):
        self.show_board()
        for i in range(100):
            self.turn()
            if functools.reduce(lambda a, b: a + b, list(self.life.flat), 0) == 0:
                break


my_life = Life()
