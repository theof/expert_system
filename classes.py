import sys, collections

class Item:

	def __init__(self, symbol, left, right, value):
		self.symbol = symbol
		self.left = left
		self.right = right
		self.value = value

	def evaluate(self, item):
		if (item.value != -1):
			return (item.value)
		elif (item.symbol == '+'):
			return(andeval(item))
		elif (item.symbol == '|'):
			return(oreval(item))
		elif (item.symbol == '^'):
			return(xoreval(item))

	def andeval(item):
		return evaluate(item.left) and evaluate(item.right)

	def oreval(item):
		return evaluate(item.left) or evaluate(item.right)

	def xoreval(item):
		return evaluate(item.left) ^ evaluate(item.right)
