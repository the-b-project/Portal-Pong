import pygame as pg

from settings import *
from classes.player import *

class Player1(Player):

    def __init__(self, pos, groups):
        super().__init__(pos, groups)

    def input(self):
        keys = pg.key.get_pressed()

        # Y - Direction
        if keys[pg.K_w]:
            self.direction.y = -1
        elif keys[pg.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0