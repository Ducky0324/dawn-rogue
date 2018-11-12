import pygame as pg
from content.dungeon_generator import DungeonGenerator
from content.mob_spawner import MobSpawner
from engine.pos import Pos, Directions
from actors.hero import Hero
from actions import Walk


class Game:
    def __init__(self, engine):
        self.engine = engine
        self.surf = pg.Surface((self.engine.winHeight * 1.33, self.engine.winHeight))
        self.gameOver = False

        self.currentActor = 0
        self.currentDepth = 1

        self.player = Hero(Pos(1, 1))
        self.player.isVisible = True

        self.actors = [self.player]
        self.stageGenerator = DungeonGenerator(self)
        self.stage = self.stageGenerator.generate()

        self.mobSpawner = MobSpawner(self, self.stage)
        self.mobSpawner.populateStage()

        self.player.setPos(self.stage.getSpawnPosition())
        self.stage.addActor(self.player)
        self.stage.refreshFov(self.player.pos)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.gameOver = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.gameOver = True
                if event.key == pg.K_w:
                    self.player.setNextAction(
                        Walk(self.player, self.stage, Directions.N)
                    )
                    self.stage.refreshFov(self.player.pos)
                if event.key == pg.K_a:
                    self.player.setNextAction(
                        Walk(self.player, self.stage, Directions.W)
                    )
                    self.stage.refreshFov(self.player.pos)
                if event.key == pg.K_s:
                    self.player.setNextAction(
                        Walk(self.player, self.stage, Directions.S)
                    )
                    self.stage.refreshFov(self.player.pos)
                if event.key == pg.K_d:
                    self.player.setNextAction(
                        Walk(self.player, self.stage, Directions.E)
                    )
                    self.stage.refreshFov(self.player.pos)

    def update(self):
        action = self.actors[self.currentActor].getNextAction()
        if action is None:
            self.currentActor = (self.currentActor + 1) % len(self.actors)
            return
        result = action.perform()
        if result.result:
            result.do()
        self.currentActor = (self.currentActor + 1) % len(self.actors)

    def draw(self, engine):
        self.surf.fill(pg.Color("black"))
        self.stage.draw(self.surf)
        self.engine.window.blit(self.surf, (0, 0))
