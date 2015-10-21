#!/usr/bin/env python3

#//////////// expert_system.py  by  theof & oniro @ 42borntocode //////////////#

import sys, classes, collections

################################################################################

UNDEFINED = -1
FALSE = 0
TRUE = 1

################################################################################

def expert_system(fd):

 # Initialize dictionnary
	items = {}
	for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
		items[letter] = UNDEFINED

 # Process input
	for line in fd:
		line = ''.join(line.split())
		if line == '':
			pass

		elif line.startswith('='):
			for letter in line[1:]:
				if ()

		elif line.startswith('?'):
			for letter in line[1:]:
				if letter not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
					print()
				else
					items[letter].evaluate(items)

		else:
			


################################################################################

def main():

	if len(sys.argv) == 1:
		expert_system(sys.stdin)
	else:
		for argv in sys.argv:
			try:
				fd = open(argv)
				expert_system(fd)
				fd.close()
			except FileNotFoundError as e:
				print('{}: {}'.format(sys.argv[0], e.what))

################################################################################

if __name__ == "__main__":

	try:
		main()
	except (KeyboardInterrupt):
		print('\u0443\u043A\u0430')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////#
