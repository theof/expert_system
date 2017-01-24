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
			return node.left in self.true and node.left not in self.false
		else:
			return self.visit(node.left)

	def visit_AndConclusion(self, node):
		# print('visit_AndConclusion')
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
		if self.visit(node.expression):
			return self.visit(node.conclusion)

	def visit_System(self, node):
		# print('visit_System')
		for fact in node.initial_facts:
			self.true.append(fact)
		for rule in node.rules:
			self.visit(rule)
		for query in node.queries:
			if query in self.true and query not in self.false:
				print(query, ': True')
			else:
				print(query, ': False')

	def interpret(self):
		self.visit(self.parser.parse())



