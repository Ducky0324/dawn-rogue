import random

from engine.stage_builder import StageBuilder
from content.bsp_leaf import Leaf
from content.room import Room

from engine.pos import Pos, Directions
from engine.tile import Tiles

"""
BSP Dungeon Generation that uses a drunken walk to connect the rooms.
"""


class DungeonGenerator(StageBuilder):
    def __init__(self, game):
        super().__init__(game)
        self.maxRoomSize = 10
        self.minRoomSize = 6
        self.maxLeafSize = 20
        self.smoothEdges = True
        self.smoothing = 1
        self.filling = 3

    def generate(self):
        self.fill(Tiles.wall)
        self.leaves = []
        root = Leaf(0, 0, self.width, self.height)
        self.leaves.append(root)

        splitSuccessfully = True
        while splitSuccessfully:
            splitSuccessfully = False
            for leaf in self.leaves:
                if leaf.child1 is None and leaf.child2 is None:
                    if leaf.width > self.maxLeafSize or leaf.height > self.maxLeafSize:
                        if leaf.split():
                            self.leaves.append(leaf.child1)
                            self.leaves.append(leaf.child2)
                            splitSuccessfully = True

        root.createRooms(self)
        self.cleanUpStage()
        self.stage.fillSpawnPositions()
        self.stage.rooms = self.rooms
        return self.stage

    def createRoom(self, room: Room):
        self.rooms.add(room)
        for x in range(room.x + 1, room.x2):
            for y in range(room.y + 1, room.y2):
                pos = Pos(x, y)
                self.stage.setTile(pos, Tiles.floor)

    def connect(self, room1: Room, room2: Room):
        drunkard = room2.getCenter()
        goal = room1.getCenter()
        while not (room1.x <= drunkard.x <= room1.x2) or not (
            room1.y <= drunkard.y <= room1.y2
        ):
            north = 1.0
            south = 1.0
            east = 1.0
            west = 1.0

            weight = 1

            if drunkard.x < goal.x:
                east += weight
            elif drunkard.x > goal.x:
                west += weight

            if drunkard.y < goal.y:
                south += weight
            elif drunkard.y > goal.y:
                north += weight

            total = north + south + east + west
            north /= total
            south /= total
            east /= total
            west /= total

            choice = random.random()
            d = Pos(0, 0)
            if 0 <= choice < north:
                d = Directions.N
            elif north <= choice < (north + south):
                d = Directions.S
            elif (north + south) <= choice < (north + south + east):
                d = Directions.E
            else:
                d = Directions.W

            if (0 < drunkard.x + d.x < self.width - 1) and (
                0 < drunkard.y + d.y < self.height - 1
            ):
                drunkard += d
                if self.stage.getTile(drunkard) == Tiles.wall:
                    self.stage.setTile(drunkard, Tiles.floor)

    def cleanUpStage(self):
        if self.smoothEdges:
            for i in range(3):
                for x in range(1, self.width - 1):
                    for y in range(1, self.height - 1):
                        pos = Pos(x, y)
                        if (
                            self.stage.getTile(pos) == Tiles.wall
                            and self.getAdjWalls(pos) <= self.smoothing
                        ):
                            self.stage.setTile(pos, Tiles.floor)
                        if (
                            self.stage.getTile(pos) == Tiles.floor
                            and self.getAdjWalls(pos) >= self.filling
                        ):
                            self.stage.setTile(pos, Tiles.wall)

    def getAdjWalls(self, pos: Pos) -> int:
        wallCounter = 0
        for direction in Directions.CARDINAL:
            if self.stage.getTile(pos + direction) == Tiles.wall:
                wallCounter += 1
        return wallCounter
