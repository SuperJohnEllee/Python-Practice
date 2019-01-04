num = int(input())
x = num
k = []
while x > 0:
	a = int(float(num%2))
	k.append(a)
	num = (num-a) / 2
k.append(0)
string = ""
for j in k[::-1]:
	string = string + str(j)
print((x, string))