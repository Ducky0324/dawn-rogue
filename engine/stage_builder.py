from engine.stage import Stage
from engine.tile import Tiles
from engine.pos import Pos


class StageBuilder:
    def __init__(self, game):
        self.width = game.surf.get_width() // 16
        self.height = game.surf.get_height() // 16
        self.stage = Stage(self.width, self.height)

        self.rooms = set()

    def generate(self) -> Stage:
        self.fill(Tiles.wall)
        for y in range(1, self.stage.height - 1):
            for x in range(1, self.stage.width - 1):
                p = Pos(x, y)
                self.stage.setTile(p, Tiles.floor)
        return self.stage

    def fill(self, tType):
        for x in range(self.stage.width):
            for y in range(self.stage.height):
                p = Pos(x, y)
                self.stage.setTile(p, tType)
