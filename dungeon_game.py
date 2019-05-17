import random
import os

# check win/ loss

CELLS=[(1,1),(1,2),(1,3),(1,4),(1,5),
       (2,1),(2,2),(2,3),(2,4),(2,5),
       (3,1),(3,2),(3,3),(3,4),(3,5),
       (4,1),(4,2),(4,3),(4,4),(4,5),
       (5,1),(5,2),(5,3),(5,4),(5,5)]



def clear_screen():
	os.system('cls' if os.name =="nt" else 'clear')



def get_locations():
	return random.sample(CELLS,3) 


def move_player(player, move):
	x,y=player
	if move== "LEFT":
		y-=1
	if move== "RIGHT":
		y+=1
	if move== "UP":
		x-=1
	if move== "DOWN":
		x+=1
	return x,y



def get_moves(player):
	x,y=player
	moves=["LEFT", "RIGHT", "UP", "DOWN"]
	if y==1:
		moves.remove("LEFT")
	if y==5:
		moves.remove("RIGHT")
	if x==1:
		moves.remove("UP")
	if x==5:
		moves.remove("DOWN")
	return moves



def draw_grid(player):
	for i in range(5):
		print(" _",end="")
	print()
	for r in range(1,6):
		print("|",end="")
		for c in range(1,6):
			if player== (r,c):
				print("X",end="")
				print("|",end="")
			else:
				print("_",end="")
				print("|",end="")
		print()
	
	

# print("Welcome to the dungeon")
monster, door, player= get_locations()
while True:
	clear_screen()
	draw_grid(player)
	print("You're currently in {}".format(player)) 
	print("You can move {}".format(get_moves(player))) 
	print("Enter QUIT to quit")

	move=input("> ").upper()

	if move=="QUIT":
		print("** Come Back Soon **")
		break
	else:
		player=move_player(player,move)
	if player==monster:
		print("***** YOU LOSE *****")
		break
	if player==door:
		print("***** YOU WIN *****")
		break



