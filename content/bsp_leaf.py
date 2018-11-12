import random
from .room import Room


class Leaf:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.minSize = 10
        self.child1 = None
        self.child2 = None
        self.room = None

    def split(self) -> bool:
        if self.child1 is not None or self.child2 is not None:
            return False
        splitH = random.choice([True, False])
        if self.width / self.height >= 1.25:
            splitH = False
        if self.height / self.width >= 1.25:
            splitH = True

        if splitH:
            maxSplitSize = self.height - self.minSize
        else:
            maxSplitSize = self.width - self.minSize

        if maxSplitSize <= self.minSize:
            return False

        split = random.randint(self.minSize, maxSplitSize)

        if splitH:
            self.child1 = Leaf(self.x, self.y, self.width, split)
            self.child2 = Leaf(self.x, self.y + split, self.width, self.height - split)
        else:
            self.child1 = Leaf(self.x, self.y, split, self.height)
            self.child2 = Leaf(self.x + split, self.y, self.width - split, self.height)

        return True

    def createRooms(self, dungeon):
        if self.child1 or self.child2:
            if self.child1:
                self.child1.createRooms(dungeon)
            if self.child2:
                self.child2.createRooms(dungeon)

            if self.child1 and self.child2:
                dungeon.connect(self.child1.getRoom(), self.child2.getRoom())

        else:
            w = random.randint(
                dungeon.minRoomSize, min(dungeon.maxRoomSize, self.width - 1)
            )
            h = random.randint(
                dungeon.minRoomSize, min(dungeon.maxRoomSize, self.height - 1)
            )
            x = random.randint(self.x, self.x + (self.width - 1) - w)
            y = random.randint(self.y, self.y + (self.height - 1) - h)
            self.room = Room(x, y, w, h)
            dungeon.createRoom(self.room)

    def getRoom(self):
        if self.room:
            return self.room
        else:
            if self.child1:
                self.room1 = self.child1.getRoom()
            if self.child2:
                self.room2 = self.child2.getRoom()

            if not self.child1 and not self.child2:
                return None
            elif not self.room2:
                return self.room1
            elif not self.room1:
                return self.room2
            elif random.random() < 0.5:
                return self.room1
            else:
                return self.room2
