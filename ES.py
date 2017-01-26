#!/usr/bin/env python3
import sys
from lexer import Lexer, Token
from parser import Parser
from interpreter import Interpreter

def expert_system(file):
	try:
		lexer = Lexer(file)
		parser = Parser(lexer)
		interpreter = Interpreter(parser)
		interpreter.interpret()
	except Exception as e:
		if 'maximum recursion depth exceeded while calling a Python object' == str(e):
			print('ES : Too Deep.')
		elif 'ES : Invalid character : ' in str(e) or 'ES : Invalid syntax :' in str(e):
			print(e)
		else:
			raise e

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as fd:
		expert_system(fd.read())
