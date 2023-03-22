#quiz1={'cap of Az  ':'baku', 'cap of USA  ':'vasinqton', 'cap of Japan  ':'tokyo', 'cap of Russia  ':'moscow'}
#t={}
def test(a,b,c,d):
	try:
		for i, j in a.items():
			x = input(i)
			if x == '' :
				d.update({i:j})
			elif x.lower() == j :
				b.update({i:j})
			else:
				c.update({i:j})
		#print('\nOverall answers: {} \nCorrect: {}\nWrong: {}'.format(len(b)+len(c),len(b),len(c)))
	except KeyboardInterrupt as e:
		print('\n\a')
		print(e)
	finally:
		print('\nOverall answers: {} \nCorrect: {}\nWrong: {} \nNotAnswered: {}'.format(len(b)+len(c),len(b),len(c),len(d)))
    
quiz = {'cap of Az  ':'baku', 'cap of USA  ':'vasinqton', 'cap of Japan  ':'tokyo', 'cap of Russia  ':'moscow'}
t = {}
w = {}
n_a = {}

test(quiz,t,w,n_a)