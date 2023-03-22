from random import shuffle
import time
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x']

MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
	}

def shuffle_field():
	game_board = []
	for i in range(0,len(my_list),4):
		game_board.append(my_list[i:i+4])
	shuffle(game_board)
	return game_board

'''def print_field(game_board):
	game_board = shuffle_field()
	for i in game_board:
		print(i)'''

def game_finished(game_board):
	game_win = []
	for i in range(0,len(my_list),4):
		game_win.append(my_list[i:i+4])
	if game_board == game_win:
		return True
	else:
		return False

def perform_move(field, key):
	for l in field:
		if 'x' in l:
			pos_x = l.index('x')
			ls_indx = field.index(l)
	if key == 'a':
		field[:][ls_indx][pos_x], field[:][ls_indx][pos_x-1] =\
		field[:][ls_indx][pos_x-1], field[:][ls_indx][pos_x]
	if key == 's': 
		field[:][ls_indx][pos_x], field[:][ls_indx-1][pos_x] =\
		field[:][ls_indx-1][pos_x], field[:][ls_indx][pos_x]
	if key == 'd':
		field[:][ls_indx][pos_x], field[:][ls_indx][pos_x+1] =\
		field[:][ls_indx][pos_x+1], field[:][ls_indx][pos_x]
	if key == 'w':
		field[:][ls_indx][pos_x], field[:][ls_indx+1][pos_x] =\
		field[:][ls_indx+1][pos_x], field[:][ls_indx][pos_x]	

	print(pos_x,ls_indx)
		
def handle_user_input():
	user_input = input('Enter "w" move up "s" move down "a" move left "d" move right: ').lower()
	if  user_input == 'w':
		return 'w'
	elif user_input == 's':
		return 's'
	elif user_input == 'a':
		return 'a'
	elif user_input == 'd':
		return 'd'

def main():	
	field = shuffle_field()
	game_fin = game_finished(field)
	while True:
		try:
			for i in field:
				print(i)
			key = handle_user_input()
			perform_move(field,key)
			if game_fin:
				print("you win")
				break
		except IndexError :
			print("Cant move")

main()