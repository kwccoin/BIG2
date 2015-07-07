import random

#suffle cards 1-52 1-13 clubs 14-26 diamonds 27-39 hearts 40-52 spades

def shuffle_card():
	items=[]
	suits=["club","diamond","heart","spade"]
	for i in range(0,4,1):
		for j in range(1,14,1):
			items.append(cards(suits[i],j))

  
	random.shuffle(items)

	return items


#deal the card. depending on how many robot we got.
def deal_card(shuffled,num_robots,no_player):
	#needa find '3'(club 3) in the list first to decide who get the leftover
	if num_robots==2:
		if no_player==3:
			return shuffled[51]
		else:
				return shuffled[0+17*no_player:17+17*no_player]

	elif num_robots==3:
		return shuffled[0+13*no_player:13+13*no_player]

def find_club_3(shuffled,x):
    if x==1:
    	for i in range(0,52,1):
    		if shuffled[i].get_number()==3 and shuffled[i].get_suit()=="club":
    			return i+1;
    elif x==2:
    	for i in range(0,52,1):
    		if shuffled[i].get_number()==3 and shuffled[i].get_suit()=="diamond":
    			return i+1;


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

	
	def getname(self):
		return self.name
	
	def getdeck(self):
		return self.deck

class robot(object):
	"""docstring fos robot"""
	def __init__(self, name,deck ):
		
		self.name = name
		self.deck = deck
	
	def getname(self):
		return self.name
	
	def getdeck(self):
		return self.deck



	#def __str__(self):
     #   return "%s s deck is %s" % (self.name, self.deck)
		