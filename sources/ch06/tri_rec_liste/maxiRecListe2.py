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

from random import *

#
# remplissage de la liste avec des nombres aleatoires
#
def initialiser(l, n):
	if n > 0:
		l.append(randrange(1, 100))
		initialiser(l, n-1)

#
# recherche recursive du maximum
#
def maxi_rec(l):
	if len(l) > 1:
		maxi = maxi_rec(l[:-1])
		if maxi > l[-1]:
			return maxi
		else:
			return l[-1]
	else:
		return l[0]

if __name__ == "__main__":

	#
	# la liste est initialement vide
	#
	liste = []
	initialiser(liste, 10)

	print(liste)
	print(maxi_rec(liste))
