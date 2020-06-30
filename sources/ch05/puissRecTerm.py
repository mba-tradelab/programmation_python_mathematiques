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

def puissance_rec_term(a, n, p):
	print("appel avec a =", a, "; n =", n, "; p =", p)
	if n == 0:
		return p
	else:
		return puissance_rec_term(a, n-1, p*a)

def puissance(a, n):
	return puissance_rec_term(a, n, 1)

print(puissance(2, 10))
