#! /usr/bin/python
import os, subprocess, tempfile, time, sys, shutil
from test_file import TESTS as test_file

def clean_delete(filename):
	if os.path.isdir(filename):
		shutil.rmtree(filename)
	elif os.path.isfile(filename):
		os.remove(filename)

def create_and_write(filename, content):
	with open(filename, "wr+") as fd:
		fd.write(content)

def try_test(query, keep_tests):
	clean_delete("dummy")
	if keep_tests:
		create_and_write("done/"+keep_tests, query)
	create_and_write("dummy", query)
	sandbox = tempfile.NamedTemporaryFile(prefix='.', dir='.')
	sandbox.write(query)
	sandbox.seek(0)
	try:
		out = subprocess.check_output(["./ES.py", sandbox.name])
	except:
		print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!" + '\033[91m' + " subprocess failed " + '\033[0m' + "!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
		return None
	sandbox.close()
	return out		

def test_one(name, test, break_on_fail, keep_tests, verbose):
	ok = 0
	for each in test:
		subname = each[0]
		answer = each[1]
		query = each[2]
		if keep_tests:
			keep_tests = name+'_'+subname
		print name, ">>>>", subname, 
		result = try_test(query, keep_tests)
		if result != answer:
			print '\033[91m' + "FAIL" + '\033[0m'
			if verbose:
				print "\n"+query+"\n\nexpected: "+repr(answer)+"\nreturned: "+repr(result)+"\n\n--------------------\n\n"
			if break_on_fail:
				exit(0)
		else:
			ok += 1
			print '\033[92m' + "OK" + '\033[0m'
	return ok


def main():
	i = 0;
	break_on_fail = 0
	keep_tests = 0
	verbose = 0
	for arg in sys.argv:
		if arg[0] == '-':
			break_on_fail += arg.count('b')
			keep_tests += arg.count('k')
			verbose += arg.count('v')

	print "********************\n*                  *\n*      ES_test     *\n*                  *\n********************\n"

	ko = 0
	ok = 0
	if keep_tests:
		clean_delete("done")
		os.makedirs("done")	
	for test in test_file:
		ko += len(test_file[test])
		ok += test_one(test, test_file[test], break_on_fail, keep_tests, verbose)
	ko = ko - ok
	
	print "\nOK :", ok, "\nKO :", ko

if __name__ == "__main__":
	main()