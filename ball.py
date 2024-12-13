import pygame as pg
import settings as sets
from power_up import PowerUp
from random import choice, randint

from typing import TypeVar

Game = TypeVar("Game")
Paddle = TypeVar("Paddle")
Bricks = TypeVar("Bricks")

class Ball():
    """this is the ball class. it should handle the movement and the collisions of the ball"""
    def __init__(self, game: Game, image: pg.Surface, paddle: Paddle, bricks: Bricks) -> None:
        """
        Initializes the ball object.
        Args:
        game (Game): the game object
        image (pg.Surface): the image of the ball
        paddle (Paddle): the paddle object
        bricks (Bricks): the bricks object
        """
        self.game = game
        self.image = image
        self.paddle = paddle
        self.bricks = bricks

        self.rect = self.image.get_rect(midbottom=paddle.rect.midtop)
        self.old_rect = self.rect.copy()
        self.pos = pg.Vector2(self.rect.topleft)
        self.direction = pg.Vector2((choice((-1, 1)), -1))

        self.speed = 5
        self.active = False

    def handle_death(self) -> None:
        """ Handles the death of the ball. """
        if self.rect.top > sets.GAME_WINDOW_HEIGHT:
            self.active = False
            self.direction = pg.Vector2((1, -1))
            self.game.extra_lives -= 1

    def handle_vertical_brick_collision(self) -> None:
        """ Handles the vertical collision with a brick. """
        for i, brick in enumerate(self.bricks.brick_rects):
            if self.rect.colliderect(brick):
                if self.direction.y > 0 and self.old_rect.top > brick.bottom:
                    self.rect.bottom = brick.top - 1
                elif self.direction.y < 0 and self.old_rect.bottom < brick.top:
                    self.rect.top = brick.bottom + 1
                self.pos = pg.Vector2(self.rect.topleft)
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

    def handle_horizontal_brick_collision(self) -> None:
        """ Handles the horizontal collision with a brick. """
        for i, brick in enumerate(self.bricks.brick_rects):
            if self.rect.colliderect(brick):
                if self.direction.x > 0 and self.old_rect.left > brick.right:
                    self.rect.right = brick.left - 1
                elif self.direction.x < 0 and self.old_rect.right < brick.left:
                    self.rect.left = brick.right + 1
                self.pos = pg.Vector2(self.rect.topleft)
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

    def handle_paddle_collision(self) -> None:
        """ Handles the collision with the paddle. """
        if self.rect.colliderect(self.paddle.rect):
            self.direction.y *= -1  
            self.paddle.top = self.rect.bottom
            self.pos = pg.Vector2(self.rect.topleft)
                      
    def handle_wall_collisions(self) -> None:
        """ Handles the collision with the walls. """
        if self.rect.left < 0:
            self.rect.left = 0
            self.pos = pg.Vector2(self.rect.topleft)
            self.direction.x *= -1

        if self.rect.right > sets.GAME_WINDOW_WIDTH:
            self.rect.right = sets.GAME_WINDOW_WIDTH
            self.pos = pg.Vector2(self.rect.topleft)
            self.direction.x *= -1

        if self.rect.top < 0:
            self.rect.top = 0
            self.pos = pg.Vector2(self.rect.topleft)
            self.direction.y *= -1

    def update(self) -> None:
        """ Updates the ball's position and calls collision handling methods. """
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
            self.pos = pg.Vector2(self.rect.topleft)

    def render(self, surf: pg.Surface) -> None:
        """
        Renders the ball onto the given surface.
        Args:
        surf (pg.Surface): The surface to render the ball onto.
        """
        surf.blit(self.image, self.pos)