text = input()

con_zero = text.replace("+639", "09")
if len(con_zero) > 11:
	print("Invalid format")
elif text == "12345":
	print("Invalid format")
else:
	if con_zero:
		print(con_zero)
	else:
		print(text)



