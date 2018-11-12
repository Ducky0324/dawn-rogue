import math
from engine.pos import Pos


class Fov:
    def __init__(self, stage, radius: int = 10):
        self.stage = stage
        self.radius = radius
        self.fovCache = set()

    def refresh(self, pos):
        for tile in self.fovCache:
            self.stage.setVisible(Pos(tile[0], tile[1]), False)
        self.fovCache.clear()
        for i in range(0, 360):
            x = math.cos(float(i * 0.01745))
            y = math.sin(float(i * 0.01745))
            self.calcFov(pos, x, y)

    def calcFov(self, pos, x, y):
        ox = float(pos.x + 0.5)
        oy = float(pos.y + 0.5)
        if self.radius == -1:
            while True:
                p = Pos(int(ox), int(oy))
                self.fovCache.add((p.x, p.y))
                self.stage.setVisible(p, True)
                if not self.stage.getTile(p).walkable:
                    return
                ox += x
                oy += y
        else:
            for i in range(self.radius):
                p = Pos(int(ox), int(oy))
                self.fovCache.add((p.x, p.y))
                self.stage.setVisible(p, True)
                if not self.stage.getTile(p).walkable:
                    return
                ox += x
                oy += y
