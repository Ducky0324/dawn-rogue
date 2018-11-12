from actors import Actor
from engine.pos import Pos
from actions import ActionResult
import pygame as pg


class Monster(Actor):
    def __init__(self, symbol, color):
        super().__init__(symbol, color, Pos(0, 0))

    def getNextAction(self):
        return ActionResult(True)


class Monsters:
    orc = Monster("o", "red")
