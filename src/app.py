import pygame
import Ui.menue
from Buildings.lager import lager

import Ui.objecte
from dataclasses import dataclass

class App:
	def __init__(self, lager):
		pygame.init()
		self.widht = 500
		self.height = 600
		self.window = pygame.display.set_mode((self.widht, self.height))
		self.lager = lager
		self.name = pygame.display.set_caption("Minicrafter")
		
		self.hoi1 = Ui.menue.Head_Overlay(self, 0, 0, "Holz:")
		self.hoi2 = Ui.menue.Head_Overlay(self, 105, 0, "Stein:")
		self.hoi3 = Ui.menue.Head_Overlay(self, 210, 0, "Bretter:")
		self.hoi4 = Ui.menue.Head_Overlay(self, 315, 0, "Kupfer Erz:")
		self.hoi5 = Ui.menue.Head_Overlay(self, 420, 0, "Kohle")
		self.hoi6 = Ui.menue.Head_Overlay(self, 525, 0, "Eisenerz:")
		self.hoi7 = Ui.menue.Head_Overlay(self, 630, 0, "Hoi")
		self.left_oi1 = Ui.menue.Head_Overlay(self, 5, 200, "Stadt")
		self.left_oi2 = Ui.menue.Head_Overlay(self, 5, 255, "Wald")
		self.left_oi3 = Ui.menue.Head_Overlay(self, 5, 310, "Steinbruch")
		self.left_oi4 = Ui.menue.Head_Overlay(self, 5, 365, "Mine")
		self.left_oi5 = Ui.menue.Head_Overlay(self, 5, 420, "Sägewerk")
		self.left_oi6 = Ui.menue.Head_Overlay(self, 5, 475, "Schmelze")
		self.object_list = []			
		self.running = True
		self.clock = pygame.time.Clock()
	
	def run_game(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
			self.delta_time = self.clock.tick(60) / 1000
			self.window.fill((0, 0, 0))
			self.hoi1.update()
			self.hoi2.update()
			self.hoi3.update()
			self.hoi4.update()
			self.hoi5.update()
			self.left_oi1.update()
			self.left_oi2.update()
			self.left_oi3.update()
			self.left_oi4.update()
			self.left_oi5.update()
			self.left_oi6.update()
			self.prüfen()
			#self.label1.update()
			pygame.display.update()
			
	pygame.quit()
	def prüfen(self):
		while len(self.object_list) <= 2:
			self.object_list.append(Ui.objecte.Click_Object(self))
			for object in self.object_list:
				object.draw_rect()
		else:
			for object in self.object_list:
				object.draw_rect()
			
game = App(lager)



