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
# r\'ecursif terminal
#
def puissance(a, n, p):
	print("appel avec a =", a, "; n =", n, "; p =", p)
	if n == 0:
		return p
	else:
		return puissance(a, n-1, p*a)

print(puissance(2, 10, 1))
