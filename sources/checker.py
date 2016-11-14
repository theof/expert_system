import string

def init_checkers():

	# before
	cb = {'!': lambda n: n in string.ascii_uppercase+'('}
	for c in '=>?':
		cb[c] = lambda n: False
	for c in string.ascii_uppercase+')':
		cb[c] = lambda n: n in ')+|^=\n\0'
	for c in '|+^(':
		cb[c] = lambda n: n in string.ascii_uppercase+'!('

	# after
	ca = {'+': lambda n: n in string.ascii_uppercase}
	for c in string.ascii_uppercase:
		ca[c] = lambda n: n in '+\0'
	for c in '|^()!':
		ca[c] = lambda n: False

	# ?
	ci = {}
	for c in string.ascii_uppercase+'?':
		ci[c] = lambda n: n in string.ascii_uppercase+'\0'
	for c in '=>|+^':
		ci[c] = lambda n : False

	# =
	ce = {}
	for c in string.ascii_uppercase+'=':
		ce[c] = lambda n: n in string.ascii_uppercase+'\0'
	for c in '?>|+^':
		ce[c] = lambda n : False

	return cb, ca, ci, ce


def one(line, checker):
	r = []
	if not bool(line):
		return [False]
	for i, c in enumerate(line+'\0'):
		if i+1 < len(line):
			n = (line+'\0')[i+1]
			r.append(checker[c](n))
		else:
			return r

def illegal_line(line):
	cb, ca, ci, ce = init_checkers()
	line = line[:-1]
	if '=>' in line:
		before, _, after = line.partition('=>')
		return all(one(before, cb) + one(after, ca))
	elif '?' in line:
		return all(one(line, ci) + [line.count('?') is 1, line[0] is '?'])
	elif '=' in line:
		return all(one(line, ce) + [line.count('=') is 1, line[0] is '='])