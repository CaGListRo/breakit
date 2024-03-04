# this is a breakout clone
import pygame as pg
from timeit import default_timer as timer

from ball import Ball
from brick import Brick
from paddle import Paddle
from utilities import load_image, load_images
import settings as sets
import breakit_pattern as bip


class Game:
    '''This is the game class, here is the main-loop located in the play-method'''  
    def __init__(self):
        pg.init()
        self.main_window = pg.display.set_mode((sets.MAIN_WINDOW_WIDTH, sets.MAIN_WINDOW_HEIGHT))
        self.game_window = pg.Surface((sets.GAME_WINDOW_WIDTH, sets.GAME_WINDOW_HEIGHT))
        self.running = True
        self.level = 1

        self.game_assets = {
            'ball': load_image(path='ball', img_name='ball.png', width=32),
            'bricks': load_images(path='bricks', width=(sets.GAME_WINDOW_WIDTH // 9)),
            'paddle': load_images(path='paddle',width=32),
            'pwr_ups':  load_images(path='power ups',width=32)
        }

    def load_pattern(self):
        pattern_name = 'level' + str(self.level) + '_pattern'
        self.level_pattern = getattr(bip, pattern_name)

    def event_handler(self):
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()

    def draw_window(self):
        self.main_window.fill((100, 100, 100))
        self.game_window.fill('black')
        counter = 0
        for element in self.game_assets['bricks']:
            
            self.game_window.blit(element, (155 * counter, 50))
            counter += 1
        self.main_window.blit(self.game_window, (100, 100))

        pg.display.update()


    def run(self):
        last_time = timer()
        self.load_pattern()

        while self.running:
            # delta time
            dt = timer() - last_time
            last_time = timer()
            self.draw_window()

            self.event_handler()
            


if __name__ == '__main__':
    Game().run()