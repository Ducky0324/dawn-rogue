import pygame as pg
from engine.pos import Pos
from engine.glyph import Glyph
from engine.char_codes import CharCodes


class TileType:
    def __init__(
        self, exploredColor: str, visibleColor: str, symbol: str, walkable: bool
    ):
        self.visibleColor = visibleColor
        self.exploredColor = exploredColor
        self.symbol = symbol
        self.walkable = walkable


class Tile:
    def __init__(self, pos: Pos, tileType: TileType):
        self.type = tileType
        self.visible = Glyph(tileType.visibleColor, tileType.symbol)
        self.explored = Glyph(tileType.exploredColor, tileType.symbol)
        self.visible.setPos(pos)
        self.explored.setPos(pos)

        self.isVisible = False
        self.isExplored = False

    def setVisible(self, visible: bool) -> bool:
        self.isVisible = visible

        if self.isVisible and not self.isExplored:
            self.isExplored = True
            return True

        return False

    def draw(self, surface: pg.Surface):
        if self.isExplored:
            if self.isVisible:
                self.visible.draw(surface)
            else:
                self.explored.draw(surface)

    def __repr__(self):
        return f"{self.type.symbol}"


class Tiles:
    floor = TileType("grey12", "grey50", CharCodes.MIDDOT, True)
    wall = TileType("grey10", "goldenrod", "#", False)
    tree1 = TileType("chartreuse4", "chartreuse2", CharCodes.UPWARD_TRIANGLE, False)
    tree2 = TileType("darkgreen", "green3", CharCodes.SPADE_SUIT, False)
    tree3 = TileType("green4", "green3", CharCodes.CLUB_SUIT, False)
    trees = [tree1, tree2, tree3]
