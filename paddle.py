import pygame as pg


class Paddle:
    '''the paddle class handles all the movements and collisions of the paddle'''
    def __init__(self, game):
        self.game = game

    def render(self, surf):
        surf.blit(self.game.game_assets['paddle'][1], (700, 600))