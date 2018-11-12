import random

from engine.array2D import Array2D
from engine.pos import Pos
from engine.tile import Tile, TileType
from engine.fov import Fov


class Stage:
    def __init__(self, width, height, rooms = None):
        self.width = width
        self.height = height
        self.fov = Fov(self, 16)
        self.spawnPositions = []
        self.rooms = rooms

        self.tiles = Array2D(self.width, self.height)
        self.actors = Array2D(self.width, self.height)
    
    def fillSpawnPositions(self):
        for x in range(self.width):
            for y in range(self.height):
                pos = Pos(x, y)
                if self.getTile(pos).walkable:
                    self.spawnPositions.append(pos)
    
    def getSpawnPosition(self):
        pos = random.choice(self.spawnPositions)
        self.spawnPositions.remove(pos)
        self.setVisible(pos, True)
        return pos

    def addActor(self, actor):
        if not self.actors[actor.pos]:
            self.actors[actor.pos] = actor

    def moveActor(self, actor, direction: Pos):
        if self.actors[actor.pos]:
            self.actors[actor.pos] = None
            self.actors[actor.pos + direction] = actor
    
    def getActorAt(self, pos):
        return self.actors[pos]

    def getTile(self, pos: Pos) -> TileType:
        return self.tiles[pos].type

    def setTile(self, pos: Pos, tType: TileType):
        self.tiles[pos] = Tile(pos, tType)

    def setVisible(self, pos, visible):
        self.tiles[pos].setVisible(visible)
        if self.actors[pos]:
            self.actors[pos].setVisible(visible)

    def refreshFov(self, pos):
        self.fov.refresh(pos)

    def draw(self, surface):
        for x in range(self.width):
            for y in range(self.height):
                pos = Pos(x, y)
                self.tiles[pos].draw(surface)
                if self.actors[pos]:
                    self.actors[pos].draw(surface)
