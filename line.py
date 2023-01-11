import pygame as pg

from settings import *

class Line(pg.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pg.Surface((10, HEIGHT))
        self.image.fill("white")
        #self.image = pg.image.load("assets/rock.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.mask = pg.mask.from_surface(self.image)