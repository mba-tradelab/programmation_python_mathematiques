#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
# (C) Alexandre Casamayou-Boucau, Pascal Chauvin, Guillaume Connan     #
#                                                                      #
# Complément de l'ouvrage :                                            #
# Programmation en Python pour les mathématiques                       #
# Editeur : Dunod                   -        Collection : Sciences Sup #
# ISBN-13: 978-2100738311           -                  Licence : GPLv2 #
########################################################################

from rationnel import *

class expression(object):
	""" expression à évaluer """

	def __init__(self, s):
		self.__source = s
		self.__n = len(s)
		self.__i = 0
		self.__err = 0
		self.__val = 0

	def __str__(self):
		s = ""
		for ch in self.__source:
			if not str.isspace(ch):
				s += ch
		return s

	def erreur(self, e):
		if self.__err == 0:
			self.__err = e

	def erreur_existe(self):
		if self.__err == 0:
			return False
		else:
			return True

	def aucune_erreur(self):
		return not self.erreur_existe()

	def valeur(self):
		self.evaluer()
		return self.__val

	def evaluer(self):
		self.__ch = self.suivant()
		if self.__ch == '{':
			self.__ch = self.suivant()
			self.__val = self.expr()
			self.__ch = self.suivant()
			if self.__ch != '}':
				self.erreur(2) # manque une "}"
		else:
			self.erreur(1) # manque une "{"

	def suivant(self):
		while self.__i < self.__n:
			t = self.__source[self.__i]
			self.__i += 1
			if str.isspace(t):
				continue
			else:
				return t
		return '\0'

	def prochain_lu(self):
		while self.__i < self.__n:
			t = self.__source[self.__i]
			if str.isspace(t):
				self.__i += 1
			else:
				return t
		return '\0'

	def suivant_est(self, t):
		if self.prochain_lu() == t:
			return True
		else:
			return False

# expr ::= expr1 '+' expr1 | expr1 '-' expr1 | expr1
	def expr(self):
		if self.erreur_existe():
			return 0
		t = self.expr1()
		while self.suivant_est('+') or self.suivant_est('-'):
			self.__ch = self.suivant()
			if self.__ch == '+':
				self.__ch = self.suivant()
				t += self.expr1()
			else:
				if self.__ch == '-':
					self.__ch = self.suivant()
					t -= self.expr1()
		return t

# expr1 ::= expr2 '*' expr2 | expr2 '/' expr2 | expr2
	def expr1(self):
		if self.erreur_existe():
			return 0
		t = self.expr2()
		while self.suivant_est('*') or self.suivant_est('/') or self.suivant_est(':'):
			self.__ch = self.suivant()
			if self.__ch == '*':
				self.__ch = self.suivant()
				t *= self.expr2()
			else:
				if self.__ch == '/' or self.__ch == ':':
					self.__ch = self.suivant()
					t /= self.expr2()
					if not t.est_valide():
						self.erreur(7) # tentative de diviser par 0
		return t

# expr2 ::= '-' expr3 | expr3
	def expr2(self):
		if self.erreur_existe():
			return 0
		negate = False
		while self.__ch == '-':
			negate = not negate
			self.__ch = self.suivant()
		t = self.expr3()
		if negate:
			return -t
		else:
			return t

# expr3 ::= expr4 '^' expr2 | expr4
	def expr3(self):
		if self.erreur_existe():
			return 0
		t = self.expr4()
		if self.suivant_est('^'):
			self.__ch = self.suivant()
			self.__ch = self.suivant()
			k = self.expr2()
			if not k.est_valide():
				self.erreur(8) # exposant invalide 
			t = t ** k
		return t

# expr4 ::= <naturel> | '(' expr ')'
	def expr4(self):
		if self.erreur_existe():
			return 0
		if str.isdigit(self.__ch):
			t = self.naturel()
			return rationnel(int(t))
		if self.__ch == '(':
			self.__ch = self.suivant()
			t = self.expr()
			self.__ch = self.suivant()
			if self.__ch == ')':
				return t
			else:
				self.erreur(10) # manque une ")"
		else:
			self.erreur(9) # manque une "("
		return 0

# naturel ::= ('0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9')*
	def naturel(self):
		n = int(self.__ch)
		x = self.prochain_lu()
		while str.isdigit(x):
			n = n * 10 + int(x)
			self.__ch = self.suivant()
			x = self.prochain_lu()
		return n

