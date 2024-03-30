import pygame 
import sys 
from dataclasses import dataclass 
from ressourcen import BaseRess 




@dataclass 
class Player:

	def __init__(self, name, id, title, lager):
		self.name = name 
		self.id = id 
		self.title = title 
		self.lager = lager
		
