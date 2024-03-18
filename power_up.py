import pygame as pg

import settings as sets

from random import randint



class PowerUp:
    def __init__(self, game, pos, img_number):
        self.game = game
        self.pos = list(pos)
        self.image = game.game_assets['pwr_ups'][img_number]
        self.rect = self.image.get_rect(midtop=self.pos)
        self.game.power_up_rects.append([self.rect, img_number])

    def update(self):
        self.pos[1] += 2
        self.rect.midtop = self.pos

    def render(self, surf):
        surf.blit(self.image, (self.pos))