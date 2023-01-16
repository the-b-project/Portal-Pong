import pygame as pg

from settings import *

class Player(pg.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        
        self.image = pg.Surface((50, 300))
        self.image.fill("white")
        #self.image = pg.image.load("assets/rock.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.mask = pg.mask.from_surface(self.image)
    
        self.groups = groups

        # Movement
        self.direction = pg.math.Vector2()
        self.speed = 5
        self.type = "player"

        # Attack
        #self.attacking = False
        #self.counter = 60

    def move(self, speed):
        #if self.direction.magnitude() != 0:
        #    self.direction = self.direction.normalize()
        
        #self.rect.x += self.direction.x * speed
        self.rect.y += self.direction.y * speed

    def cooldown(self):
        self.counter -= 1
        if self.counter < 0:
            self.attacking = False
            self.counter = 60

    def update(self):
        self.input()
        self.move(self.speed)
        #if self.attacking:
        #    self.cooldown()
