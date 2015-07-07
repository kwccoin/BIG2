#from card import card
import random
#import deck
from card import *



print "POKER GAME : BIG 2!"

player_name=raw_input ("player name:")
NumberofRobots=input ("robot number?")

#numberofrobots has to be greater than 1 and less than 3


while NumberofRobots>3 or NumberofRobots<2:
	print "there can only be 2 or 3 robots "
	NumberofRobots=raw_input ("robot number?")
#shuffled card 
shuffled_items=shuffle_card()


#deal card to players(0:player 1~3:robots)
if NumberofRobots==2:

	player0=player(player_name,deal_card(shuffled_items,NumberofRobots,0))
	robot1=robot("robot1",deal_card(shuffled_items,NumberofRobots,1))
	robot2=robot("robot2",deal_card(shuffled_items,NumberofRobots,2))

	leftover=deal_card(shuffled_items,NumberofRobots,3)

    #gives leftover to someone who has club 3
	leftover_decision=find_club_3(shuffled_items,1)
	#consider the case that club 3 is leftover
	if leftover_decision==52:
		leftover_decision=find_club_3(shuffled_items,2)
	if leftover_decision<17:
		player0.deck.append(leftover)
	elif leftover_decision<34:
		robot1.deck.append(leftover)
	elif leftover_decision<51:
		robot2.deck.append(leftover)

 



     
    

  


elif NumberofRobots==3:

	player0=player(player_name,deal_card(shuffled_items,NumberofRobots,0))
	robot1=robot("robot1",deal_card(shuffled_items,NumberofRobots,1))
	robot2=robot("robot2",deal_card(shuffled_items,NumberofRobots,2))
	robot3=robot("robot3",deal_card(shuffled_items,NumberofRobots,3))


for i in range(0,13,1):
	print player0.deck[i].get_number()
	print player0.deck[i].get_suit()

print player0.deck[1].get_number()
print robot1.getdeck()
print robot2.getdeck()
#print robot3.getdeck()











