#arrange deck, find pairs fullhouse flush....(and set priority)
from card import *
from priority_set import *
from big2_class import *
#from print_card import *


def arrange_deck(player):
	player.deck=object_quicksort(player.deck)
	length=len(player.deck)
	for i in range(0,length,1):
		player.deck[i].index=i



#quicksort for object

def object_quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0].get_number()
        for x in array:
            if x.get_number() < pivot:
                less.append(x)
            if x.get_number() == pivot:
                equal.append(x)
            if x.get_number() > pivot:
                greater.append(x)
        # Don't forget to return something!
        return object_quicksort(less)+equal+object_quicksort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quicksort(less)+equal+quicksort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

#find pairs and return all possible pairs we can select
def find_pairs(player):
	player.pairs=[]
	length=len(player.deck)
	i=0
	#length-1 coz we only count its gaps like {1 | 2 | 3}
	while i<length-1:
		if player.deck[i].get_number()==player.deck[i+1].get_number():
			this_pair=pairs(player.deck[i],player.deck[i+1],1)
			#check if this pair have spade. spade=bigger pair when same numbers
			if this_pair.pairs_1.suit=="spade" or this_pair.pairs_2.suit=="spade":
				this_pair.power=1
				
			player.pairs.append(this_pair)
		i=i+1
	#consider the case that we have club3 diamond3 spade3 but we want club3+spade3. so "+2"
	i=0
	while i<length-2:
		if player.deck[i].get_number()==player.deck[i+2].get_number():
			#
			#
			#remember to set the priority
			this_pair=pairs(player.deck[i],player.deck[i+2],1)
			if this_pair.pairs_1.suit=="spade" or this_pair.pairs_2.suit=="spade":
				this_pair.power=1
			player.pairs.append(this_pair)
			#print player.pairs[0].get_pairs_1()
		i=i+1
	#if we have pair then switch have_pairs from 0 to 1
	if len(player.pairs)!=0:
		player.have_pairs=1
#
#
#needa deal with the condition if we got 4 same numbers like AAAA
def find_fullhouse(player):
	player.fullhouses=[]
	length=len(player.deck)
	i=0
	if player.have_pairs==0:
		exit

	while i<length-2:
		if player.deck[i].get_number()==player.deck[i+1].get_number() and player.deck[i].get_number()==player.deck[i+2].get_number():
			pair_length=len(player.pairs)
			for x in range (0,pair_length,1):
				if player.pairs[x].pairs_1.get_number()!=player.deck[i].get_number():
					#remember to set priority
					this_fullhouse=fullhouses(player.deck[i] , player.deck[i+1] , player.deck[i+2] , player.pairs[x].pairs_1 , player.pairs[x].pairs_2,1)
					player.fullhouses.append(this_fullhouse)


		i=i+1
	#if we have pair then switch have_pairs from 0 to 1
	if len(player.fullhouses)!=0:
		player.have_fullhouses=1

def find_flush(player):
	player.flushes=[]
	length=len(player.deck)
	#use a counter to see how many cards for each numbers
	#if we have streak 5 numbers that all have cards then we have flush(apply extract_flush)
	counter=[]
	#initial counter[] to 0
	for i in range(0,13,1):
		counter.append(0)
	#count the number of cards
	for i in range(0,length,1):
		counter[player.deck[i].get_number()-1]+=1
	print counter
	i=0
	streak=0
	temp_flushes=[]
	#to see if we have streak 5 numbers (have flushes) 
	while i<13:
		if counter[i]!=0:
			streak=streak+1
			if streak==5:
				#extract flush returns the list for all possible for this number series
				
				temp_flushes=extract_flush(player.deck,counter,i-4)
				"""
				print temp_flushes[0].flushes_1.get_number()
				print temp_flushes[0].flushes_2.get_number()
				print temp_flushes[0].flushes_3.get_number()
				print temp_flushes[0].flushes_4.get_number()
				print temp_flushes[0].flushes_5.get_number()"""
				#conca the list
				player.flushes.extend(temp_flushes)
				#player.flushes=player.flushes+temp_flushes
				streak=streak-1
		elif counter[i]==0:
			streak=0
		i=i+1
		temp_flushes=[]
	if len(player.flushes)!=0:
		player.have_flushes=1

def extract_flush(deck,counter_1,start_number):
	extraction=[]
	start_point=0
	temp=counter_1
	counter=0
	
	for i in range(0,start_number,1):
		
		start_point=start_point+counter_1[i]

	#print "start point:"
	#print start_point
	start_point=start_point+counter_1[start_number]-1
	for i in range(0,counter_1[start_number],1):
		for j in range(0,counter_1[start_number+1],1):
			for k in range(0,counter_1[start_number+2],1):
				for m in range(0,counter_1[start_number+3],1):
					for n in range(0,counter_1[start_number+4],1):
						counter=counter+1
						this_flushes=flushes(deck[start_point-i],deck[count_start(start_point,counter_1,start_number,1)-j],deck[count_start(start_point,counter_1,start_number,2)-k],deck[count_start(start_point,counter_1,start_number,3)-m],deck[count_start(start_point,counter_1,start_number,4)-n],1)
						extraction.append(this_flushes)
						"""
						print this_flushes.flushes_1.get_number()
						print this_flushes.flushes_1.get_suit()
						print this_flushes.flushes_2.get_number()
						print this_flushes.flushes_2.get_suit()
						print this_flushes.flushes_3.get_number()
						print this_flushes.flushes_3.get_suit()
						print this_flushes.flushes_4.get_number()
						print this_flushes.flushes_4.get_suit()
						print this_flushes.flushes_5.get_number()
						print this_flushes.flushes_5.get_suit()
						"""
	return extraction				

def count_start(start_point,counter,start_number,n):
	for i in range (0,n,1):
		start_point=start_point+counter[start_number+i+1]
	return start_point

def check_deck(player):

	
	arrange_deck(player)
	player.pairs=[]
	find_pairs(player)
	player.fullhouses=[]
	find_fullhouse(player)
	player.flushes=[]
	find_flush(player)
	priority_set(player)

def play_deck(player_lists,order,i):
	finish_game=0
	finish_game=player_lists[(order+i)%4].play_card()
	print "finish_game"
	print finish_game
	player_lists[(order+i+1)%4].state=player_lists[(order+i)%4].state
	

	player_lists[(order+i+1)%4].last_combination.append(player_lists[(order+i)%4].current_combination[-1])









