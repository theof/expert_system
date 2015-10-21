#!/usr/bin/env python3

###############################################################################
###############################################################################

class Item:

	def __init__(self, symbol, left, right, value, name):
		self.symbol = symbol
		self.left = left
		self.right = right
		self.value = value
		self.name = name

	def andeval(item):
		return item.left.evaluate(item) and item.right.evaluate(item)

	def oreval(item):
		return item.left.evaluate(item) or item.right.evaluate(item)

	def xoreval(item):
		return bool(item.left.evaluate(item)) ^ bool(item.right.evaluate(item))

	def evaluate(self, item):
		print(self.name, ' => ', end='')
		if (self.symbol == '+'):
			print(self.left.name, ' + ', self.right.name)
			return(self.andeval())
		elif (self.symbol == '|'):
			print(self.left.name, ' | ', self.right.name)
			return(self.oreval())
		elif (self.symbol == '^'):
			print(self.left.name, ' ^ ', self.right.name)
			return(self.xoreval())
		else:
			print(bool(self.value))
			return (bool(self.value))

###############################################################################
###############################################################################

def main():
	item = {}
	item['A'] = Item('', None, None, 1, 'A')
	item['B'] = Item('', None, None, 1, 'B')
	item['C'] = Item('+', item['A'], item['B'], 0, 'C')
	item['D'] = Item('', None, None, 0, 'D')
	item['E'] = Item('+', item['A'], item['D'], 0, 'E')
	item['F'] = Item('^', item['A'], item['E'], 0, 'F')
	item['G'] = Item('+', item['C'], item['F'], 0, 'G')

	item['G'].evaluate(item)

###############################################################################

if (__name__ == '__main__'):
	main()

###############################################################################
###############################################################################
