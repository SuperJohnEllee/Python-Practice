import random
import string


def create_pass(x):
	allChars = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
	passPhrase = []
	for i in range(x):
		tmp = random.choice(allChars)
		passPhrase.append(tmp)
	res = "".join(passPhrase)
	return res

test1 = create_pass(16)
print(test1)
test2 = create_pass(32)
print(test2)