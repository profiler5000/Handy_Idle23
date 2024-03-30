from Ressourcen.holz import Holz
from Ressourcen.stein import Stein  

class Lager():
	def __init__(self):
		self.namen = []
		self.holz = Holz()
		self.stein = Stein()
		self.lagerliste =[]
		self.create_lagerliste()

	def create_lagerliste(self):
		self.lagerliste.append(self.holz)
		self.lagerliste.append(self.stein)
		
	def namen_ausgeben(self):
		for item in self.lagerliste:
			return item.namen
			
lager = Lager()


