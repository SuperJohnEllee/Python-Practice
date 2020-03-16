num1=input("First Number: ")
num2=input("Second Number: ")
print("Results")
if num1.isdigit() or num2.isdigit():
	print(int(num1), " + ", int(num2), " = ", int(num1) + int(num2))
	print(int(num1), " - ", int(num2), " = ", int(num1) - int(num2))
	print(int(num1), " * ", int(num2), " = ", int(num1) * int(num2))
	print(int(num1), " / ", int(num2), " = ", int(num1) / int(num2))
	print(int(num1), " % ", int(num2), " = ", int(num1) % int(num2))
else:
	print("Error, number is a string")