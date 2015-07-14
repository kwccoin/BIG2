from print_card import *

class cards(object):
	"""docstring for cards"""
	def __init__(self, suit,number):
		self.suit = suit
		self.number=number
		self.index=0
	def get_suit(self):
		return self.suit
	def get_number(self):
		return self.number

		

class big2(object):
	"""docstring for big2"""
	def __init__(self,NumofRobots):
		self.NumofRobots = NumofRobots
		#0:single 1:pairs 2:fullhouses 3:lushes
		self.state=0
	
	def get_NumofPlayers(self):
		return self.NumofRobots
	def get_state(self):
		return self.state

		


class player(big2):
	"""docstring fos player"""
	def __init__(self, name,deck,num_of_robot ):
		big2.__init__(self,num_of_robot)
		self.name = name
		self.deck = deck
		self.have_pairs=0
		self.have_fullhouses=0
		self.have_flushes=0
		self.pairs=[]
		self.fullhouses=[]
		self.flushes=[]
		self.have_club_3=0
	
	def getname(self):
		return self.name
	
	def getdeck(self):
		return self.deck
	def first_play_club_3(self):
		playable_list=[]
		counter=1
		#find how many forms for each combination
		length_deck=len(self.deck)
		length_pairs=len(self.pairs)
		length_fullhouses=len(self.fullhouses)
		length_flushes=len(self.flushes)
		decision=input("what kind of conbination you want to play(1:single,2:pairs,3:fullhouses,4:flushes):")
		#case:1 to play a single card
		if decision==1:
			print "3(club)"

			for i in range (0,length_deck-1,1):
				if self.deck[i].get_number()==3 and self.deck[i].get_suit()=="club":
					del self.deck[i]
					
		if decision==2:
			for i in range (0,length_pairs,1):
				if self.pairs[i].pairs_1.get_number()==3 and self.pairs[i].pairs_1.get_suit()=="club":
					playable_list.append(self.pairs[i])
					print '(%d.)' %(counter),
					print "%d_%s %d_%s" %(self.pairs[i].pairs_1.get_number(),self.pairs[i].pairs_1.get_suit(),self.pairs[i].pairs_2.get_number(),self.pairs[i].pairs_2.get_suit()),
					counter=counter+1
					playable_list.append(self.pairs[i])					
				if self.pairs[i].pairs_2.get_number()==3 and self.pairs[i].pairs_2.get_suit()=="club":
					playable_list.append(self.pairs[i])
					print '(%d.)' %(counter), 
					print "%d_%s %d_%s" %(self.pairs[i].pairs_1.get_number(),self.pairs[i].pairs_1.get_suit(),self.pairs[i].pairs_2.get_number(),self.pairs[i].pairs_2.get_suit()),
					counter=counter+1
					playable_list.append(self.pairs[i])
			print ""
			choice=input("choose 1 from above list:")
			print "%d_%s %d_%s" %(playable_list[choice-1].pairs_1.get_number(),playable_list[choice-1].pairs_1.get_suit(),playable_list[choice-1].pairs_2.get_number(),playable_list[choice-1].pairs_2.get_suit())
			del self.deck[playable_list[choice-1].pairs_1.index]
			del self.deck[playable_list[choice-1].pairs_2.index]

		if decision==3:
			for i in range (0,length_fullhouses,1):
				#case of 333XX
				if self.fullhouses[i].fullhouses_1.get_number()==3:
					if self.fullhouses[i].fullhouses_1.get_suit()=="club":
						#put any playable fullhouses in the list
						playable_list.append(self.fullhouses[i])
						#print out the choice
						print "(%d.)" %(counter),
						print_fullhouses(self.fullhouses[i]) 
						#the index of play_list
						counter=counter+1
					elif self.fullhouses[i].fullhouses_2.get_suit()=="club":
						playable_list.append(self.fullhouses[i])
						print "(%d.)" %(counter),
						print_fullhouses(self.fullhouses[i]) 
						counter=counter+1
					elif self.fullhouses[i].fullhouses_3.get_suit()=="club":
						playable_list.append(self.fullhouses[i])
						print "(%d.)" %(counter),
						print_fullhouses(self.fullhouses[i]) 
						counter=counter+1
				if self.fullhouses[i].fullhouses_4.get_number()==3:
					if self.fullhouses[i].fullhouses_4.get_suit()=="club":
						#put any playable fullhouses in the list
						playable_list.append(self.fullhouses[i])
						#print out the choice
						print "(%d.)" %(counter),
						print_fullhouses(self.fullhouses[i]) 
						#the index of play_list
						counter=counter+1
					if self.fullhouses[i].fullhouses_5.get_suit()=='club':
						playable_list.append(self.fullhouses[i])
						print "(%d.)" %(counter),
						print_fullhouses(self.fullhouses[i]) 
						counter=counter+1
			print " "
			choice=input("choose 1 from above list:")
			print_fullhouses(playable_list[choice-1])
			del_fullhouses(self,playable_list[choice-1])
		if decision==4:
			for i in range (0,length_flushes,1):
				if self.flushes[i].flushes_1.get_number()==3 and self.flushes[i].flushes_1.get_suit()=='club':
					playable_list.append(self.flushes[i])
					#print out the choice
					print "(%d.)" %(counter),
					print_flushes(self.flushes[i]) 
					#the index of play_list
					counter=counter+1
				if self.flushes[i].flushes_2.get_number()==3 and self.flushes[i].flushes_2.get_suit()=='club':
					playable_list.append(self.flushes[i])
					#print out the choice
					print "(%d.)" %(counter),
					print_flushes(self.flushes[i]) 
					#the index of play_list
					counter=counter+1
				if self.flushes[i].flushes_2.get_number()==3 and self.flushes[i].flushes_2.get_suit()=='club':
					playable_list.append(self.flushes[i])
					#print out the choice
					print "(%d.)" %(counter),
					print_flushes(self.flushes[i]) 
					#the index of play_list
					counter=counter+1
			print " "
			choice=input("choose 1 from above list:")
			print_flushes(playable_list[choice-1])
			del_flushes(self,playable_list[choice-1])



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
		self.have_club_3=0
	
	def getname(self):
		return self.name
	
	def getdeck(self):
		return self.deck

	def first_play_3(self):


class pairs(object):
	"""docstring for pairs"""
	def __init__(self, pairs_1,pairs_2,priority):
		self.pairs_1=pairs_1
		self.pairs_2=pairs_2
		self.priority=priority
		self.power=0
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
		self.power=0
		#0:club,1:diamond,2:heart,3:spade
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










