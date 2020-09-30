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

#
# Tous les symboles non internationaux sont omis.
#

from entier import *

def verif_entier(n):
	if n == 1:
		return True
	else:	
		if n % 2 == 0:
			return verif_entier(n/2)
		if n % 5 == 0:
			return verif_entier(n/5)
		return False

class rationnel(object):

	def __init__(self, num =0, denom =1, valide =True):
		valide = valide and (type(num) == int or isinstance(num, entier))
		valide = valide and (type(denom) == int or isinstance(denom, entier))

		if valide:
			if type(num) == int:
				num = entier(num)
			if type(denom) == int:
				denom = entier(denom)

		valide = valide and num.est_valide() and denom.est_valide()

		self.__valide = valide and (denom.valeur() != 0)

		if self.__valide:
			if denom.valeur() < 0:
				num, denom = -num, -denom
			d = pgcd_entiers(num, denom)
			self.__num, self.__denom = num / d, denom / d
		else:
			self.__num, self.__denom = entier(0), entier(1)


	def __str__(self):
		if self.__valide:
			if self.__denom.valeur() == 1:
				return str(self.__num)
			if verif_entier(self.__denom.valeur()):
				return str(self.__float__())
			else:
				return str(self.__num) + "/" + str(self.__denom)
		return "(rationnel invalide)"


	def __float__(self):
		if self.__valide:
			a, b = self.__num.valeur(), self.__denom.valeur()
			return (float(a)/float(b))
		else:
			return float(0)


	def __add__(self, autre):
		if self.__valide and autre.__valide:
			a, b = self.__num, self.__denom
			p, q = autre.__num, autre.__denom
			return rationnel(a*q + b*p, b*q)
		else:
			return rationnel(0, 1, False)


	def __neg__(self):
		if self.__valide:
			a, b = self.__num, self.__denom
			return rationnel(-a, b)
		else:
			return rationnel(0, 1, False)

	def __sub__(self, autre):
		return self.__add__(autre.__neg__())


	def __mul__(self, autre):
		if self.__valide and autre.__valide:
			a, b = self.__num, self.__denom
			p, q = autre.__num, autre.__denom
			return rationnel(a*p, b*q)
		else:
			return rationnel(0, 1, False)


	def __truediv__(self, autre):
		if self.__valide and autre.__valide:
			a, b = self.__num, self.__denom
			p, q = autre.__num, autre.__denom
			return rationnel(a*q, b*p)
		else:
			return rationnel(0, 1, False)


	def __pow__(self, autre):
		if self.__valide and autre.__valide:
			a, b = self.__num, self.__denom
			p, q = autre.__num, autre.__denom
			if (a.valeur() == 0) and (p.valeur() <= 0):
				return rationnel(0, 1, False)

			if p.valeur() < 0:
				p, a, b = -p, b, a

			if b.valeur() < 0:
				a, b = -a, -b

			if q.valeur() == 1:
				return rationnel(a**p, b**p)

		return rationnel(0, 1, False)


if __name__ == "__main__":
	a = rationnel(-23)
	print(a)
	
	b = rationnel(entier(-23))
	print(b)
	
	c = rationnel(4, 0)
	print(c)
	
	d = rationnel(-400, -3760)
	print(d)
	print(float(d))

	d = rationnel(entier(-400), entier(-3760))
	print(d)
	print(float(d))

	x = a + d
	print(x)

	x = c + d
	print(x)

	x = d ** rationnel(-5)
	print(x)

