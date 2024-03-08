import pygame as pg
import settings as sets
from random import choice

class Ball():
    '''this is the ball class. it should handle the movement and the collisions of the ball'''
    def __init__(self, image, paddle):
        self.image = image
        self.paddle = paddle

        self.rect = self.image.get_rect(midbottom=paddle.rect.midtop)
        self.old_rect = self.rect.copy()
        self.pos = pg.math.Vector2(self.rect.topleft)
        self.direction = pg.math.Vector2((choice((-1, 1)), -1))

        self.speed = 10
        self.active = False

    def handle_paddle_collision(self):
        if self.rect.colliderect(self.paddle.rect):
            # self.pos = self.rect.topleft
            self.direction.y *= -1
            print('top')
            

    def handle_wall_collisions(self): 
        if self.rect.left < 0:
            self.rect.left = 0
            self.pos = self.rect.topleft
            self.direction.x *= -1

        if self.rect.right > sets.GAME_WINDOW_WIDTH:
            self.rect.right = sets.GAME_WINDOW_WIDTH
            self.pos = self.rect.topleft
            self.direction.x *= -1

        if self.rect.top < 0:
            self.rect.top = 0
            self.pos = self.rect.topleft
            self.direction.y *= -1

    def update(self):
        if self.active:
            self.old_rect = self.rect.copy()
            x = self.pos[0] + self.direction.x * self.speed
            y = self.pos[1] + self.direction.y * self.speed
            self.pos = (x, y)
            self.rect.topleft = self.pos
            self.handle_wall_collisions()
            self.handle_paddle_collision()
        else:
            self.rect.midbottom = self.paddle.rect.midtop
            self.pos = self.rect.topleft

    def render(self, surf):
        surf.blit(self.image, self.pos)