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

class calcul(object):
	""" évaluation d'une expression postfixée """

	def __init__(self):
		self.__pile = []

	def empiler(self, arg):
		self.__pile.append(arg)

	def depiler(self):
		if len(self.__pile) > 0:
			return self.__pile.pop(-1)
		else:
			return rationnel(0, 1, False)

	def additionner(self):
		b = self.depiler()
		a = self.depiler()
		r = a + b
		self.empiler(r)

	def soustraire(self):
		b = self.depiler()
		a = self.depiler()
		r = a - b
		self.empiler(r)

	def multiplier(self):
		b = self.depiler()
		a = self.depiler()
		r = a * b
		self.empiler(r)

	def diviser(self):
		b = self.depiler()
		a = self.depiler()
		r = a / b
		self.empiler(r)

	def elever_puissance(self):
		b = self.depiler()
		a = self.depiler()
		r = a ** b
		self.empiler(r)

	def resultat(self):
		return self.depiler()

	def reponse(self):
		return self.resultat()

if __name__ == "__main__":
	c = calcul()
	c.empiler(rationnel(45, 70))
	c.empiler(rationnel(56, -100))
	c.multiplier()

	resultat = c.depiler()
	print(resultat)
	print(resultat.est_valide())

