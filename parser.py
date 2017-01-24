class AST(object):
	pass

class System(AST):
	def __init__(self, rules, initial_facts, queries):
		self.rules = rules
		self.initial_facts = initial_facts
		self.queries = queries

class Rule(AST):
	def __init__(self, expression, conclusion):
		self.expression = expression
		self.conclusion = conclusion

class Expression(AST):
	def __init__(self, left, right=None):
		self.left = left
		self.right = right

class XorExpr(AST):
	def __init__(self, left, right=None):
		self.left = left
		self.right = right

class OrExpr(AST):
	def __init__(self, left, right=None):
		self.left = left
		self.right = right

class AndExpr(AST):
	def __init__(self, negation, right):
		self.negation = negation
		self.right = right

class ParenExpr(AST):
	def __init__(self, left):
		self.left = left

class Conclusion(AST):
	def __init__(self, left, right=None):
		self.left = left
		self.right = right

class AndConclusion(AST):
	def __init__(self, negation, right):
		self.negation = negation
		self.right = right


class Parser(object):

	def __init__(self, lexer):
		self.lexer = lexer
		self.current_token = self.lexer.get_next_token()

	def error(self, expected):
		raise Exception('ES : Invalid syntax :\ngot: {}\texpected:{}'.format(self.current_token, expected))

	def eat(self, token_type):
		# print(self.current_token)
		if self.current_token.type == token_type:
			self.current_token = self.lexer.get_next_token()
		else:
			self.error(token_type)

	def and_conclusion(self):
		# print('and_conclusion')
		if self.current_token.type == 'NOT':
			self.eat('NOT')
			node = AndConclusion(True, self.current_token.value)
			self.eat('FACT')
			return node
		else:
			token = self.current_token.value
			self.eat('FACT')
			return AndConclusion(False, token)

	def conclusion(self):
		# print('conclusion')
		left = self.and_conclusion()
		if self.current_token.type == 'AND':
			self.eat('AND')
			return Conclusion(left, self.conclusion())
		return Conclusion(left)

	def paren_expr(self):
		# print('paren_expr')
		if self.current_token.type == 'L_PAREN':
			self.eat('L_PAREN')
			node = self.expression()
			self.eat('R_PAREN')
			return ParenExpr(node)
		token = self.current_token.value
		self.eat('FACT')
		return token

	def and_expr(self):
		# print('and_expr')
		if self.current_token.type == 'NOT':
			self.eat('NOT')
			return AndExpr(True, self.and_expr())
		return ParenExpr(self.paren_expr())

	def or_expr(self):
		# print('or_expr')
		left = self.and_expr()
		if self.current_token.type == 'AND':
			self.eat('AND')
			return OrExpr(left, self.or_expr())
		return OrExpr(left)

	def xor_expr(self):
		# print('xor_expr')
		left = self.or_expr()
		if self.current_token.type == 'OR':
			self.eat('OR')
			return XorExpr(left, self.xor_expr())
		return XorExpr(left)

	def expression(self):
		# print('expression')
		left = self.xor_expr()
		if self.current_token.type == 'XOR':
			self.eat('XOR')
			return Expression(left, self.expression())
		return Expression(left)

	def rule(self):
		# print('rule')
		expression = self.expression()
		self.eat('IMPLICATION')
		conclusion = self.conclusion()
		self.eat('NEWLINE')
		return Rule(expression, conclusion)		

	def system(self):
		# print('system')
		rules = []
		initial_facts = []
		queries = []
		
		while self.current_token.type in ['FACT', 'L_PAREN', 'NOT']:
			rules.append(self.rule())
		
		if self.current_token.type == 'EQUAL':
			self.eat('EQUAL')
			while self.current_token.type == 'FACT':
				initial_facts.append(self.current_token.value)
				self.eat('FACT')
			self.eat('NEWLINE')

		if self.current_token.type == 'QUERY':
			self.eat('QUERY')
			while self.current_token.type == 'FACT':
				queries.append(self.current_token.value)
				self.eat('FACT')
			self.eat('NEWLINE')

		self.eat('EOF')
		return System(rules, initial_facts, queries)

	def parse(self):
		return self.system()

