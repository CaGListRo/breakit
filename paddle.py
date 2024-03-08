import pygame as pg
import settings as sets

class Paddle:
    '''the paddle class handles all the movements and collisions of the paddle'''
    def __init__(self, game, image):
        self.game = game
        self.image = image
        self.pos = [600, 650]
        self.rect = self.image.get_rect(topleft=self.pos)
        

    def update(self, movement=(0, 0), paddle_size=200):
        self.pos[0] += (movement[1] - movement[0]) * 10
        self.rect.topleft = self.pos
        if self.pos[0] < 0:
            self.pos[0] = 0
        if self.pos[0] + paddle_size > sets.GAME_WINDOW_WIDTH:
            self.pos[0] = sets.GAME_WINDOW_WIDTH - paddle_size

    def render(self, surf):
        surf.blit(self.image, self.pos)