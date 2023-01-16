import pygame as pg
from settings import *

class Ball(pg.sprite.Sprite):

    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        
        self.image = pg.Surface((32, 32))
        self.image.fill("white")
        #self.image = pg.image.load("assets/rock.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.mask = pg.mask.from_surface(self.image)

        self.obstacle_sprites = obstacle_sprites

        # Movement
        self.direction = pg.math.Vector2()
        self.direction.x = 1
        self.direction.y = 1
        self.speed = 10
        self.status = "play"

    def move(self):
        # Check left screen border collision
        if self.rect.left <= 0:
            self.status = "leftout"
        # Check right screen border collision
        if self.rect.right >= WIDTH - 10:
            self.direction.x *= -1
        # Check top and bottom border collision
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.direction.y *= -1

        self.rect.x += self.direction.x * self.speed
        self.collision("horizontal")
        self.rect.y += self.direction.y * self.speed
        #self.collision("vertical")

    def collision(self):
        for sprite in self.obstacle_sprites:
            if sprite.type == "player":
                if self.rect.left <= sprite.rect.right:
                    self.direction.x *= -1
                #if self.rect.top <= sprite.rect.bottom or self.rect.bottom >= sprite.rect.top:
                 #   self.direction.y *= -1
    
    def collision(self, direction):
        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    offset_x = sprite.rect.topleft[0] - self.rect.left
                    offset_y = sprite.rect.topleft[1] - self.rect.top
                    if self.mask.overlap(sprite.mask, (offset_x, offset_y)):
                        if sprite.type == "player":
                            self.direction.y *= -1

        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    offset_x = sprite.rect.topleft[0] - self.rect.left
                    offset_y = sprite.rect.topleft[1] - self.rect.top
                    if self.mask.overlap(sprite.mask, (offset_x, offset_y)):
                        if sprite.type == "player":
                            self.direction.x *= -1
                        if sprite.type == "startportal-p1":
                            for sprite in self.obstacle_sprites:
                                if sprite.type == "endportal-p1":
                                    self.direction.y *= -1
                                    self.rect.center = sprite.rect.center
                        if sprite.type == "startportal-p2":
                            for sprite in self.obstacle_sprites:
                                if sprite.type == "endportal-p2":
                                    self.direction.y *= -1
                                    self.rect.center = sprite.rect.center

    def update(self):
        self.move()