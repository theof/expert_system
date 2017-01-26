import string, pprint
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
		self.expr_value = None
		self.fact_values = {x:[] for x in string.ascii_uppercase}

	def print_fact_values(self, target=False, true_only=True):
		if not target:
			target = self.fact_values
		for k,v in target.items():

			if len(v) and not true_only:
				print("'{}' : {}".format(k,all(v)))
			elif len(v) and all(v):
				print("'{}'".format(k))


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
			return all(self.fact_values[node.left]) and len(self.fact_values[node.left])
		else:
			return self.visit(node.left)

	def visit_AndConclusion(self, node):
		# print('visit_AndConclusion')
		if node.negation != self.expr_value:
			self.fact_values[node.right].append(True)
		else:
			self.fact_values[node.right].append(False)
	
	def visit_Conclusion(self, node):
		# print('visit_Conclusion')
		self.visit(node.left)
		if node.right:
			self.visit(node.right)

	def visit_Rule(self, node):
		self.expr_value = self.visit(node.expression)
		self.visit(node.conclusion)

	def set_initial_facts(self):
		for initial_fact in self.node.initial_facts:
			self.fact_values[initial_fact].append(True)

	def eval(self):
		for i in range(0, MAX_DEPTH):
			# init
			self.set_initial_facts()
			# old
			for rule in self.node.rules:
				self.visit(rule)
			# new
			old_values = self.fact_values
			for rule in self.node.rules:
				self.visit(rule)
			# final = (new - old) + init
			for key, new_values in self.fact_values.items() :
				for old in old_values[key]:
					new_values.remove(old)
			self.set_initial_facts()

	def visit_System(self, node):
		# print('visit_System')
		self.eval()

		for query in node.queries:
			# print(query, ':', self.fact_values[query])
			if all(self.fact_values[query]) and len(self.fact_values[query]):
				print(query, ': True')
			else:
				print(query, ': False')
		
	def interpret(self):
		self.node = self.parser.parse()
		self.visit(self.node)



