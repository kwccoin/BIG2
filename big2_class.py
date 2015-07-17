from print_card import *

#1:single 2:pairs 3:fullhouses 4:flushes




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
		#1:single 2:pairs 3:fullhouses 4:flushes
		self.state=1
		self.current_combination=[]
		self.last_combination=[]
	
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

	def play_card(self):
		playable_list=[]
		counter=1
		length_deck=len(self.deck)
		length_pairs=len(self.pairs)
		length_fullhouses=len(self.fullhouses)
		length_flushes=len(self.flushes)
		have_play=0
		if self.state==1:
			for i in range(0,length_deck,1):
				if self.deck[i].get_number()>self.last_combination[-1].get_number():
					playable_list.append(self.deck[i])
					print '(%d.)' %(counter),
					print "%d_%s " %s(self.deck[i].get_number(),self.deck[i].get_suit())
					counter=counter+1
			if len(playable_list)!=0:
				print " "
				choice=input("choose 1 from above list:")
				print "%d_%s " %(self.deck[i].get_number(),self.deck[i].get_suit())
				self.current_combination.append(playable_list[choice-1])
				self.state=1
				del self.deck[i]
			else:
				print "pass"
				self.current_combination.append(self.last_combination[-1])
				self.state=1
		elif self.state==2:
			for  i in range(0,length_pairs,1):
				if self.pairs[i].priority>self.last_combination[-1].priority:
					playable_list.append(self.pairs[i])
					print '(%d.)' %(counter),
					print "%d_%s %d_%s" %(self.pairs[i].pairs_1.get_number(),self.pairs[i].pairs_1.get_suit(),self.pairs[i].pairs_2.get_number(),self.pairs[i].pairs_2.get_suit()),
					counter=counter+1
			if len(playable_list)!=0:
				print " "
				choice=input("choose 1 from above list:")
				print "%d_%s %d_%s" %(playable_list[choice-1].pairs_1.get_number(),playable_list[choice-1].pairs_1.get_suit(),playable_list[choice-1].pairs_2.get_number(),playable_list[choice-1].pairs_2.get_suit())
				self.current_combination.append(playable_list[choice-1])
				self.state=2
				del_pairs(self,playable_list[choice-1])
			else:
				print "pass"
				self.current_combination.append(self.last_combination[-1])
				self.state=2


		elif self.state==3:
			for  i in range(0,length_fullhouses,1):
				if self.fullhouses[i].priority>self.last_combination[-1].priority:
					playable_list.append(self.fullhouses[i])
					print '(%d.)' %(counter),
					print_fullhouses(self.fullhouses[i]) 
					counter=counter+1
			if len(playable_list)!=0:
				print " "
				choice=input("choose 1 from above list:")
				print_fullhouses(playable_list[choice-1])
				self.current_combination.append(playable_list[choice-1])
				self.state=3
				del_fullhouses(self,playable_list[choice-1])
			else:
				print "pass"
				self.current_combination.append(self.last_combination[-1])
				self.state=3

		elif self.state==4:
			for  i in range(0,length_flushes,1):
				if self.flushes[i].priority>self.last_combination[-1].priority:
					playable_list.append(self.flushes[i])
					print '(%d.)' %(counter),
					print_flushes(self.flushes[i]) 
					counter=counter+1
			if len(playable_list)!=0:
				print " "
				choice=input("choose 1 from above list:")
				print_flushes(playable_list[choice-1])
				self.current_combination.append(playable_list[choice-1])
				self.state=4
				del_flushes(self,playable_list[choice-1])
			else:
				print "pass"
				self.current_combination.append(self.last_combination[-1])
				self.state=3








	def first_play_club_3(self):
		playable_list=[]
		counter=1
		#find how many forms for each combination
		length_deck=len(self.deck)
		length_pairs=len(self.pairs)
		length_fullhouses=len(self.fullhouses)
		length_flushes=len(self.flushes)
		decision=input("what kind of conbination you want to play(1:single,2:pairs,3:fullhouses,4:flushes):")
		self.state=decision
		#case:1 to play a single card
		if decision==1:
			print "3(club)"

			for i in range (0,length_deck-1,1):
				if self.deck[i].get_number()==3 and self.deck[i].get_suit()=="club":
					self.current_combination.append(self.deck[i])
					del self.deck[i]
					
		if decision==2:
			for i in range (0,length_pairs,1):
				if self.pairs[i].pairs_1.get_number()==3 and self.pairs[i].pairs_1.get_suit()=="club":
					playable_list.append(self.pairs[i])
					print '(%d.)' %(counter),
					print "%d_%s %d_%s" %(self.pairs[i].pairs_1.get_number(),self.pairs[i].pairs_1.get_suit(),self.pairs[i].pairs_2.get_number(),self.pairs[i].pairs_2.get_suit()),
					counter=counter+1
									
				if self.pairs[i].pairs_2.get_number()==3 and self.pairs[i].pairs_2.get_suit()=="club":
					playable_list.append(self.pairs[i])
					print '(%d.)' %(counter), 
					print "%d_%s %d_%s" %(self.pairs[i].pairs_1.get_number(),self.pairs[i].pairs_1.get_suit(),self.pairs[i].pairs_2.get_number(),self.pairs[i].pairs_2.get_suit()),
					counter=counter+1
			print ""
			choice=input("choose 1 from above list:")
			print "%d_%s %d_%s" %(playable_list[choice-1].pairs_1.get_number(),playable_list[choice-1].pairs_1.get_suit(),playable_list[choice-1].pairs_2.get_number(),playable_list[choice-1].pairs_2.get_suit())
			self.current_combination.append(playable_list[choice-1])
			del_pairs(self,playable_list[choice-1])
		

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
			self.current_combination.append(playable_list[choice-1])
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
				if self.flushes[i].flushes_3.get_number()==3 and self.flushes[i].flushes_3.get_suit()=='club':
					playable_list.append(self.flushes[i])
					#print out the choice
					print "(%d.)" %(counter),
					print_flushes(self.flushes[i]) 
					#the index of play_list
					counter=counter+1
			print " "
			choice=input("choose 1 from above list:")
			print_flushes(playable_list[choice-1])
			self.current_combination.append(playable_list[choice-1])
			del_flushes(self,playable_list[choice-1])



class robot(big2):
	"""docstring fos robot"""
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

	def play_card(self):
		playable_list=[]
		length_deck=len(self.deck)
		length_pairs=len(self.pairs)
		length_fullhouses=len(self.fullhouses)
		length_flushes=len(self.flushes)
		if self.state==1:
			for i in range(0,length_deck,1):
				if self.deck[i].get_number()>self.last_combination[-1].get_number():
					print self.deck[i].get_number()
					playable_list.append(self.deck[i])
			if len(playable_list)!=0:
				min=10000
				temp=0
				for i in range(0,len(playable_list),1):
					if playable_list[i].get_number()<min:
						min=playable_list[i].get_number()
						temp=i
				print "this is temp ",
				print temp
				print "%d_%s " %(playable_list[temp].get_number(),playable_list[temp].get_suit())
				self.current_combination.append(playable_list[temp])
				self.state=1
				del self.deck[playable_list[i].index]
			else:
				print "pass"
				self.current_combination.append(self.last_combination[-1])
				self.state=1
		
		elif self.state==2:
			for  i in range(0,length_pairs,1):
				if self.pairs[i].priority>self.last_combination[-1].priority:
					playable_list.append(self.pairs[i])
			if len(playable_list)!=0:
				min=10000
				temp=0
				for i in range(0,len(playable_list),1):
					if playable_list[i].priority<min:
						min=playable_list[i].priority
						temp=i
				print "%d_%s %d_%s" %(playable_list[temp].pairs_1.get_number(),playable_list[temp].pairs_1.get_suit(),playable_list[temp].pairs_2.get_number(),playable_list[temp].pairs_2.get_suit())
				self.current_combination.append(playable_list[temp])
				self.state=2
				del_pairs(self,playable_list[temp])
		
			else:
				print "pass"
				self.current_combination.append(self.last_combination[-1])
				self.state=2

		elif self.state==3:
			for  i in range(0,length_fullhouses,1):
				if self.fullhouses[i].priority>self.last_combination[-1].priority:
					playable_list.append(self.fullhouses[i])
			if len(playable_list)!=0:
				min=10000
				temp=0
				for i in range(0,len(playable_list),1):
					if playable_list[i].priority<min:
						min=playable_list[i].priority
						temp=i
				print_fullhouses(playable_list[temp])
				self.current_combination.append(playable_list[temp])
				self.state=3
				del_fullhouses(self,playable_list[temp])
		
			else:
				print "pass"
				self.current_combination.append(self.last_combination[-1])
				self.state=3

		elif self.state==4:
			for  i in range(0,length_flushes,1):
				if self.flushes[i].priority>self.last_combination[-1].priority:
					playable_list.append(self.flushes[i])
			if len(playable_list)!=0:
				min=10000
				temp=0
				for i in range(0,len(playable_list),1):
					if playable_list[i].priority<min:
						min=playable_list[i].priority
						temp=i
				print_flushes(playable_list[temp])
				self.current_combination.append(playable_list[temp])
				self.state=4
				del_flushes(self,playable_list[temp])
		
			else:
				print "pass"
				self.current_combination.append(self.last_combination[-1])
				self.state=4

	def first_play_club_3(self):
		length_deck=len(self.deck)
		length_flushes=len(self.flushes)
		length_fullhouses=len(self.fullhouses)
		length_pairs=len(self.pairs)
		play_flush=[0,0,0]
		playable_list=[]
		have_play=0
		for i in range (0,length_flushes,1):
			if self.flushes[i].flushes_1.get_number()==3 and self.flushes[i].flushes_1.get_suit()=='club':
				play_flush[0]=i
			elif self.flushes[i].flushes_2.get_number()==3 and self.flushes[i].flushes_2.get_suit()=='club':
				play_flush[1]=i
			elif self.flushes[i].flushes_3.get_number()==3 and self.flushes[i].flushes_3.get_suit()=='club':
				play_flush[2]=i
		for i in range (0,3,1):
			if play_flush[i]!=0:
				print_flushes(self.flushes[play_flush[i]])
				self.current_combination.append(self.flushes[play_flush[i]])
				del_flushes(self,self.flushes[play_flush[i]])
				have_play=1
				break
		if have_play==1:
			self.state=4
			return 0

		for i in range (0,length_fullhouses,1):
			if self.fullhouses[i].fullhouses_1.get_number()==3:
				if self.fullhouses[i].fullhouses_1.get_suit()=="club":
				#put any playable fullhouses in the list
					playable_list.append(self.fullhouses[i])
				
				elif self.fullhouses[i].fullhouses_2.get_suit()=="club":
					playable_list.append(self.fullhouses[i])
				elif self.fullhouses[i].fullhouses_3.get_suit()=="club":
					playable_list.append(self.fullhouses[i])
			if self.fullhouses[i].fullhouses_4.get_number()==3:
				if self.fullhouses[i].fullhouses_4.get_suit()=="club":
				#put any playable fullhouses in the list
					playable_list.append(self.fullhouses[i])

				if self.fullhouses[i].fullhouses_5.get_suit()=='club':
					playable_list.append(self.fullhouses[i])
		if len(playable_list)!=0:
			min=10000
			temp=0
			for i in range(0,len(playable_list),1):
				if playable_list[i].priority<min:
					min=playable_list[i].priority
					temp=i
			print_fullhouses(playable_list[temp])
			self.current_combination.append(playable_list[temp])
			del_fullhouses(self,playable_list[temp])
			have_play=1
		if have_play==1:
			self.state=3
			return 0

		for i in range (0,length_pairs,1):
			if self.pairs[i].pairs_1.get_number()==3 and self.pairs[i].pairs_1.get_suit()=="club":
				
				print "%d_%s %d_%s" %(self.pairs[i].pairs_1.get_number(),self.pairs[i].pairs_1.get_suit(),self.pairs[i].pairs_2.get_number(),self.pairs[i].pairs_2.get_suit())
				have_play=1
				self.current_combination.append(self.pairs[i])
				del_pairs(self,self.pairs[i])
				break
			if self.pairs[i].pairs_2.get_number()==3 and self.pairs[i].pairs_2.get_suit()=="club":
				playable_list.append(self.pairs[i])
				print "%d_%s %d_%s" %(self.pairs[i].pairs_1.get_number(),self.pairs[i].pairs_1.get_suit(),self.pairs[i].pairs_2.get_number(),self.pairs[i].pairs_2.get_suit())
				have_play=1
				self.current_combination.append(self.pairs[i])
				del_pairs(self,self.pairs[i])
				break
		if have_play==1:
			self.state=2
			return 0

		for i in range (0,length_deck,1):
			if self.deck[i].get_number()==3 and self.deck[i].get_suit()=='club':
				print "%d_%s" %(self.deck[i].get_number(),self.deck[i].get_suit())
				self.state=1
				self.current_combination.append(self.deck[i])
				del self.deck[i]
				return 0







			


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










