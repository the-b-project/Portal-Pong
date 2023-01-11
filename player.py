import pygame as pg

from settings import *

class Player(pg.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        
        self.image = pg.Surface((50, 300))
        self.image.fill("green")
        #self.image = pg.image.load("assets/rock.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.mask = pg.mask.from_surface(self.image)
    
        self.groups = groups

        # Movement
        self.direction = pg.math.Vector2()
        self.speed = 5
        self.status = "right"

        # Attack
        self.attacking = False
        self.counter = 60

        self.type = "player"

    def input(self):
        keys = pg.key.get_pressed()

        # Y - Direction
        if keys[pg.K_UP]:
            self.direction.y = -1
            self.status = "up"
        elif keys[pg.K_DOWN]:
            self.direction.y = 1
            self.status = "down"
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
        if keys[pg.K_SPACE] and not self.attacking:
            self.attacking = True

            if self.status == "up":
                pos_x = self.rect.x
                pos_y = self.rect.y - 50
            elif self.status == "down":
                pos_x = self.rect.x
                pos_y = self.rect.y + 50
            elif self.status == "left":
                pos_x = self.rect.x - 50
                pos_y = self.rect.y
            else:
                pos_x = self.rect.x + 50
                pos_y = self.rect.y
            #Bullet((pos_x, pos_y), self.status, self.groups, self.obstacle_sprites)

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.rect.x += self.direction.x * speed
        self.rect.y += self.direction.y * speed

    def cooldown(self):
        self.counter -= 1
        if self.counter < 0:
            self.attacking = False
            self.counter = 60

    def update(self):
        self.input()
        self.move(self.speed)
        if self.attacking:
            self.cooldown()
