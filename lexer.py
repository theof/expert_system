import string

class Token(object):
	
	def __init__(self, type_, value):
		self.type = type_
		self.value = value

	def __str__(self):
		return "({}: {})".format(self.type, self.value)


class Lexer(object):

	def __init__(self, file):
		self.file = self.cleaner(file)
		self.pos = 0
		self.current_char = self.file[self.pos]

	def error(self):
		raise Exception('ES : Invalid character : {}.'.format(repr(self.current_char)))

	def advance(self):
		self.pos += 1
		if self.pos > len(self.file) - 1:
			self.current_char = None
		else:
			self.current_char = self.file[self.pos]

	def peek(self):
		peek_pos = self.pos + 1
		if peek_pos > len(self.file) - 1:
			return None
		else:
			return self.file[peek_pos]

	def get_sign_token(self):
		return {
			'(' : Token('L_PAREN', self.current_char),
			')' : Token('R_PAREN', self.current_char),
			'!' : Token('NOT', self.current_char),
			'+' : Token('AND', self.current_char),
			'|' : Token('OR', self.current_char),
			'^' : Token('XOR', self.current_char),
			'=' : Token('EQUAL', self.current_char),
			'?' : Token('QUERY', self.current_char),
			'\n' : Token('NEWLINE', repr(self.current_char)),
		}.get(self.current_char)

	def get_next_token(self):
	
		while self.current_char is not None:
			
			if self.current_char == '#':
				while self.current_char != '\n':
					self.advance()
				continue

			if self.current_char == '=' and self.peek() == '>':
				self.advance()
				self.advance()
				return Token('IMPLICATION', '=>')
			
			if self.current_char in '()!+|^=?\n':
				token = self.get_sign_token()
				self.advance()
				return token
			
			if self.current_char in string.ascii_uppercase:
				token = Token('FACT', self.current_char)
				self.advance()
				return token
			
			self.error()
		return Token('EOF', None)

	def cleaner(self, raw):
		for c in string.whitespace.replace('\n', ''):
			raw = raw.replace(c, '')
		return raw

