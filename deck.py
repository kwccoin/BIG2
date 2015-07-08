#arrange deck, find pairs fullhouse flush....(and set priority)
from card import *
from big2_class import *


def arrange_deck(unarranged_deck):
	arranged=object_quicksort(unarranged_deck)
	return arranged



#quicksort

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

"""
def find_pairs(arrange_deck):
	length=len(arrange_deck)
	i=0
	while i<length:

"""








