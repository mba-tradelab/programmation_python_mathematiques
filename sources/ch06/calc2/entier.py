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

class entier(object):
	""" nombre entier """

	def __init__(self, valeur =0, valide =True):
		if not valide:
			valeur = 0
		self.__valide = valide
		self.__valeur = valeur
		
	def __str__(self):
		if self.__valide:
			return str(self.__valeur)
		else:
			return "(entier invalide)"

	def est_valide(self):
		return self.__valide

	def valeur(self):
		return self.__valeur

	def __add__(self, autre):
		if self.__valide and autre.__valide:
			a = self.__valeur
			b = autre.__valeur
			return entier(a + b)
		else:
			return entier(0, False)

	def __neg__(self):
		if self.__valide:
			a = self.__valeur
			return entier(-a)
		else:
			return entier(0, False)

	def __sub__(self, autre):
		return self.__add__(autre.__neg__())

	def __mul__(self, autre):
		if self.__valide and autre.__valide:
			a = self.__valeur
			b = autre.__valeur
			return entier(a * b)
		else:
			return entier(0, False)

	def __truediv__(self, autre):
		if not(self.__valide and autre.__valide):
			return entier(0, False)
			
		if autre.__valeur == 0:
			return entier(0, False)
			
		a = self.__valeur
		b = autre.__valeur
		if a % b != 0:
			return entier(0, False)
			
		return entier(a // b)

	def __div__(self, autre):
		return self.__truediv__(autre)

	def __pow__(self, autre):
		if not(self.__valide and autre.__valide):
			return entier(0, False)
			
		a = self.__valeur
		n = autre.__valeur
		if a == 0:
			if n <= 0:
				return entier(0, False)
			else:
				return entier()
				
		if n < 0:
			return entier(0, False)
			
		p = 1
		while n > 0:
			if n % 2 == 1:
				p *= a
			n //= 2
			a *= a
		return entier(p)

def pgcd_naturels(a, b):
	if b == 0:
		return a
	else:
		return pgcd_naturels(b, a % b)

def pgcd_entiers(a, b):
	if a.est_valide() and b.est_valide():
		return entier(pgcd_naturels(abs(a.valeur()), abs(b.valeur())))
	else:
		return entier(0, False)

if __name__ == "__main__":
	
	a = entier(-232)
	print(a)
	print((a.valeur()))
	print((a.est_valide()))
	
	b = entier(4)

	x = a - b
	print(x)

	x = a / b
	print(x)

	x = a / (b - b)
	print(x)

	a = entier(23)
	b = entier(9)
	x = a ** b
	print(x)

	b = entier(-4)
	x = a ** b
	print(x)

	a = entier(23*80*9)
	b = entier(40*3*37)
	x = pgcd_entiers(a, b)
	print(x)

