class Pos:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if type(other) == type(self):
            return Pos(self.x + other.x, self.y + other.y)
        elif type(other) == int:
            self.x += other
            self.y += other
        else:
            raise ValueError("Only integers and other Points may be added!")

    def __mul__(self, other):
        if type(other) == type(self):
            self.x *= other.x
            self.y *= other.y
        elif type(other) == int:
            self.x *= other
            self.y *= other
        else:
            raise ValueError("Only integers and other Points may be multiplied!")

    def __sub__(self, other):
        if type(other) == type(self):
            self.x -= other.x
            self.y -= other.y
        elif type(other) == int:
            self.x -= other
            self.y -= other
        else:
            raise ValueError("Only integers and other Points may be subtracted!")

    def __eq__(self, other):
        if type(other) == type(self):
            return self.x == other.x and self.y == other.y
        else:
            raise ValueError("Invalid comparison!")

    def __repr__(self):
        return f"Pos({self.x}, {self.y})"


class Directions:
    N = Pos(0, -1)
    S = Pos(0, 1)
    W = Pos(-1, 0)
    E = Pos(1, 0)
    NW = Pos(-1, -1)
    NE = Pos(1, -1)
    SW = Pos(-1, 1)
    SE = Pos(1, 1)
    NONE = Pos(0, 0)
    CARDINAL = [N, S, E, W]
    ALL = [N, S, E, W, NE, NW, SE, SW, NONE]
