class BaseRess:
	def __init__(self, description):
		self.name = __class__.__name__
		self.description = description
		self.cur_amount : int
		self.cur_exp_amount : int
		
		
		
		