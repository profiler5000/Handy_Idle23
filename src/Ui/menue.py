import pygame       


class Head_Overlay:
	def __init__(self, game, xpos, ypos, text):
		pygame.init()
		self.game = game
		self.surface = self.game.window
		self.xpos = xpos
		self.ypos = ypos
		self.width = 50
		self.height = 25
		self.color = pygame.Color(255, 255, 255)
		self.text = text
		self.font = pygame.font.Font(None, 20)
		self.text= self.font.render(self.text, True, "black")
		
		
		

	def update(self):
		self.draw_head()

	def draw_head(self):
		pygame.draw.rect(self.surface, self.color, (self.xpos, self.ypos, self.width, self.height))
		self.surface.blit(self.text, (self.xpos + 5, self.ypos + 5))
#ho1 = Head_Overlay(0, 0)

