import string
from classes import Fact

def crash(msg):
	print msg
	exit(0)

FACTLIST = {
	"A": Fact("A"),
	"B": Fact("B"),
	"C": Fact("C"),
	"D": Fact("D"),
	"E": Fact("E"),
	"F": Fact("F"),
	"G": Fact("G"),
	"H": Fact("H"),
	"I": Fact("I"),
	"J": Fact("J"),
	"K": Fact("K"),
	"L": Fact("L"),
	"M": Fact("M"),
	"N": Fact("N"),
	"O": Fact("O"),
	"P": Fact("P"),
	"Q": Fact("Q"),
	"R": Fact("R"),
	"S": Fact("S"),
	"T": Fact("T"),
	"U": Fact("U"),
	"V": Fact("V"),
	"W": Fact("W"),
	"X": Fact("X"),
	"Y": Fact("Y"),
	"Z": Fact("Z"),
}

ALLOWED_CHARS = string.ascii_uppercase + "()!+|^=>?\n"

def make_not_rule(part, total, lasts):
	target = part[2:find_end(part)]
	if target in total:
		return "!#"+str(total.index(target))
	else:
		return "!#"+str(total.index(lasts[target]))

def explode_parentheses(string):
	stack = [0]
	for i, c in enumerate(string):
		if c == '(':
			stack.append(i)
		elif c == ')' and stack:
			start = stack.pop()
			yield string[start + 1:i]
	start = stack.pop()
	yield string[start:i+1]

def clean_useless_parentheses(s):
	while (s[0] == '(' and find_end(s) == len(s)-1):
		s = s[1:-1]
	found_useless = True
	while found_useless:
		found_useless = False
		l = list(explode_parentheses(s))
		i = 0
		for i in range(0, len(l)):
			if '(('+l[i]+'))' in s:
				s = s.replace('('+l[i]+')', l[i])
				found_useless = True
				break
	return s

def clean_not(s):
	for i in range(0, len(s)-1):
		if s[i] == '!' and s[i+1] != '(':
			s = s[:i+1] + '(' + s[i+1] + ')' + s[i+2:]
	return s

def all_cleans(s):
	s = clean_useless_parentheses(s)
	s = clean_not(s)
	return s

def find_end(string): 
	deepness = 0
	for i, c in enumerate(string):
		if c == '(':
			deepness += 1
		elif c == ')':
			deepness -= 1
			if deepness == 0:
				return i

def find_part(needle, haystack, magnet):
	end = find_end(needle)
	needle = needle[1:end]
	return haystack.index(magnet[needle])

def check_parentheses(test):
	if test.count('(') != test.count(')'):
		return False
	deepness = 0
	pos = []
	i = 0;
	for c in test:
		if c == '(':
			deepness += 1
			if deepness == 1 and len(pos) == 0:
				pos.append(i)
		elif c == ')':
			deepness -= 1
			if deepness == 0 and len(pos) == 1:
				pos.append(i)
		if deepness < 0:
			return False
		i += 1;
	return True

def all_checks(t):
	if not len(t):
		return False
	elif not check_parentheses(t):
		return False
	return True
