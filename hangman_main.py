import random
from terminaltables import SingleTable 
#================#
words=['baku', 'moscow', 'tokyo', 'london', 'ankara', 'alat']

def select_word():
	return random.choice(words)


def user_input():
	usr_input=input('Input letter: ')
	return usr_input

def lst(word):
	find_word=[]
	for i in word:
		find_word.append(' _ ')
	return find_word

def main():
	word=select_word()
	empty=lst(word)
	print('\a'.join(empty))
	game_end=0
	life=10
	while True:
		x=user_input()
		if x in word and x!='':
			for i in range(len(word)):
				if x == word[i]:
					empty[i] = x
			print(''.join(empty))
		if x not in word or x=='':
			life-=1
			print(''.join(empty))
			print('You left {} try'.format(life))
			if game_end == life: 
				print('You lose!!!')
				break
		if word == ''.join(empty):
			print('=== You win!!! ===\a')
			break
	
try:
	main()
except KeyboardInterrupt as e:
	print('\n\aGame stopped!!!')


