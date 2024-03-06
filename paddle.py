import pygame as pg
import settings as sets

class Paddle:
    '''the paddle class handles all the movements and collisions of the paddle'''
    def __init__(self, game):
        self.game = game
        self.pos = [600, 650]

    def update(self, movement=(0, 0), paddle_size=200):
        self.pos[0] += (movement[1] - movement[0]) * 5
        if self.pos[0] < 0:
            self.pos[0] = 0
        if self.pos[0] + paddle_size > sets.GAME_WINDOW_WIDTH:
            self.pos[0] = sets.GAME_WINDOW_WIDTH - paddle_size

    def render(self, surf):
        surf.blit(self.game.game_assets['paddle'][1], self.pos)