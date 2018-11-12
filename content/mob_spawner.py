import random
from actors.monster import Monster, Monsters

from engine.stage import Stage


class MobSpawner:
    def __init__(self, game, stage: Stage):
        self.game = game
        self.stage = stage

    def populateStage(self):
        spawnChance = 0.3 + self.game.currentDepth / 30
        for c in range(self.game.currentDepth * 10):
            choice = random.random()
            if choice < spawnChance:
                print("Spawning Monster!")
                monster = Monsters.orc
                monster.setPos(self.stage.getSpawnPosition())
                self.stage.addActor(monster)
                self.game.actors.append(monster)
