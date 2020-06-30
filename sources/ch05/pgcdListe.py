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
# pgcd de deux entiers naturels
#
def pgcd(a, b):
	if b == 0:
		return a
	else:
		return pgcd(b, (a % b))

#
# pgcd d'une liste
#
def pgcd_liste(l):
	if len(l) == 1:
		return l[0]
	else:
		return pgcd(l[0], pgcd_liste(l[1:]))

print(pgcd_liste([4*5*6*37, 3*5*6*37, 3*4*6*37, 3*4*5*37]))

