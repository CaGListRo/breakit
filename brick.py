import pygame as pg
import breakit_pattern as bip

from typing import Final, TypeVar

Game = TypeVar("Game")


class Brick:
    """the brick class should handle the brick related stuff, like the position and health of the brick"""
    BRICK_X_DISTANCE: Final[int] = 140
    BRICK_Y_DISTANCE: Final[int] = 48

    def __init__(self, game: Game, level: int) -> None:
        """
        Initializes the Brick object.
        Args:
        game (Game): The game object.
        level (int): The current level.
        """
        self.game: Game = game
        self.level: int = level
        self.brick_list: list[list[int]] = []
        self.brick_rects = []
        self.load_pattern()

    def create_bricks(self) -> None:
        """ Creates the brick_list and the brick_rects list. """
        for i in range(10):
            for j in range(5):
                if self.level_pattern[j][i] > 0:
                    self.brick_list.append([i * self.BRICK_X_DISTANCE, j * self.BRICK_Y_DISTANCE, self.level_pattern[j][i]])
                    self.brick_rects.append(pg.Rect(i * self.BRICK_X_DISTANCE, j * self.BRICK_Y_DISTANCE, self.BRICK_X_DISTANCE, self.BRICK_Y_DISTANCE))
        # print(f"bl: {self.brick_list}     br: {self.brick_rects}")

    def load_pattern(self) -> None:
        """ Loads the brick pattern from the breakit_pattern.py (bip)"""
        pattern_name = "level" + str(self.level) + "_pattern"
        self.level_pattern = getattr(bip, pattern_name)
        self.create_bricks()

    def render(self, surf: pg.Surface) -> None:
        """
        Draws the bricks to the given surface.
        Args:
        serf (pg.Surface): The surface to draw the bricks on.
        """
        for brick in self.brick_list:
            if brick[2] > 0:
                surf.blit(self.game.game_assets["bricks"][brick[2] - 1], (brick[0], brick[1]))
        for rectangle in self.brick_rects:
            pg.draw.rect(surf, (255, 0,  0), rectangle, 3)