MAX_DEPTH = 50

class NodeVisitor(object):

	def visit(self, node):
		method_name = 'visit_' + type(node).__name__
		visitor = getattr(self, method_name, self.generic_visit)
		return visitor(node)

	def generic_visit(self, node):
		raise Exception('ES : No visit_{} method.'.format(type(node).__name__))



class Interpreter(NodeVisitor):

	def __init__(self, parser):
		self.parser = parser
		self.true = []
		self.false = []

	def visit_Expression(self, node):
		# print('visit_Expression')
		if node.right:
			return self.visit(node.left) ^ self.visit(node.right)
		else:
			return self.visit(node.left)		

	def visit_XorExpr(self, node):
		# print('visit_XorExpr')
		if node.right:
			return self.visit(node.left) | self.visit(node.right)
		else:
			return self.visit(node.left)		

	def visit_OrExpr(self, node):
		# print('visit_OrExpr')
		if node.right:
			return self.visit(node.left) and self.visit(node.right)
		else:
			return self.visit(node.left)

	def visit_AndExpr(self, node):
		# print('visit_AndExpr')
		if node.negation:
			return not self.visit(node.right)
		else:
			return self.visit(node.right)

	def visit_ParenExpr(self, node):
		# print('visit_ParenExpr')
		if isinstance(node.left, str):
			self.dependences += node.left
			return node.left in self.true and node.left not in self.false
		else:
			return self.visit(node.left)

	def visit_AndConclusion(self, node):
		# print('visit_AndConclusion')
		self.updates = node.right
		if node.negation:
			self.false.append(node.right)
		else:
			self.true.append(node.right)
	
	def visit_Conclusion(self, node):
		# print('visit_Conclusion')
		self.visit(node.left)
		if node.right:
			self.visit(node.right)

	def visit_Rule(self, node):
		self.dependences = ''
		self.outcomes = ''
		self.visit(node.expression)
		self.visit(node.conclusion)
		return [self.dependences, self.outcomes, node, True]

	def eval(self, node):
		lines = []
		for rule in node.rules:
			lines.append(self.visit(rule))
		self.dependences = [x[0] for x in lines]
		self.outcomes = [x[1] for x in lines]

		self.true = []
		self.false = []
		for fact in node.initial_facts:
			self.true.append(fact)
		deepness = 0
		while True in [x[3] for x in lines] and deepness < MAX_DEPTH:
			deepness += 1
			for line in lines:
				if line[3] and all([True if fact not in self.outcomes else False for fact in line[0]]):
					if self.visit(line[2].expression):
						self.visit(line[2].conclusion)
						line[3] = False
						for fact in line[1]:
							self.dependences.replace(fact, '')
		for line in lines:
			if line[3]:
				if self.visit(line[2].expression):
					self.visit(line[2].conclusion)

	def visit_System(self, node):
		# print('visit_System')
		self.eval(node)

		for query in node.queries:
			if query in self.true and query not in self.false:
				print(query, ': True')
			else:
				print(query, ': False')

	def interpret(self):
		self.visit(self.parser.parse())



