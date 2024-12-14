import pygame as pg
import settings as sets

from typing import Final, TypeVar

Game = TypeVar("Game")

class Paddle:
    """ The paddle class handles the movements of the paddle and the collisions with power ups. """
    MID_TOP: Final[tuple[int]] = (700, 650)

    def __init__(self, game: Game, image: pg.Surface) -> None:
        """
        Initializes the paddle object.
        Args:
        game (Game): The game object.
        image (pg.Surface): The image of the paddle.
        """
        self.game: Game = game
        self.image: pg.Surface = image
        self.rect: pg.Rect = self.image.get_rect(midtop=self.MID_TOP)
        self.pos: pg.Vector2 = pg.Vector2(self.rect.topleft)
        
    def check_pwr_up_collision(self) -> None:
        """ Checks if the paddle collides with a power up. """
        for i, pwr_up in enumerate(self.game.power_up_rects.copy()):
            if self.rect.colliderect(pwr_up[0]):
                if pwr_up[1] == 0 and self.game.ball.speed > 1:
                    self.game.ball.speed -= 0.5
                if pwr_up[1] == 1 and self.game.ball.speed < 10:
                    self.game.ball.speed += 0.5
                if pwr_up[1] == 2:
                    self.game.extra_lives += 1
                if pwr_up[1] == 3:
                    self.image = self.game.game_assets["paddle"][0]
                    self.rect = self.image.get_rect(midtop=self.rect.midtop)
                if pwr_up[1] == 4:
                    pass
                    # self.image = self.game.game_assets["paddle"][0]
                    # self.rect = self.image.get_rect(midtop=self.rect.midtop)
                if pwr_up[1] == 5:
                    self.image = self.game.game_assets["paddle"][3]
                    self.rect = self.image.get_rect(midtop=self.rect.midtop)
                if pwr_up[1] == 5:
                    self.image = self.game.game_assets["paddle"][2]
                    self.rect = self.image.get_rect(midtop=self.rect.midtop)
                self.game.power_ups.pop(i)
                self.game.power_up_rects.pop(i)

    def update(self, movement: tuple[int] = (0, 0), paddle_size: int = 200) -> None:
        """
        Updates the paddle position based on the movement and the paddle size.
        Args:
        movement (tuple[int]): The movement of the paddle. Defaults to (0, 0).
        paddle_size (int): The size of the paddle. Defaults to 200.
        """
        self.pos.x += (movement[1] - movement[0]) * 10
        self.rect.topleft = self.pos
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x + paddle_size > sets.GAME_WINDOW_WIDTH:
            self.pos.x = sets.GAME_WINDOW_WIDTH - paddle_size

    def render(self, surf: pg.Surface) -> None:
        """
        Renders the paddle on the given surface.
        Args:
        surf (pg.Surface): The surface to render the paddle on.
        """
        surf.blit(self.image, self.pos)