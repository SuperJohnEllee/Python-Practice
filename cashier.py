items = int(input())
for i in range(items):
	product = input()
	price = float(input())
	quantity = int(input())
	total = price * quantity
print(product)
print(str(float(price)))
print(str(int(quantity)))
print(str(int(total)))
all_total = total * items
print('Total price is ' + str(float(all_total)))
