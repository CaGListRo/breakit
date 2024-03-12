import pygame as pg

import settings as sets

from random import randint



class PowerUp:
    def __init__(self, game, pos):
        self.game = game
        self.pos = list(pos)
        self.image = game.game_assets['pwr_ups'][randint(0, 4)]

    def update(self):
        self.pos[1] += 1

        if self.pos[1] >= sets.GAME_WINDOW_HEIGHT + 100:
            self.game.power_ups.remove(self)

    def render(self, surf):
        surf.blit(self.image, (self.pos))