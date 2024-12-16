import pygame as pg

from typing import TypeVar, Final

Game = TypeVar("Game")


class PowerUp:
    SIZE: Final[tuple[int]] = (50, 50)
    
    def __init__(self, game: Game, pos: tuple[int], img_number: int) -> None:
        """
        Initialize the PowerUp object.
        Args:
        game (Game): The game object.
        pos (tuple[int]): The position of the PowerUp.
        img_number (int): The image number of the PowerUp.
        """
        self.game = game
        self.pos = list(pos)
        self.image = pg.transform.scale(game.game_assets['pwr_ups'][img_number], self.SIZE)
        self.rect = self.image.get_rect(midtop=self.pos)
        self.game.power_up_rects.append([self.rect, img_number])

    def update(self) -> None:
        """ Update the PowerUp position and the rect position. """
        self.pos[1] += 2
        self.rect.midtop = self.pos

    def render(self, surf: pg.Surface) -> None:
        """
        Render the PowerUp on the screen.
        Args:
        surf (pg.Surface): The screen surface.
        """
        surf.blit(self.image, (self.pos))