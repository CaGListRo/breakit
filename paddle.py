import pygame as pg
import settings as sets

class Paddle:
    '''the paddle class handles all the movements and collisions of the paddle'''
    def __init__(self, game, image):
        self.game = game
        self.image = image
        self.rect = self.image.get_rect(midtop=(700, 650))
        self.pos = pg.math.Vector2(self.rect.topleft)
        
    def check_pwr_up_collision(self):
        for i, pwr_up in enumerate(self.game.power_up_rects):
            if self.rect.colliderect(pwr_up[0]):
                if pwr_up[1] == 0 and self.game.ball.speed > 1:
                    self.game.ball.speed -= 0.5
                if pwr_up[1] == 1 and self.game.ball.speed < 10:
                    self.game.ball.speed += 0.5
                if pwr_up[1] == 2:
                    self.game.lives += 1
                if pwr_up[1] == 3:
                    self.image = self.game.game_assets["paddle"][0]
                    self.rect = self.image.get_rect(midtop=self.rect.midtop)
                if pwr_up[1] == 4:
                    pass
                    # self.image = self.game.game_assets["paddle"][0]
                    # self.rect = self.image.get_rect(midtop=self.rect.midtop)
                if pwr_up[1] == 5:
                    self.image = self.game.game_assets["paddle"][2]
                    self.rect = self.image.get_rect(midtop=self.rect.midtop)
                if pwr_up[1] == 5:
                    self.image = self.game.game_assets["paddle"][3]
                    self.rect = self.image.get_rect(midtop=self.rect.midtop)
            # self.game.power_ups.pop(i)
            # self.game.power_up_rects.pop(i)

    def update(self, movement=(0, 0), paddle_size=200):
        self.pos.x += (movement[1] - movement[0]) * 10
        self.rect.topleft = self.pos
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x + paddle_size > sets.GAME_WINDOW_WIDTH:
            self.pos.x = sets.GAME_WINDOW_WIDTH - paddle_size

    def render(self, surf):
        surf.blit(self.image, self.pos)