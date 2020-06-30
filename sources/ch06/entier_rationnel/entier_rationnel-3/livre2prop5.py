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
# Eléments d'Euclide: livre 2, proposition 5
#

from rationnel import *

un = rationnel(1)
deux = rationnel(2)

def prod(x, y):
	return x*y

def diff(x, y):
	return ((x+y)/deux)**deux - ((x-y)/deux)**deux

a = rationnel(655399, 100)

b = a + un

for n in range(6):
	u = prod(a, b)
	v = diff(a, b)
	print(u - v)
	a, b = u, a + un

