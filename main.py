#from card import card
import random
#import deck
from card import *
from deck import *
from big2_class import *
from play_card_order import *
from print_card import *


print "POKER GAME : BIG 2!"

player_name=raw_input ("player name:")
NumberofRobots=input ("robot number?")

#numberofrobots has to be greater than 1 and less than 3


while NumberofRobots>3 or NumberofRobots<2:
	print "there can only be 2 or 3 robots "
	NumberofRobots=input ("robot number?")
#shuffled card 
shuffled_items=shuffle_card()


#deal card to players(0:player 1~3:robots)
if NumberofRobots==2:

	player0=player(player_name,deal_card(shuffled_items,NumberofRobots,0),NumberofRobots)
	robot1=robot("robot1",deal_card(shuffled_items,NumberofRobots,1))
	robot2=robot("robot2",deal_card(shuffled_items,NumberofRobots,2))
	#gives leftover to someone who have club 3
	club_3_decision_case1(NumberofRobots,shuffled_items,player0,robot1,robot2)
	player0.deck=arrange_deck(player0.deck)
	robot1.deck=arrange_deck(robot1.deck)
	robot2.deck=arrange_deck(robot2.deck)


elif NumberofRobots==3:

	player0=player(player_name,deal_card(shuffled_items,NumberofRobots,0),NumberofRobots)
	robot1=robot("robot1",deal_card(shuffled_items,NumberofRobots,1))
	robot2=robot("robot2",deal_card(shuffled_items,NumberofRobots,2))
	robot3=robot("robot3",deal_card(shuffled_items,NumberofRobots,3))

	club_3_decision_case2(shuffled_items,player0,robot1,robot2,robot3)


	

#have dealed the card
#next step: arrange the deck
#define a function to deal the deck




finish_game=0

if NumberofRobots==3:
	player_lists=[player0,robot1,robot2,robot3]
	order=who_have_3(player_lists)
	print 'check'
	print order
	while finish_game==0:
		check_deck(player_lists[order])
		for i in range(0,13,1):
			print player_lists[order].deck[i].get_number()
			print player_lists[order].deck[i].get_suit()
			print player_lists[order].deck[i].index
		player_lists[order].first_play_club_3()
		for i in range(0,12,1):
			print player_lists[order].deck[i].get_number()
			print player_lists[order].deck[i].get_suit()
			print player_lists[order].deck[i].index
		check_deck(player_lists[(order+1)%4])
		check_deck(player_lists[(order+2)%4])
		check_deck(player_lists[(order+3)%4])
		finish_game=1



"""
		for i in range(0,13,1):
			print player_lists[order].deck[i].get_number()
			print player_lists[order].deck[i].get_suit()
			print player_lists[order].deck[i].index

"""

#print player0.deck[1].get_number()
#print robot1.getdeck()
#print robot2.getdeck()
#print robot3.getdeck()
#deck testing











