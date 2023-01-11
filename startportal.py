import pygame as pg

from settings import *

class Startportal(pg.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pg.Surface((64, 64))
        self.image.fill("white")
        #self.image = pg.image.load("assets/rock.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.mask = pg.mask.from_surface(self.image)

        self.type = "startportal"