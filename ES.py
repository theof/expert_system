#!/usr/bin/env python3
import sys
from lexer import Lexer, Token
from parser import Parser
from interpreter import Interpreter

def expert_system(file):
	lexer = Lexer(file)
	parser = Parser(lexer)
	interpreter = Interpreter(parser)
	interpreter.interpret()

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as fd:
		expert_system(fd.read())
