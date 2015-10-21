#!/usr/bin/env python3

#//////////// expert_system.py  by  theof & oniro @ 42borntocode //////////////#

import sys, classes, collections

################################################################################

UNDEFINED = -1
FALSE = 0
TRUE = 1

class err_msgs:

	def bad_letter(ltr):
		return '{}: unrecognized token `{}` \u00AF\\(\u00B0_o)/\u00AF'\
				.format(sys.argv[0], ltr)

	def bad_rule(line):
		return '{}: bad rule syntax `{}` \u00AF\\(\u00B0_o)/\u00AF'\
				.format(sys.argv[0], line)

################################################################################

def try_set_letter(vars, letter, value):
	if letter not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
		print(err_msgs.bad_letter(letter))
	else:
		vars[letter] = value

################################################################################

def get_letters(members):

	i = 0
	while(members[i])
		pass

################################################################################

def expert_system(fd):

 # Initialize dictionnary
	vars = {}
	for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
		vars[letter] = UNDEFINED

 # Process input
	for line in fd:
		line = ''.join(line.split())
		if line == '':
			pass

		elif line == 'status':
			for letter, value in vars.items():
				if value == TRUE:
					print('{} is true'.format(letter))

		elif line.startswith('='):
			for letter in line[1:]:
				try_set_letter(vars, letter, TRUE)

		elif line.startswith('!='):
			for letter in line[2:]:
				try_set_letter(vars, letter, FALSE)

		elif line.startswith('?'):
			for letter in line[1:]:
				if letter not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
					print(err_msgs.bad_letter(letter))
				else:
					vars[letter].evaluate(vars)

		else:
			members = filter(None, line.split('=>'))
			if len(members) == 2:                               #Carrement crade. A corriger
				rop = get_letters(members[1])
				if (rop != None):
					for each in rop:
						vars[each] = Item(members[0])
				else:
					print(err_msgs.bad_rule(line))
			else:
				print(err_msgs.bad_rule(line))

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
