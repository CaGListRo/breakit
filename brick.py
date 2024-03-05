import pygame as pg
import breakit_pattern as bip


class Brick:
    '''the brick class should handle the brick related stuff, like the position and health of the brick'''
    def __init__(self, game, level):
        self.game = game
        self.level = level
        self.brick_list = []
        self.brick_rects = []
        self.load_pattern()

    def check_collision(self):
        pass

    def create_bricks(self):
        for i in range(9):
            for j in range(5):
                self.brick_list.append([i * 155 + 1, j * 45, self.level_pattern[j][i]])
                self.brick_rects.append(pg.Rect(i * 155 + 1, j * 45, 155, 42))

    def load_pattern(self):
        pattern_name = 'level' + str(self.level) + '_pattern'
        self.level_pattern = getattr(bip, pattern_name)
        self.create_bricks()

    def render(self, surf):
        for brick in self.brick_list:
            if brick[2] != 0:
                surf.blit(self.game.game_assets['bricks'][brick[2] - 1], (brick[0], brick[1]))