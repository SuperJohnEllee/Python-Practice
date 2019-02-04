import itertools
import random

deck = list(itertools.product(range(1,14),[
	'Spade', 'Heart', 'Diamond', 'Club']))
random.shuffle(deck)
print("You got: ")
for x in range(13):
	print(deck[x][0], "of", deck[x][1])