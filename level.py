import pygame as pg
import random

from settings import *
from player import *
from ball import *
from startportal import *
from endportal import *
from line import *

class Level:
	
	def __init__(self):
		self.display_surface = pg.display.get_surface()
		self.visible_sprites = pg.sprite.Group() # Sprites that are visible
		self.obstacle_sprites = pg.sprite.Group() # Sprites that can collide with each other
		# Player centric camera view
		#self.offset = pg.math.Vector2()

		self.playing = False
		self.score = [0, 0]
		self.key_pressed = False

		self.font = pg.font.SysFont(None, 50) # Load font file and set the font size

	def create_objects(self):
		Player((100, HEIGHT // 2), [self.visible_sprites, self.obstacle_sprites])
		self.ball = Ball((random.randrange(WIDTH * 0.4, WIDTH * 0.6), random.randrange(0, HEIGHT)), [self.visible_sprites], self.obstacle_sprites)
		Line((WIDTH // 2 , HEIGHT // 2), [self.visible_sprites])
		Startportal((WIDTH // 3 , HEIGHT // 3), [self.visible_sprites, self.obstacle_sprites])
		Endportal((WIDTH * 0.8 , HEIGHT * 0.8), [self.visible_sprites, self.obstacle_sprites])

	def draw(self):
		# Draw Start screen
		if not self.playing and self.score == [0, 0]:
			self.draw_default_screen("start")
			self.check_space_press()
		
		# Draw Game over Screen
		elif not self.playing and self.score != [0, 0]:
			self.draw_default_screen("gameover")
			self.check_space_press()
		# Draw playing screen
		else:
			self.key_pressed = False
			# Player centric camera view
			#self.offset.x = self.player.rect.centerx - WIDTH // 2
			#self.offset.y = self.player.rect.centery - HEIGHT // 2

			for sprite in self.visible_sprites:
				# Player centric camera view
				#offset_pos = sprite.rect.topleft - self.offset
				#self.display_surface.blit(sprite.image, offset_pos)
				self.display_surface.blit(sprite.image, sprite.rect.topleft)

	def run(self):
		if self.playing:
			if self.ball.status == "play":
				self.playing = True
			elif self.ball.status == "leftout":
				self.score[0] += 1
				self.playing = False
				# Delete all sprites
				for sprite in self.visible_sprites:
					sprite.kill()

		self.draw()
		self.visible_sprites.update()
	
	def check_space_press(self):
		keys = pg.key.get_pressed()
		if keys[pg.K_SPACE] and self.key_pressed == False:
			self.key_pressed = True # Prevent multiple key presses
			self.playing = True # Set the level status to be playing (again)
			self.create_objects() # Create the level objects
	
	def draw_default_screen(self, status):
		if status == "start":
			text1 = self.font.render("To Start the game press 'Space'", True, (0, 255, 0))
			textRect1 = text1.get_rect()
			textRect1.center = (WIDTH // 2, HEIGHT // 2)
			self.display_surface.blit(text1, textRect1)

		if status == "gameover":
			text1 = self.font.render("Press 'Space' to re-play", True, (0, 255, 0))
			textRect1 = text1.get_rect()
			textRect1.center = (WIDTH // 2, HEIGHT * 0.4)
			self.display_surface.blit(text1, textRect1)

			text2 = self.font.render(f"Score: {self.score[0]} : {self.score[1]}", True, (0, 255, 0))
			textRect2 = text2.get_rect()
			textRect2.center = (WIDTH // 2, HEIGHT * 0.5)
			self.display_surface.blit(text2, textRect2)
		