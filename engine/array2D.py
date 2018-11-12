from engine.pos import Pos


class Array2D:
    def __init__(self, cols, rows):
        self.rows = rows
        self.cols = cols
        self.array = [[None for _ in range(cols)] for y in range(rows)]

    def __getitem__(self, index: Pos):
        return self.array[index.y][index.x]

    def __setitem__(self, index: Pos, val):
        self.array[index.y][index.x] = val

    def __repr__(self):
        for row in range(self.rows):
            print(self.array[row])
        return ""
