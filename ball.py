import pygame as pg
import settings as sets
from power_up import PowerUp
from random import choice, randint

class Ball():
    '''this is the ball class. it should handle the movement and the collisions of the ball'''
    def __init__(self, game, image, paddle, bricks):
        self.game = game
        self.image = image
        self.paddle = paddle
        self.bricks = bricks

        self.rect = self.image.get_rect(midbottom=paddle.rect.midtop)
        self.old_rect = self.rect.copy()
        self.pos = pg.math.Vector2(self.rect.topleft)
        self.direction = pg.math.Vector2((choice((-1, 1)), -1))

        self.speed = 5
        self.active = False

    def handle_death(self):
        if self.rect.top > sets.GAME_WINDOW_HEIGHT:
            self.active = False
            self.direction = pg.math.Vector2((1, -1))
            self.game.extra_lives -= 1

    def handle_vertical_brick_collision(self):
        for i, brick in enumerate(self.bricks.brick_rects):
            if self.rect.colliderect(brick):
                if self.direction.y > 0 and self.old_rect.top > brick.bottom:
                    self.rect.bottom = brick.top - 1
                elif self.direction.y < 0 and self.old_rect.bottom < brick.top:
                    self.rect.top = brick.bottom + 1
                self.pos = pg.math.Vector2(self.rect.topleft)
                self.direction.y *= -1
                self.bricks.brick_list[i][2] -= 1
                self.game.score += 5

                if self.bricks.brick_list[i][2] == 0:
                    if randint(1, 100) > 80:
                        pwr_up_number = randint(0, 6)
                        self.game.power_ups.append(PowerUp(self.game, (self.bricks.brick_list[i][0] + 30, self.bricks.brick_list[i][1]), pwr_up_number))
                    del self.bricks.brick_list[i]
                    del self.bricks.brick_rects[i]
                    self.game.score += 10

    def handle_horizontal_brick_collision(self):
        for i, brick in enumerate(self.bricks.brick_rects):
            if self.rect.colliderect(brick):
                if self.direction.x > 0 and self.old_rect.left > brick.right:
                    self.rect.right = brick.left - 1
                elif self.direction.x < 0 and self.old_rect.right < brick.left:
                    self.rect.left = brick.right + 1
                self.pos = pg.math.Vector2(self.rect.topleft)
                self.direction.x *= -1
                self.bricks.brick_list[i][2] -= 1
                self.game.score += 5

                if self.bricks.brick_list[i][2] == 0:
                    if randint(1, 100) > 80:
                        pwr_up_number = randint(0, 6)
                        self.game.power_ups.append(PowerUp(self.game, (self.bricks.brick_list[i][0] + 30, self.bricks.brick_list[i][1]), pwr_up_number))
                    del self.bricks.brick_list[i]
                    del self.bricks.brick_rects[i]
                    self.game.score += 10

    def handle_paddle_collision(self):
        if self.rect.colliderect(self.paddle.rect):
            self.direction.y *= -1  
            self.paddle.top = self.rect.bottom
            self.pos = pg.math.Vector2(self.rect.topleft)
                      
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
            self.handle_death()
            self.handle_vertical_brick_collision()
            self.handle_horizontal_brick_collision()
            self.handle_wall_collisions()
            self.handle_paddle_collision()
            
        else:
            self.rect.midbottom = self.paddle.rect.midtop
            self.pos = pg.math.Vector2(self.rect.topleft)


    def render(self, surf):
        surf.blit(self.image, self.pos)