import pygame as pg
import settings as sets

class Paddle:
    '''the paddle class handles all the movements and collisions of the paddle'''
    def __init__(self, game, image):
        self.game = game
        self.image = image
        self.rect = self.image.get_rect(midtop=(700, 650))
        self.pos = pg.math.Vector2(self.rect.topleft)
        

    def update(self, movement=(0, 0), paddle_size=200):
        self.pos.x += (movement[1] - movement[0]) * 10
        self.rect.topleft = self.pos
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x + paddle_size > sets.GAME_WINDOW_WIDTH:
            self.pos.x = sets.GAME_WINDOW_WIDTH - paddle_size

    def render(self, surf):
        surf.blit(self.image, self.pos)