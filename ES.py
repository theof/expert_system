#! /usr/bin/python
import sys
sys.path.append("sources")
from main import expert_system

def main(argv):
	i = 1
	display = 0
	while i < len(argv) and argv[i][0] == '-':
		display += argv[i].count('v')
		i += 1
	if i >= len(argv):
		print "ES ERROR : At least one file required."
		print "Usage : ES.py [-vv] file"
		exit(0);
	try :
		file = open(argv[i], "r")
	except IOError:
		print("ES ERROR : Invalid file given : {}.".format(argv[i]))
	else:
		with file:
			expert_system(file, display)

if (__name__ == "__main__"):
	main(sys.argv)
