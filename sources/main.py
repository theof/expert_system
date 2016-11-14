import string
from checker import illegal_line
from utils import FACTLIST, ALLOWED_CHARS, crash
from setup import get_base_facts, get_queries, create_rules
from classes import Fact

def cleaner(file):
	cleanfile = []
	i = 0;
	for line in file:
		line = line.replace(" ", "").replace("\t", "")
		if '#' in line:
			line = line[0:line.index('#')]
		j = 0;
		for char in line:
			if char not in ALLOWED_CHARS:
				crash("ES ERROR : Illegal character {} line {} col {}.".format(char, i, j))
			j += 1;
		if not illegal_line(line):
			crash("ES ERROR : Illegal instruction.")
		if len(line):
			cleanfile.append(line)
		i += 1;
	return cleanfile

def evaluate(facts, queries, display):
	result = []
	return_values = {None: '?', True: 'T', False: 'F'}
	for f in queries:
		result.append((f, facts[f].eval(0)))
	
	if not display:
		s = ""
		for r in result:
			s += return_values[r[1]]
		print s
	
	elif display > 0:
		for r in result:
			print "{} : {}".format(r[0], r[1])


def expert_system(raw_file, display=0):
	file = cleaner(raw_file)
	facts =	create_rules(file, FACTLIST)
	facts = get_base_facts(file, facts)
	queries = get_queries(file)
	if display > 1:
		print "".join(file)
	evaluate(facts, queries, display)
