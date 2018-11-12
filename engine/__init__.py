import pygame as pg

from engine.game import Game


class Engine:
    def __init__(self, title, winWidth):
        # These class variables will be useful for positioning GUI
        self.winWidth = winWidth
        self.winHeight = self.winWidth * 9 // 16

        # initialize pygame
        pg.init()
        pg.font.init()
        pg.key.set_repeat(100, 100)

        pg.display.set_caption(title)
        self.window = pg.display.set_mode((self.winWidth, self.winHeight))
        self.window.fill((51, 51, 51))
        self.clock = pg.time.Clock()

        self.game = Game(self)
        self.running = True

    def start(self):
        while self.running:
            self.clock.tick(60)
            pg.display.set_caption(f"dawn-rpg       fps: {self.clock.get_fps():.2f}")
            self.handleEvents()
            self.update()
            self.render()

    def handleEvents(self):
        if self.game.gameOver:
            self.running = False
        self.game.handle_events()

    def update(self):
        self.game.update()

    def render(self):
        self.game.draw(self)
        pg.display.flip()
