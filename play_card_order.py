def who_have_3(player_list):
	length=len(player_list)
	for i in range(0,length,1):
		if player_list[i].have_club_3==1:
			return i