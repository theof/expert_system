#!/usr/bin/env python3

#//////////// expert_system.py  by  theof & oniro @ 42borntocode //////////////#

import sys

################################################################################
################################################################################

class Simple:

	def __init__(self, need):
		self.need = need

################################################################################

class And:

	def __init__(self, left, right):
		if (right.need == 1 and left.need == 1):
			self.need = 1
		else:
			self.need = -1

################################################################################

class Or:

	def __init__(self, left, right):
		if (right.need == 1 or left.need == 1):
			self.need = 1
		else:
			self.need = -1

################################################################################

class Xor:

	def __init__(self, left, right):
		if (right.need == 1 and left.need == -1):
			self.need = 1
		elif (right.need == -1 and left.need == 1):
			self.need = 1
		else:
			self.need = -1

################################################################################

class Not:

	def __init__(self, need):
		self.need = -1 * need

################################################################################
################################################################################


def parse_file(file):
	fd = open(file)

	rules = []
	facts = []
	queries = ''

	for line in fd:

		line = line.split('#')[0]
		if line:
			if (line[0] == '='):
				facts.append(line[1:-1])
			elif (line[0] == '?'):
				queries = line[1:-1]
			else:
				rules.append(line[0:-1])

	return (rules, facts, queries)

################################################################################

def main():

	try:
		rules, facts, queries = parse_file(sys.argv[1])
	except (IndexError):
		print ('{}: no file name provided.'.format(sys.argv[0]))
		exit(1)
	except (FileNotFoundError) as e:
		print ('{}: {}'.format(sys.argv[0], e))
		exit(1)

	## 

	# Rules #

	A = Simple(D)
	B = And(E, F)
	C = Or(G, H)

	# Facts #

	D = Simple(1)
	E = Simple(1)
	F = Simple(1)
	G = Simple(1)

	for i in range(0, len(queries)):
	    evaluate(queries[i])

################################################################################

if __name__ == "__main__":
	try:
		main()
	except (KeyboardInterrupt):
		print('If you don\'t want me, i dont want you ' +
		'\U0000265E <- this is a horse')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////#
