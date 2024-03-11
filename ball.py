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

        self.speed = 5
        self.active = False

    def handle_vertical_brick_collision(self):
        for i, brick in enumerate(self.bricks.brick_rects):
            if self.rect.colliderect(brick):
                if self.direction.y > 0 and self.old_rect.top > brick.bottom:  # Ball bewegt sich nach unten
                    self.rect.bottom = brick.top - 1
                elif self.direction.y < 0 and self.old_rect.bottom < brick.top:  # Ball bewegt sich nach oben
                    self.rect.top = brick.bottom + 1
                self.direction.y *= -1
                self.bricks.brick_list[i][2] -= 1

                if self.bricks.brick_list[i][2] == 0:
                    del self.bricks.brick_list[i]
                    del self.bricks.brick_rects[i]
        # for i, brick in enumerate(self.bricks.brick_rects):
        #     if self.rect.colliderect(brick):
        #         if self.rect.top <= brick.bottom and self.old_rect.top > brick.bottom:
        #             brick.bottom = self.rect.top
        #             self.rect.topleft = self.pos
        #             self.direction.y *= -1
        #             self.bricks.brick_list[i][2] -= 1
        #         if self.rect.bottom >= brick.top and self.old_rect.bottom < brick.top:
        #             brick.top = self.rect.bottom
        #             self.rect.topleft = self.pos
        #             self.direction.y *= -1
        #             self.bricks.brick_list[i][2] -= 1

        #         if self.bricks.brick_list[i][2] == 0:
        #             del self.bricks.brick_list[i]
        #             del self.bricks.brick_rects[i]

    def handle_horizontal_brick_collision(self):
        for i, brick in enumerate(self.bricks.brick_rects):
            if self.rect.colliderect(brick):
                if self.direction.x > 0 and self.old_rect.left > brick.right:  # Ball bewegt sich nach rechts
                    self.rect.right = brick.left - 1
                elif self.direction.x < 0 and self.old_rect.right < brick.left:  # Ball bewegt sich nach links
                    self.rect.left = brick.right + 1
                self.direction.x *= -1
                self.bricks.brick_list[i][2] -= 1

                if self.bricks.brick_list[i][2] == 0:
                    del self.bricks.brick_list[i]
                    del self.bricks.brick_rects[i]
        # for i, brick in enumerate(self.bricks.brick_rects):
        #     if self.rect.colliderect(brick):
        #         if self.rect.left <= brick.right and self.old_rect.left > brick.right:
        #             brick.right = self.rect.left
        #             self.rect.topleft = self.pos
        #             self.direction.x *= -1
        #             self.bricks.brick_list[i][2] -= 1
        #         if self.rect.right >= brick.left and self.old_rect.right < brick.left:
        #             brick.left = self.rect.right
        #             self.rect.topleft = self.pos
        #             self.direction.x *= -1
        #             self.bricks.brick_list[i][2] -= 1

        #         if self.bricks.brick_list[i][2] == 0:
        #             del self.bricks.brick_list[i]
        #             del self.bricks.brick_rects[i]

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
            self.old_rect = self.rect.copy()
            self.pos.x += self.direction.x * self.speed
            self.pos.y += self.direction.y * self.speed  
            self.rect.topleft = self.pos
            self.handle_vertical_brick_collision()
            self.handle_horizontal_brick_collision()
            self.handle_wall_collisions()
            self.handle_paddle_collision()
        else:
            self.rect.midbottom = self.paddle.rect.midtop
            self.pos = pg.math.Vector2(self.rect.topleft)


    def render(self, surf):
        surf.blit(self.image, self.pos)