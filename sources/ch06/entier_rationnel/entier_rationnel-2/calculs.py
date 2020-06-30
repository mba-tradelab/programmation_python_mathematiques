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

#
# quelques constantes
#
zero = rationnel()
un = rationnel(1)
deux = rationnel(2)
trois = rationnel(3)
six = rationnel(6)
cent = rationnel(100)
mille = rationnel(1000)
millieme = rationnel(1, 1000)



def valeur_approchee(r):
	""" donne une valeur approchée par un réel machine """
	a = float(r.get_num().valeur())
	b = float(r.get_denom().valeur())
	return (a/b)



def babylone(a):
	""" algorithme de Babylone (approx. de la racine carrée) """
	global un, deux
	r = un
	for n in range(5):
		r = (r + a/r)/deux
	return r



if __name__ == "__main__":

	print("2^1000")
	print(deux ** mille)
	print()

	print("une approximation de pi par la formule de Wallis")
	pi = deux
	for n in range(1, 200):
		pi *= rationnel((2*n)**2, (2*n-1)*(2*n+1))
	print(pi)
	print(valeur_approchee(pi))
	print()

	print("une approximation de pi par un décimal")
	pi = rationnel(3141592654, 1000000000)
	print(pi)
	print(valeur_approchee(pi))
	print(float(pi))
	print()

	print("une approximation de la racine carrée de 50")
	x = babylone(rationnel(50))
	print(x)
	print(valeur_approchee(x))
	print()

