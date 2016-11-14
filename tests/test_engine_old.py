#! /usr/bin/python
import os, subprocess, tempfile, time, sys, shutil
from test_file import TESTS as t

VERBOSE, BREAK_ON_FAIL, KEEP_TEST = 0, 0, 0
ok, ko = 0, 0

def keep(query, filename):
	if os.path.isdir("tests/done"):
		shutil.rmtree("tests/done")
	elif os.path.isfile("tests/done"):
		os.remove("tests/done")
	os.makedirs("tests/done")	
	with open("tests/done/"+filename, "wr+") as fd:
		fd.write(query)
		fd.close()

def get_res(query, keep_tests=False):
	if os.path.isfile("dummy"):
		os.remove("dummy")
	if keep_tests:
		keep(query, keep_tests)
	dummy = open("dummy", "wr+")
	dummy.write(query)
	dummy.close
	sandbox = tempfile.NamedTemporaryFile(prefix='.', dir='.')
	sandbox.write(query)
	sandbox.seek(0)
	try:
		out = subprocess.check_output(["./ES.py", sandbox.name])
	except:
		print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
		print "!!!!!" + '\033[91m' + " subprocess failed " + '\033[0m' + "!!!!!"
		print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
		return None
	sandbox.close()
	return out

def goa_test(name, test):
	global ok, ko

	for u in test:
		returned = get_res(u[2], False if not KEEP_TEST else name+'_'+u[0])
		print name, ">>>", u[0], 
		if returned != u[1]:
			ko += 1
			print '\033[91m' + "FAIL" + '\033[0m'
			if VERBOSE and returned:
				print ""
				print u[2]
				print ""
				print "expected:", repr(u[1])
				print "returned:", repr(returned)
				print ""
				print "-"*20
				print ""
			if BREAK_ON_FAIL:
				exit(0)
		else:
			ok += 1
			print '\033[92m' + "OK" + '\033[0m'

def main():
	global ok, ko, VERBOSE, BREAK_ON_FAIL, KEEP_TEST

	print "*"*20
	print "*                  *"
	print "*      ES_test     *"
	print "*                  *"
	print "*"*20
	print ""

	if len(sys.argv) == 2 and sys.argv[1][0] == '-':
		VERBOSE = "v" in sys.argv[1]
		BREAK_ON_FAIL = "b" in sys.argv[1]
		KEEP_TEST = "k" in sys.argv[1]
	for o in t:
		goa_test(o, t[o])
	print "\nOK : {}\nKO : {}\n".format(ok, ko)

main()
