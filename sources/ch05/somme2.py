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
# somme recursive terminale (avec accumulateur)
#
def somme_rec(acc, n):
	if n > 0:
		return somme_rec(acc + n, n - 1)
	else:
		return acc

#
# somme (enveloppe)
#
def somme(n):
	return somme_rec(0, n)

print(somme(10))

