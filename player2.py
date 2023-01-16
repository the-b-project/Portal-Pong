import pygame as pg

from settings import *
from classes.player import *

class Player2(Player):

    def __init__(self, pos, groups):
        super().__init__(pos, groups)

    def input(self):
        keys = pg.key.get_pressed()

        # Y - Direction
        if keys[pg.K_UP]:
            self.direction.y = -1
        elif keys[pg.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        # X - Direction
        #if keys[pg.K_LEFT]:
        #    self.direction.x = -1
        #    self.status = "left"
        #elif keys[pg.K_RIGHT]:
        #    self.direction.x = 1
        #    self.status = "right"
        #else:
        #    self.direction.x = 0

        # Set portal
        #if keys[pg.K_SPACE] and not self.attacking:
        #    self.attacking = True

        #    if self.status == "up":
        #        pos_x = self.rect.x
        #        pos_y = self.rect.y - 50
        #    elif self.status == "down":
        #        pos_x = self.rect.x
        #        pos_y = self.rect.y + 50
        #    elif self.status == "left":
        #        pos_x = self.rect.x - 50
        #        pos_y = self.rect.y
        #    else:
        #        pos_x = self.rect.x + 50
        #        pos_y = self.rect.y
        #    Bullet((pos_x, pos_y), self.status, self.groups, self.obstacle_sprites)