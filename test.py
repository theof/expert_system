#!/usr/bin/env python3

import sys, collections
from classes import *

#################################################################

def get_items(file):
	fd = open(file)
	items={}

	for line in fd:
		line = line.split('#')[0]
		for i in range(0, len(line)):
			if (line[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and line[i] not in items):
				items[line[i]] = Simple(-1)
	fd.close()
	return (items)

#################################################################

def get_facts(file, items):
	fd = open(file)

	for line in fd:
		line = line.split('#')[0]
		if (line[0] == '='):
			for i in range(1, len(line) - 1):
				items[line[i]] = Simple(1)
	fd.close()
	return (items)

#################################################################

def parse_condition(tab, items):

	if (len(tab) == 3):
		if (tab[1] == '+'):
			item = And(items[tab[0]], items[tab[2]])
		elif (tab[1] == '|'):
			item = Or(items[tab[0]], items[tab[2]])
		elif (tab[1] == '^'):
			item = Xor(items[tab[0]], items[tab[2]])
	else:
		print('2 hard 4 me', tab)
		exit(1)

	return (item)

#################################################################

def get_rules(file, items):
	fd = open(file)

	for line in fd:
		tab = line.split('=>')
		if (len(tab) == 1):
			 pass
		else:
			tab[0] = " ".join(tab[0].split())
			n = tab[1][1]
			items[n] = parse_condition(tab[0].split(), items)

	return (items)


#################################################################

def evaluate(name, items):
	if (items[name].need == 1):
		print(name, "is TRUE")
	else:
		print(name, "is FALSE")

#################################################################

def queries(file, items):
	fd = open(file)
	qries = ''

	for line in fd:
		line = line.split('#')[0]
		if (line[0] == '?'):
			for i in range(1, len(line) -1):
				evaluate(line[i], items)


#################################################################

def expert_system(file):
	items = get_items(file)
	items = get_facts(file, items)
	items = get_rules(file, items)
	queries(file, items)

#################################################################

def main():
	try:
		expert_system(sys.argv[1])
	except (IndexError):
		print ('{}: no file name provided.'.format(sys.argv[0]))
		exit(1)
	except (FileNotFoundError) as e:
		print ('{}: {}'.format(sys.argv[0], e))
		exit(1)

#################################################################

if __name__ == "__main__":
	try:
		main()
	except (KeyboardInterrupt):
		print('biatch')
