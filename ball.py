import pygame as pg
import settings as sets

class Ball:
    '''this is the ball class. it should handle the movement and the collisions of the ball'''
    def __init__(self, image, paddle):
        self.image = image
        self.paddle = paddle
        self.pos = (679, 608)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.active = False

    def handle_collisions(self): 
        if self.rect.left < 0:
            pass

    def update(self):
        if self.active:
            self.handle_collisions()
        else:
            self.rect.midbottom = self.paddle.rect.midtop

    def render(self, surf):
        surf.blit(self.image, self.pos)