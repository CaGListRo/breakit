# this is a breakout clone
import pygame as pg

from ball import Ball
from brick import Brick
from paddle import Paddle
from utilities import load_image, load_images
import settings as sets

from random import randint
from typing import Final


class Game:
    """This is the game class, here is the main-loop located in the play-method"""
    FPS: Final[int] = 60
    SCORE_FONT: Final[pg.font.Font] = pg.font.SysFont("comicsans", 42)
    GAME_OVER_FONT: Final[pg.font.Font] = pg.font.SysFont("comicsans", 142)

    def __init__(self) -> None:
        """ Initializes the game class. """
        pg.init()
        self.main_window: pg.display = pg.display.set_mode((sets.MAIN_WINDOW_WIDTH, sets.MAIN_WINDOW_HEIGHT))
        self.game_window: pg.Surface = pg.Surface((sets.GAME_WINDOW_WIDTH, sets.GAME_WINDOW_HEIGHT))
        self.running: bool = True
        self.clock: pg.time.Clock = pg.time.Clock()
          
        self.game_assets: dict[pg.Surface] = {
            "background":load_images(path="backgrounds"),
            "main_background": load_image(path="main background", img_name="space.png"),
            "ball": load_image(path="ball", img_name="ball.png"),
            "bricks": load_images(path="bricks"),
            "paddle": load_images(path="paddle"),
            "pwr_ups": load_images(path="power ups")
        }

        self.score: int = 0
        self.level: int = 1
        self.extra_lives: int = 2
        self.movement: list[bool] = [False, False]
        self.paddle: Paddle = Paddle(self, self.game_assets["paddle"][1])
        self.create_brick_pattern()
        self.ball: Ball = Ball(self, self.game_assets["ball"], self.paddle, self.brick_pattern)
        self.background_number: int = randint(0, 7)
        self.power_ups: list[pg.Surface] = []
        self.power_up_rects: list[pg.Rect] = []
    
    def level_complete(self) -> None:
        """ Brings the player to the next level. """
        self.ball.active = False
        self.level += 1
        self.create_brick_pattern()

    def game_over(self) -> None:
        """ Closes the game. """
        self.ball.active = False
        self.running = False

    def create_brick_pattern(self) -> None:
        """ Creates the brick pattern. """
        self.brick_pattern = Brick(self, self.level)

    def handle_power_ups(self) -> None:
        """ Updates the power ups and deletes them when they are of screen. """
        for i, pwr_up in enumerate(self.power_ups):
            pwr_up.update()
            if pwr_up.rect.top > sets.GAME_WINDOW_HEIGHT:
                self.power_ups.pop(i)
                self.power_up_rects.pop(i)

    def event_handler(self) -> None:
        """ Handles all the events in the game. """
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = True
                    if event.key == pg.K_RIGHT:
                        self.movement[1] = True
                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = False
                    if event.key == pg.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pg.K_LCTRL:
                        self.ball.active = True

    def draw_window(self) -> None:
        """ Draws all the elements on the main window. """
        self.main_window.blit(pg.transform.scale(self.game_assets["main_background"], (sets.MAIN_WINDOW_WIDTH, sets.MAIN_WINDOW_HEIGHT)), (0, 0))
        pg.draw.rect(self.main_window, (242, 242, 242), (95, 95, 1410, 710))

        score_to_blit = self.SCORE_FONT.render(str(self.score), True, "white")
        self.main_window.blit(score_to_blit, (sets.MAIN_WINDOW_WIDTH // 2 - score_to_blit.get_width() // 2, 800))

        for i in range(self.extra_lives):
            self.main_window.blit(self.game_assets["paddle"][1], (100 + i * 300, 45))
        
        self.game_window.blit(self.game_assets["background"][self.background_number], (0, 0))

        for pwr_up in self.power_ups:
            pwr_up.render(self.game_window)
        
        self.brick_pattern.render(self.game_window)
        self.ball.render(self.game_window)
        self.paddle.render(self.game_window)

        self.main_window.blit(self.game_window, (100, 100))
        pg.display.update()

    def run(self) -> None:
        """ Runs the game and contains the game loop. """
        while self.running:
            self.clock.tick(self.FPS)
            
            self.handle_power_ups()
            self.event_handler()
            self.ball.update()
            self.paddle.update(self.movement, paddle_size=200)
            self.paddle.check_pwr_up_collision()
            if self.extra_lives < 0:
                self.game_over()
            if len(self.brick_pattern.brick_list) < 1:
                self.level_complete()
            
            self.draw_window()

if __name__ == "__main__":
    Game().run()