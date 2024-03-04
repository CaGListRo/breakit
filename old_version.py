import pygame as py
import math
from random import randint, choice
from breakit_pattern import *

py.init()

MAIN_WINDOW_RES = 1400,800
GAME_RES = (1000, 700)
MAIN_WIN = py.display.set_mode(MAIN_WINDOW_RES)
GAME_WIN = py.surface.Surface(GAME_RES)

FPS = 60
clock = py.time.Clock()


class Bricks(py.sprite.Sprite):
    def __init__(self, x, y, brick_numb):
        py.sprite.Sprite.__init__(self)
        if 1 <= brick_numb < 7:
            self.health = 1
        elif brick_numb == 7:
            self.health = 2
        elif brick_numb == 8:
            self.health = 3
        elif brick_numb == 9:
            self.health = 5
        self.image = py.transform.scale(py.image.load("EigeneProjekte\images\\breakit\\block_" + str(brick_numb) + ".png"), (100, 30))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
    
    def update(self):
        if py.sprite.spritecollide(self, ball_group, False, py.sprite.collide_mask):
            self.health -= 1
            if self.health == 0:
                self.kill()


class Paddle(py.sprite.Sprite):
    def __init__(self, x, y, type, x_scale, y_scale):
        py.sprite.Sprite.__init__(self)
        self.image = py.transform.scale(py.image.load("images/breakit/paddle_" + type + ".png"), (x_scale, y_scale))
        self.rect = self.image.get_rect()
        self.rect.midbottom = [x, y]
    
    def update(self):
        # set move speed
        speed = 8
        keys = py.key.get_pressed()
        if keys[py.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if keys[py.K_RIGHT] and self.rect.right < GAME_RES[0]:
            self.rect.x += speed
        
        self.mask = py.mask.from_surface(self.image)


class LaserBlast(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = py.transform.scale(py.image.load("images/breakit/laser_blast.png"), (20, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    
    def update(self):
        speed = 8
        


class Ball(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = py.transform.scale(py.image.load("images/breakit/ball.png"), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    

    def update(self, sticky):
        self.mask = py.mask.from_surface(self.image)
        if sticky and GAME_RES[1] - 100 <= self.rect.center[1] <= GAME_RES[1] - 80:
            speed = 8
            keys = py.key.get_pressed()
            if keys[py.K_LEFT] and self.rect.left > 80:
                self.rect.x -= speed
            if keys[py.K_RIGHT] and self.rect.right < GAME_RES[0] - 80:
                self.rect.x += speed


class PowerUps(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        extras_list = ["blaster", "extra_life", "grow", "shrink", "sticky"]
        type = choice(extras_list)
        self.image = py.transform.scale(py.image.load("images/breakit/power_up_" + type + ".png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        speed = 3
        self.rect.y += speed


brick_group = py.sprite.Group()
paddle_group = py.sprite.Group()
laser_group = py.sprite.Group()
ball_group = py.sprite.Group()
pwrup_group = py.sprite.Group()

def create_pattern(level):
    pattern_name = (f"level{str(level)}_pattern")
    # for row in len(pattern_name):
    #     for col in range(9):
    #         number = pattern_name[row][col]
    #         print(number)       
            # brick = Bricks(j * 110 + 10, i * 40 + 50, number)
            # brick_group.add(brick)

def main():
    level = 1
    dx, dy, speed = 1, -1, 5
    dx_save, dy_save = dx, dy
    run, sticky = True, True
    paddle = Paddle(GAME_RES[0] // 2, GAME_RES[1] - 50, "normal", 200, 30)
    paddle_group.add(paddle)
    ball = Ball(GAME_RES[0] // 2, GAME_RES[1] - 100)
    ball_group.add(ball)
    # powerup = PowerUps(100,100) #for testing purposes only!
    # pwrup_group.add(powerup)
    create_pattern(level)
    while run:
        clock.tick(FPS)
        for event in py.event.get():
            keys = py.key.get_pressed()
            if event.type == py.QUIT or keys[py.K_ESCAPE]:
                run = False
            if keys[py.K_SPACE]:
                sticky = False
                dx, dy = dx_save, dy_save
                print(dx, dy, dx_save, dy_save)
            if keys[py.K_a]:
                sticky = True

        if not sticky:
            if ball.rect.top < 1:
                dy *= -1
            if ball.rect.left < 1 or ball.rect.right > GAME_RES[0] - 1:
                dx *= -1
            if ball.rect.colliderect(paddle):
                dy *= -1
            ball.rect.x += dx * speed
            ball.rect.y += dy * speed
        elif sticky:
            if ball.rect.colliderect(paddle) or ball.rect.centery > GAME_RES[1] - 101:
                if dx != 0 and dy != 0:
                    dx_save, dy_save = dx, dy
                    dx, dy = 0, 0
            else:
                if ball.rect.top < 1:
                    dy *= -1
                if ball.rect.left < 1 or ball.rect.right > GAME_RES[0] - 1:
                    dx *= -1
                ball.rect.x += dx * speed
                ball.rect.y += dy * speed

        print(Ball.delta_x)
        # update groups
        brick_group.update()   
        paddle_group.update()
        ball_group.update(sticky)
        laser_group.update()
        pwrup_group.update()

        #draw_window()
        MAIN_WIN.fill("orange")
        GAME_WIN.fill("black")
        brick_group.draw(GAME_WIN)
        paddle_group.draw(GAME_WIN)
        ball_group.draw(GAME_WIN)
        laser_group.draw(MAIN_WIN)
        pwrup_group.draw(GAME_WIN)
        MAIN_WIN.blit(GAME_WIN, (50, 50))
        
        py.display.flip()
        
                
if __name__ == "__main__":
    main()