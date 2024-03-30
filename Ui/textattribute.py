import pygame
from pygame.font import SysFont

from Ui.menue import Head_Overlay

class Text_Attribute:
	def __init__(self, game, xpos, ypos, text, color, *arg, **kwargs):
		pygame.init()
		self.game = game
		self.surface = isinstance(game, Head_Overlay)
		self.xpos = xpos
		self.ypos = ypos
		self.text = text
		self.color = color
		self.font = pygame.font.SysFont
		self.font_size = 20
		self.font_type = "Arial"
		self.font_type_size = self.font_size
		self.font_type_type = self.font_type
		self.font_type_bold = False
		self.font_type_italic = False
		

	def update(self):
		self.draw_text()

	def draw_text(self):
		pygame.draw.text(self.surface, self.xpos, self.ypos)
		
		
	