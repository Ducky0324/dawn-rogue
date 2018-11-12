import pygame as pg

from engine.glyph import Glyph
from engine.pos import Pos


class Actor:
    def __init__(self, symbol: str, color: str, pos: Pos):
        self.glyph = Glyph(color, symbol)
        self.glyph.setPos(pos)
        self.pos = pos

        self.isVisible = False
        self.nextAction = None

    def setNextAction(self, action):
        self.nextAction = action

    def getNextAction(self):
        action = self.nextAction
        self.nextAction = None
        return action

    def setVisible(self, visible):
        self.isVisible = visible

    def setPos(self, pos: Pos):
        self.glyph.setPos(pos)
        self.pos = pos

    def move(self, direction: Pos):
        self.pos = self.pos + direction
        self.glyph.setPos(self.pos)

    def draw(self, surface: pg.Surface):
        if self.isVisible:
            self.glyph.draw(surface)
