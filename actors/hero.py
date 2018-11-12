from actors import Actor
from engine.pos import Pos


class Hero(Actor):
    def __init__(self, pos: Pos):
        super().__init__("@", "green", pos)

