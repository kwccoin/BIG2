from big2_class import *

def priority_set(player):
	priority_set_pairs(player)
	priority_set_fullhouses(player)
	priority_set_flushes(player)

def priority_set_pairs(player):
	length_pairs=len(player.pairs)

	for i in range(0,length_pairs,1):
		value=player.pairs[i].pairs_1.get_number()

		#Ace is greater than 13
		if value==1:
			player.pairs[i].priority=14*2
		#2 is greater than Ace
		elif value==2:
			player.pairs[i].priority=15*2
		else:
			player.pairs[i].priority=value*2

def priority_set_fullhouses(player):
	length_fullhouse=len(player.fullhouses)
	for i in range(0,length_fullhouse,1):
		value=player.fullhouses[i].fullhouses_1.get_number()
		if value==1:
			player.fullhouses[i].priority=14*3
		if value==2:
			player.fullhouses[i].priority=15*3
		else:
			player.fullhouses[i].priority=value*3

def priority_set_flushes(player):
	length_flushes=len(player.flushes)
	for i in range(0,length_flushes,1):
		value=player.flushes[i].flushes_5.get_number()
		if value==1:
			value=14
		if value==6:
			value=15
		player.flushes[i].priority=0
		for j in range(0,5,1):
			player.flushes[i].priority=player.flushes[i].priority+value-i




