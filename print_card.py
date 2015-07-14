from big2_class import *

def print_pairs(pairs):
	print "%d_%s %d_%s" %(pairs.pairs_1.get_number(),pairs.pairs_1.get_suit(),pairs.pairs_2.get_number(),pairs.pairs_2.get_suit()),

def print_fullhouses(fullhouses):
	print '%d_%s %d_%s %d_%s %d_%s %d_%s' %(fullhouses.fullhouses_1.get_number(),fullhouses.fullhouses_1.get_suit(),fullhouses.fullhouses_2.get_number(),fullhouses.fullhouses_2.get_suit(),fullhouses.fullhouses_3.get_number(),fullhouses.fullhouses_3.get_suit(),fullhouses.fullhouses_4.get_number(),fullhouses.fullhouses_4.get_suit(),fullhouses.fullhouses_5.get_number(),fullhouses.fullhouses_5.get_suit()),

def print_flushes(flushes):
	print '%d_%s %d_%s %d_%s %d_%s %d_%s' %(flushes.flushes_1.get_number(),flushes.flushes_1.get_suit(),flushes.flushes_2.get_number(),flushes.flushes_2.get_suit(),flushes.flushes_3.get_number(),flushes.flushes_3.get_suit(),flushes.flushes_4.get_number(),flushes.flushes_4.get_suit(),flushes.flushes_5.get_number(),flushes.flushes_5.get_suit()),

def del_fullhouses(player,fullhouses):
	#!!!you have to del the card start from bigger number in case the order will be messed up.
	del_list=[fullhouses.fullhouses_1.index,fullhouses.fullhouses_2.index,fullhouses.fullhouses_3.index,fullhouses.fullhouses_4.index,fullhouses.fullhouses_5.index]
	del_list.sort()
	print del_list
	for i in range (4,-1,-1):
		del player.deck[del_list[i]]

def del_flushes(player,flushes):
	#!!!you have to del the card start from bigger number in case the order will be messed up.
	del_list=[flushes.flushes_1.index,flushes.flushes_2.index,flushes.flushes_3.index,flushes.flushes_4.index,flushes.flushes_5.index]
	del_list.sort()
	print del_list
	for i in range (4,-1,-1):
		del player.deck[del_list[i]]
