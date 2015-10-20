#!/usr/bin/env python3

import sys, collections

#################################################################

class Simple:

	def __init__(self, need):
		self.need = need


class And:

	def __init__(self, left, right):
		if (left.need == 1 and right.need == 1):
			self.need = 1
		else:
			self.need = -1 


class Or:

	def __init__(self, left, right):
		if (right.need == 1 or left.need == 1):
			self.need = 1
		else:
			self.need = -1


class Xor:

	def __init__(self, left, right):
		if (right.need == 1 and left.need == -1):
			self.need = 1
		elif (right.need == -1 and left.need == 1):
			self.need = 1
		else:
			self.need = -1

#################################################################
