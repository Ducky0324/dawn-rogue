from engine.pos import Pos


class Room:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.x2 = x + w
        self.y2 = y + h

    def getCenter(self) -> Pos:
        centerx = (self.x + self.x2) // 2
        centery = (self.y + self.y2) // 2
        return Pos(centerx, centery)

    def intersects(self, other):
        return (
            self.x <= other.x2
            and self.x2 >= other.x
            and self.y <= other.y2
            and self.y2 >= other.y
        )
    
    def __repr__(self):
        return f"Room({self.x}, {self.y}, {self.x2}, {self.y2})"
    

