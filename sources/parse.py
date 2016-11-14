import string
from utils import all_checks, all_cleans, find_end, find_part, explode_parentheses, make_not_rule, crash

def explode_symbols(exploded):
	total = []
	lasts = {}

	for part in exploded:
		copy_part = part
		done = []

		if len(part) == 1:
			a, s, b = part[0], "", ""
			done = [a]
			part = ""

		while len(part) > 0:
			token_not = False
			
			# First Half
			if part[0] == '!':
				token_not = True
				part = part[1:]
			if part[0] == '(':
				a = '#'+str(find_part(part, total, lasts))
				part = part[find_end(part)+1:]
			elif len(done) == 0:
				a = part[0]
				part = part[1:]
			else:
				a = "#"+str(len(total) + len(done) - 1)
			
			# X + Y 
			if not token_not:
				# Symbol
				s = part[0]
				part = part[1:]
				
				# Second Half
				if part[0] == '!':
					done.append(make_not_rule(part, total, lasts))
					b = '#'+str(len(done) + len(total) - 1)
					part = part[find_end(part)+1:]
				elif part[0] == '(':
					b = '#'+str(find_part(part, total, lasts))
					part = part[find_end(part)+1:]
				else:
					b = part[0]
					part = part[1:]
				done.append(a+s+b)
			
			# !X
			else:
				done.append('!'+a)
		# if len(done):
		lasts[copy_part] = done[-1]
		for i in done:
			total.append(i)

	return total


def parse_rules(line):
	if not all_checks(line):
		crash("ES ERROR : Parsing failed on line : {}.".format(line))
	line = all_cleans(line)
	splitted = list(explode_parentheses(line))
	rules = list(explode_symbols(splitted))
	return rules
