from random import randrange
import time



l = [[0,0,0],
	 [0,0,0],
	 [0,0,0]]
print('   0  1  2')
for i,z in enumerate(l):
	print(i,z)

while True:
	try:
		for i in range(1,3):
			if i == 1:
				print('User1 begins')
				user1_1, user1_2 = int(input('enter 1st index number: ')), int(input('2nd index number: '))
				if l[user1_1][user1_2] == 0:
					l[user1_1][user1_2] = 1
				else:
					print('Not empty')
				print('   0  1  2')
				for i,z in enumerate(l):
					print(i,z)
			elif i == 2:
				print('User2 begins')
				user1_1, user1_2 = int(input('enter 1st index number: ')), int(input('2nd index number: '))
				l[user1_1][user1_2] = 2
				print('   0  1  2')
				for i,z in enumerate(l):
					print(i,z)
			if l[0][0] == l[1][1] == l[2][2]:
				print('You win')
				break
	except IndexError:
		print('Wrong field index!!!')

print('   0  1  2')
for i,z in enumerate(l):
	print(i,z)
	