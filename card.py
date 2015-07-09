#shuffle card, deal card, define classes

import random
from big2_class import*
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

def club_3_decision_case1(num_robots,shuffled_items,player0,robot1,robot2):
	leftover=deal_card(shuffled_items,num_robots,3)
	#gives leftover to someone who has club 3
	leftover_decision=find_club_3(shuffled_items,1)
	#consider the case that club 3 is leftover
	if leftover_decision==52:
		leftover_decision=find_club_3(shuffled_items,2)
	if leftover_decision<17:
		player0.deck.append(leftover)
		player0.have_club_3=1
	elif leftover_decision<34:
		robot1.deck.append(leftover)
		robot1.have_club_3=1
	elif leftover_decision<51:
		robot2.deck.append(leftover)
		robot2.have_club_3=1

def club_3_decision_case2(shuffled_items,player0,robot1,robot2,robot3):

	leftover_decision=find_club_3(shuffled_items,1)
	if leftover_decision<13:
		player0.have_club_3=1
	elif leftover_decision<26:
		robot1.have_club_3=1
	elif leftover_decision<39:
		robot2.have_club_3=1
	elif leftover_decision<52:
		robot3.have_club_3=1
			









