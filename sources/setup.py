from utils import crash
from classes import Rule, RuleAB, RuleNot, Fact
from string import ascii_uppercase
from parse import parse_rules
import re, string

def get_base_facts(file, facts):
	for line in file:
		if line[0] == '=':
			for char in line[1:]:
				if char in facts.keys():
					facts[char].values = [True]
				elif char != '\n':
					crash("ES ERROR : Illegal character in the initial facts line.")
	return facts

def get_queries(file):
	queries = ""
	for line in file:
		if line[0] == '?':
			for char in line[1:]:
				if char[0] in ascii_uppercase:
					queries += char[0]
				elif char != '\n':
					crash("ES ERROR : Illegal character in the queries line.")
	return queries

def split_parsed(s):
	if len(s) == 1:
		return s, False, False
	finds = re.findall("^(?:#([0-9]*)|([A-Z])|!#([0-9]*))([+|^])?(?:#([0-9]*)|([A-Z]))?", s)
	if not len(finds):
		return False, False, False
	A = [x for x in finds[0][:3] if len(x)][0] if any(finds[0][:3]) else False
	if A and all([x in string.digits for x in A]):
		A = int(A)
	S = finds[0][3] if len(finds[0][3]) else '!'
	B = [x for x in finds[0][4:] if len(x)][0] if S != '!' else False
	if B and all([x in string.digits for x in B]):
		B = int(B)
	return A, S, B

def assign(rule, rule_dict, facts):
	if type(rule) is int:
		return rule_dict[rule]
	else:
		return facts[rule]

def update_fact(fact, rule):
	if fact.virgin:
		fact.virgin = False
		fact.values = [rule]
		return fact
	else:
		fact.values.append(rule)
		return fact

def create_rules(file, facts):
	for line in file:
		if "=>" in line:
			rule_dict = {}
			i = 0
			raw_rule, _, conclusion = line.partition("=>")
			rule = parse_rules(raw_rule)
			conclusion = conclusion[:-1]
			for part in rule:
				A, S, B = split_parsed(part)
				if A is not False and S is not False and B is not False:
					A = assign(A, rule_dict, facts)
					B = assign(B, rule_dict, facts)
					rule_dict[i] = RuleAB(A, B, S) 
				elif A is not False and S == '!' and B is False:
					rule_dict[i] = RuleNot(assign(A, rule_dict, facts))
				elif A:
					rule_dict[i] = Rule(assign(A, rule_dict, facts))
				i += 1
			for c in conclusion.split('+'):
				facts[c] = update_fact(facts[c], rule_dict[i-1])
	return facts
