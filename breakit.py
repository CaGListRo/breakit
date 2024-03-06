# this is a breakout clone
import pygame as pg
from timeit import default_timer as timer

from ball import Ball
from brick import Brick
from paddle import Paddle
from utilities import load_image, load_images
import settings as sets



class Game:
    '''This is the game class, here is the main-loop located in the play-method'''  
    def __init__(self):
        pg.init()
        self.main_window = pg.display.set_mode((sets.MAIN_WINDOW_WIDTH, sets.MAIN_WINDOW_HEIGHT))
        self.game_window = pg.Surface((sets.GAME_WINDOW_WIDTH, sets.GAME_WINDOW_HEIGHT))
        self.running = True
        self.level = 1
        self.movement = [False, False]
        self.paddle = Paddle(self)
        
        self.game_assets = {
            'ball': load_image(path='ball', img_name='ball.png'),
            'bricks': load_images(path='bricks'),
            'paddle': load_images(path='paddle'),
            'pwr_ups': load_images(path='power ups')
        }
    
    def create_brick_pattern(self):
        self.brick_pattern = Brick(self, self.level)

    def event_handler(self):
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

    def draw_window(self):
        self.main_window.fill((100, 100, 100))
        self.game_window.fill('black')
        self.brick_pattern.render(self.game_window)
        self.paddle.render(self.game_window)
        self.main_window.blit(self.game_window, (100, 100))
        
        pg.display.update()


    def run(self):
        self.create_brick_pattern()
        print(self.game_assets)
        while self.running:
            self.draw_window()

            self.event_handler()
            self.paddle.update(self.movement, paddle_size=200)
            


if __name__ == '__main__':
    Game().run()