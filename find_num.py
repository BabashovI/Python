import random
nums=list(range(20,50))
random.shuffle(nums)
def find_num():
	for i in range(1,16):
		j=0
		print('Guess another number.')
		while j < 3:
			x=int(input('Guess number: '))
			if x == nums[i]:
				print('You find numer: {}'.format(nums[i]))
				break
			elif x < nums[i]:
				print('Less Than number\ntry again')
				j+=1
			elif x > nums[i]:
				print('Greater Than number\ntry again')
				j+=1

		#print(i)
find_num()