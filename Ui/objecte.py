import pygame
from random import randint
import Ressourcen.base
from Ressourcen.base import BaseRess



class Click_Object:
	def __init__(self, game ):
		self.game = game
		self.surface = game.window
		self.xpos = (randint(200, 400))
		self.ypos = (randint(200, 600))
		self.width = 10
		self.height = 10
		self.color = ("red")
		self.mousepos = pygame.mouse.get_pos()
		self.rect = pygame.Rect.__getitem__
		
	def draw_rect(self):
		pygame.draw.rect(self.surface, self.color, (self.xpos, self.ypos, self.width, self.height))

	

	def update(self):
		self.draw_rect()
		
		
			
		
				
				
		
	

		
	

