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

from string import *

from analex import *
from noeud2 import *
from rationnel import *

def simplifier_parentheses(s):
	if s.startswith('(') and s.endswith(')'):
		s = s[1:-1]
	return s

class arbre(object):
	""" arbre binaire de l'expression """

	def __init__(self, expression_infixe):
		self.__operateurs = []
		self.__pile = []
		e = analyse_lexicale(expression_infixe)
		for jeton in e:
			if jeton[-1] in digits:
				self.__pile.append(noeud2(jeton))
				continue
			if jeton == '(':
				self.__operateurs.append(jeton)
				continue
			if jeton == ')':
				while len(self.__operateurs) > 0 \
					and self.__operateurs[-1] != '(':
					self.nouvelle_operation()
				self.__operateurs.pop(-1)
				continue
			if jeton in "+-*:/^":
				if jeton != '^':
					while len(self.__operateurs) > 0 \
						and self.priorite(self.__operateurs[-1]) >= self.priorite(jeton):
						self.nouvelle_operation()
				self.__operateurs.append(jeton)
				continue
		while len(self.__operateurs) > 0:
			self.nouvelle_operation()
		if len(self.__pile) == 1:
			self.__racine = self.__pile.pop(-1)

	def nouvelle_operation(self):
		sommet = self.__operateurs.pop(-1)
		droite = self.__pile.pop(-1)
		gauche = self.__pile.pop(-1)
		noeud = noeud2(sommet, gauche, droite)
		self.__pile.append(noeud)

	def priorite(self, op):
		precedence = 0
		if op == '+' or op == '-':
			precedence = 1
		if op == '*' or op == ':' or op == '/':
			precedence = 2
		if op == '^':
			precedence = 3
		return precedence

	def prefixe(self):
		return self.__racine.en_chaine_prefixe()

	def infixe(self):
		return simplifier_parentheses(self.__racine.en_chaine_infixe())

	def postfixe(self):
		return self.__racine.en_chaine_postfixe()

	def evaluer(self):
		val = []
		p = self.__racine.en_chaine_postfixe()
		q = p.split('|')
		for n in q:
			if n[-1] in digits:
				val.append(rationnel(int(n)))
				continue
			if n == '+':
				b = val.pop(-1)
				a = val.pop(-1)
				r = a + b
				val.append(r)
				continue
			if n == '-':
				b = val.pop(-1)
				a = val.pop(-1)
				r = a - b
				val.append(r)
				continue
			if n == '*':
				b = val.pop(-1)
				a = val.pop(-1)
				r = a * b
				val.append(r)
				continue
			if n == ':' or n == '/':
				b = val.pop(-1)
				a = val.pop(-1)
				r = a / b
				val.append(r)
				continue
			if n == '^':
				b = val.pop(-1)
				a = val.pop(-1)
				r = a ** b
				val.append(r)
				continue
		return val.pop(-1)

