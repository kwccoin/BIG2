class cards(object):
	"""docstring for cards"""
	def __init__(self, suit,number):
		self.suit = suit
		self.number=number
	def get_suit(self):
		return self.suit
	def get_number(self):
		return self.number

		

class big2(object):
	"""docstring for big2"""
	def __init__(self, NumofPlayers):
		self.NumofPlayers = NumofPlayers
	
	def get_NumofPlayers(self):
		return self.NumofPlayers
		


class player(object):
	"""docstring fos player"""
	def __init__(self, name,deck ):
		
		self.name = name
		self.deck = deck
		self.have_pairs=0
		self.have_fullhouses=0
		self.have_flushes=0
		self.pairs=[]
		self.fullhouses=[]
		self.flushes=[]
	
	def getname(self):
		return self.name
	
	def getdeck(self):
		return self.deck

class robot(object):
	"""docstring fos robot"""
	def __init__(self, name,deck ):
		
		self.name = name
		self.deck = deck
		self.have_pairs=0
		self.have_fullhouses=0
		self.have_flushes=0
		self.pairs=[]
		self.fullhouses=[]
		self.flushes=[]
	
	def getname(self):
		return self.name
	
	def getdeck(self):
		return self.deck

class pairs(object):
	"""docstring for pairs"""
	def __init__(self, pairs_1,pairs_2,priority):
		self.pairs_1=pairs_1
		self.pairs_2=pairs_2
		self.priority=priority
	def get_pairs_1():
		return self.pairs_1
	def get_pairs_2():
		return self.pairs_2
	def get_priority():
		return self.priority

class fullhouses(object):
	"""docstring for fullhouses"""
	def __init__(self, fullhouses_1,fullhouses_2,fullhouses_3,fullhouses_4,fullhouses_5,priority):
		self.fullhouses_1 = fullhouses_1
		self.fullhouses_2=fullhouses_2
		self.fullhouses_3=fullhouses_3
		self.fullhouses_4=fullhouses_4
		self.fullhouses_5=fullhouses_5
		self.priority=priority
	def get_fullhouses_1():
		return fullhouses_1
	def get_fullhouses_2():
		return fullhouses_2
	def get_fullhouses_3():
		return fullhouses_3
	def get_fullhouses_4():
		return fullhouses_4
	def get_fullhouses_5():
		return fullhouses_5
	def priority():
		return priority


class flushes(object):
	"""docstring for flushes"""
	def __init__(self, flushes_1,flushes_2,flushes_3,flushes_4,flushes_5,priority):
		self.flushes_1 = flushes_1
		self.flushes_2=flushes_2
		self.flushes_3=flushes_3
		self.flushes_4=flushes_4
		self.flushes_5=flushes_5
		self.priority=priority
	def get_flushes_1():
		return flushes_1
	def get_flushes_2():
		return flushes_2
	def get_flushes_3():
		return flushes_3
	def get_flushes_4():
		return flushes_4
	def get_flushes_5():
		return flushes_5
	def priority():
		return priority