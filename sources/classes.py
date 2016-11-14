SYMBOLS_FN = {
	'+': lambda a, b: False if False in (a, b) else (None if None in (a, b) else True),
	'|': lambda a, b: None if (a, b).count(None) == 2 else (bool(a) | bool(b)),
	'^': lambda a, b: None if None in (a, b) else (a ^ b),
	'!': lambda a: None if a is None else not a
}

class Fact:
	def __init__(self, name):
		self.values = [False]
		self.virgin = True
		self.name = name

	def eval(self, deepness):
		if deepness > 100:
			return None
		ev = []
		for value in self.values:
			if type(value) is bool:
				ev.append(value)
			else:
				ev.append(value.eval(deepness + 1))
		if None in ev:
			return None
		else:
			return all(ev)

	def debug(self, display=True):
		return_values = {None: '?', True: 'T', False: 'F'}
		d = "{}({})".format(self.name, return_values[all(self.values)])
		if display:
			print d
		else:
			return d

class Rule:
	def __init__(self, A):
		self.A = A

	def eval(self, deepness):
		if deepness > 100:
			return None
		return self.A.eval(deepness + 1)

	def debug(self, display=True):
		d = "{}".format(self.A.debug(False))
		if display:
			print d
		else:
			return d

class RuleNot(Rule):	
	def eval(self, deepness):
		if deepness > 100:
			return None
		return (SYMBOLS_FN['!'](self.A.eval(deepness + 1)))

	def debug(self, display=True):
		d = "!({})".format(self.A.debug(False))
		if display:
			print d
		else:
			return d

class RuleAB(Rule):
	def __init__(self, A, B, symbol):
		self.A = A
		self.B = B
		self.symbol = symbol

	def eval(self, deepness):
		if deepness > 100:
			return None
		return (SYMBOLS_FN[self.symbol](self.A.eval(deepness + 1), self.B.eval(deepness + 1)))

	def debug(self, display=True):
		d = "{} {} {}".format("({})".format(self.A.debug(False)), self.symbol, "({})".format(self.B.debug(False)))
		if display:
			print d
		else:
			return d
