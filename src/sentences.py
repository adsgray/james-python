name = ['James', 'David', 'Jamie', 'Neha', 'Lee' ,'Sam']
verb = ['buys', 'rides', 'kicks', 'eats', 'punches']
noun = ['lion', 'bicycle', 'plane', 'hamburger', 'pizza', 'television']

from random import randint

def pick(words):
	num_words = len(words)
	num_picked = randint(0, num_words - 1)
	word_picked = words[num_picked]
	return word_picked

#print(pick(name), pick(verb), 'a', pick(noun), end='\n')

#while True:
print "{} {} a {}\n".format(pick(name), pick(verb), pick(noun))
#	blah = input()
