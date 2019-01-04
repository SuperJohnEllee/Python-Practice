import random, time
def guess():
	randNum = random.randint(0, 101)
	starttime = time.time()
	count = 0
	while True:
		count += 1
		number = int(input('Enter number between 0 to 100: '))
		if number < randNum:
			print('To Small')
		elif number > randNum:
			print('Too Large')
		else:
			endtime = time.time()
			print('The number is ', number)
			print('You have got it in', count, 'tries', 'in ', round(endtime - starttime, 2), ' seconds')
			break
if __name__ == '__main__':
	guess()

