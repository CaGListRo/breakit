import pygame as pg
import settings as sets
from random import choice

class Ball():
    '''this is the ball class. it should handle the movement and the collisions of the ball'''
    def __init__(self, image, paddle, bricks):
        self.image = image
        self.paddle = paddle
        self.bricks = bricks

        self.rect = self.image.get_rect(midbottom=paddle.rect.midtop)
        self.old_rect = self.rect.copy()
        self.pos = pg.math.Vector2(self.rect.topleft)
        self.direction = pg.math.Vector2((choice((-1, 1)), -1))
        print(self.pos)

        self.speed = 10
        self.active = False

    def handle_vertical_brick_collision(self):
        for i, brick in enumerate(self.bricks.brick_rects):
            if self.rect.colliderect(brick):
                print(self.rect.top, brick.bottom, self.old_rect.top)
                if self.rect.top <= brick.bottom and self.old_rect.top > brick.bottom:
                    print('true')
                    # y = self.bricks.brick_list[i][1] + 48
                    # self.pos = (self.pos[0], y)
                    self.rect.topleft = self.pos
                    self.direction.y *= -1
                    self.bricks.brick_list[i][2] -= 1

    def handle_horizontal_brick_collision(self):
        pass

    def handle_paddle_collision(self):
        if self.rect.colliderect(self.paddle.rect):
            # self.pos = self.rect.topleft
            self.direction.y *= -1            

    def handle_wall_collisions(self):
        if self.rect.left < 0:
            self.rect.left = 0
            self.pos = pg.math.Vector2(self.rect.topleft)
            self.direction.x *= -1

        if self.rect.right > sets.GAME_WINDOW_WIDTH:
            self.rect.right = sets.GAME_WINDOW_WIDTH
            self.pos = pg.math.Vector2(self.rect.topleft)
            self.direction.x *= -1

        if self.rect.top < 0:
            self.rect.top = 0
            self.pos = pg.math.Vector2(self.rect.topleft)
            self.direction.y *= -1

    def update(self):
        
        if self.active:
            print(f"vor {self.rect, self.old_rect}")
            self.old_rect = self.rect.copy()
            print(f"nach {self.rect, self.old_rect}")
            self.pos.x += self.direction.x * self.speed
            self.handle_vertical_brick_collision()
            self.pos.y += self.direction.y * self.speed
            self.handle_horizontal_brick_collision()
            self.rect.topleft = self.pos
            self.handle_wall_collisions()
            self.handle_paddle_collision()
            print(f"ganz nach {self.rect, self.old_rect}")
        else:
            self.rect.midbottom = self.paddle.rect.midtop
            self.pos = pg.math.Vector2(self.rect.topleft)


    def render(self, surf):
        surf.blit(self.image, self.pos)