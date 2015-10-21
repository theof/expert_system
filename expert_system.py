#!/usr/bin/env python3

#//////////// expert_system.py  by  theof & oniro @ 42borntocode //////////////#

import sys, classes, collections

################################################################################

def andeval(item):
	if (bool(evaluate(item.left)) and bool(evaluate(item.right)):
		return (1)
	else:
		return (-1)

def oreval(item):
	if (bool(evaluate(item.left)) or bool(evaluate(item.right)):
		return (1)
	else:
		return (-1)

def xoreval(item):
	if (bool(evaluate(item.left)) ^ bool(evaluate(item.right)):
		return (1)
	else:
		return (-1)

def evaluate(item):
	if (item.value != 0):
		return (item.value)
	elif (item.symbol == '+'):
		return(andeval(item))
	elif (item.symbol == '|'):
		return(oreval(item))
	elif (item.symbol == '^'):
		return(xoreval(item))


################################################################################

def main():
	
	#fill items here
	items = fakeitemfiller()
	queries = 'ABC'
	for i in len(queries):
		if (evaluate(items[queries[i]]) == 1):
			print(queries[i], ' is TRUE')
		else:
			print(queries[i], ' is FALSE')

################################################################################

if __name__ == "__main__":
	try:
		main()
	except (KeyboardInterrupt):
		print('nah')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////#
