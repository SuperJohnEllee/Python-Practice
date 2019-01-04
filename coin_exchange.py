knut = int(input())
if knut == 0:
	print('** ERROR: Must enter a positive whole number only.')
elif knut < 493:
		
	if knut < 29:
		result = str(int(knut)) + 'K'
		print(result)
	elif knut % 29 == 0:
		new = knut/29
		result = str(int(new)) + 'S'
		print(result)
	elif knut % 29 > 0:
		extra = knut % 29
		new = knut/29
		result = str(int(new)) + 'S' + ' ' + str(int(extra)) + 'K'
		print(result)
elif knut % 493 == 0 and knut != 0:
	new = knut / 493
	result = str(int(new)) + 'G'
	print(result)
elif knut % 493 > 0:
	extra = knut % 493
	if extra % 29 == 0:
		new = knut / 493
		sickles = extra / 29
		result = str(int(new)) + 'G' + ' ' + str(int(sickles)) + 'S'
		print(result)
	elif extra % 29 > 0:
		new = knut / 493
		knots = extra
		result = str(int(new)) + 'G' + ' ' + str(int(knots)) + 'K'
		print(result)