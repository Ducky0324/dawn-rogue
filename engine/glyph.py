import pygame as pg
from os import path

from engine.pos import Pos

FONT_DIR = path.join(path.abspath("."), "fonts")
if not pg.font.get_init():
    pg.font.init()

print("loading font!")
DEFAULT_FONT = pg.font.Font(path.join(FONT_DIR, "PressStart2P.ttf"), 16)


class Glyph:
    SIZE = 16

    def __init__(self, color: str, symbol: str):
        if symbol == ' ':
            self.glyph = DEFAULT_FONT.render(' ', True, pg.Color(color), pg.Color(color))
        else:
            self.glyph = DEFAULT_FONT.render(
                symbol, True, pg.Color(color), pg.Color("black")
            )
        self.glyph = pg.transform.scale(self.glyph, (self.SIZE, self.SIZE))
        self.rect = self.glyph.get_rect()

    def setPos(self, pos: Pos):
        self.rect.x = pos.x * self.SIZE
        self.rect.y = pos.y * self.SIZE

    def draw(self, surface: pg.Surface):
        surface.blit(self.glyph, self.rect)
