#!/usr/bin/python

# Ghost Game by James!!!

from random import randint
print('Ghost Game')
feeling_brave = True
score = 0
while feeling_brave:
	ghost_door = randint(1,3)
	print('three doors ahead...')
	print('a ghost behind one.')
	print('which door do you open?')
	door = input('1,2,or3?')
	door_num = int(door)
	if door_num == ghost_door:
	    print('GHOST!')
	    feeling_brave = False
	else:
		print('No ghost!')
		print('You enter the next room.')
	        score = score + 1
		print('By the way your current score is ', score)
print('run away!')
print('Game over! You scored',score)
	


