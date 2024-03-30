import sys 
import pygame
from dataclasses import dataclass
from app import App
# from amount import *

# übergabe des schwierigkeitsgrades und das es sich um ein neues spiel handelt.
auswahl = "easy"
newGame = True

@dataclass
class DifficulltSetup:
	count = 0
	def __init__(self, diff, newGame, auswahl):
		self.name = __class__.__name__
		self.description = None
		self.cur_amount = None
		self.count = None
		self.exp_amount = None
		self.max_amount = None
		self.image = None
		self.Game = newGame
		self.auswahl = auswahl
	def check_amounts(self):
		if self.auswahl == "easy" and self.Game:
			self.cur_amount = 100
			self.exp_amount = 0
			self.max_amount = self.cur_amount * 10
		elif auswahl == "medium" and newGame:
			self.cur_amount = 50
			self.exp_amount = 0
			self.max_amount = self.cur_amount * 10
		elif auswahl == "hard" and newGame:
			self.cur_amount = 25
			self.exp_amount = 0
			self.max_amount = self.cur_amount * 10
		

	
class Holz(BaseRess):
	def __init__(self, diff, newGame):
		super().__init__(self, auswahl, newGame)
		self.name = "Holz"
		self.description = 'Dies ist eine Grundressource und wird zur weiter verarbeitung genutzt'
		
		self.cur_amount = 0
		self.count = 0
		self.exp_amount = 0
		self.max_amount = None
		self.image = pygame.image.load("ressourcen/holz.png")
		self.game = newGame
		super().check_amounts(self, auswahl, newGame)
			
		

