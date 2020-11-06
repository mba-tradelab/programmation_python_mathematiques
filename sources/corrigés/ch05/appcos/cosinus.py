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
# fichier: cosinus.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/11/26
#
# (tous les symboles non internationaux sont volontairement omis)
#

import math

#
# d\'eveloppement limit\'e de cos
#
def developpement_lim_cos(x):
	return (x - (x**2)/2 + (x**4)/24 - (x**6)/720 + (x**8)/40320)



#
# approximation (r\'ecursive) de cos(x):
# le param\`etre "epsilon" d\'efinit la valeur absolue de x
# en dessous de laquelle on utilise le d\'eveloppement limit\'e
#
def cosinus(x, epsilon):
	if abs(x) < epsilon:
		return developpement_lim_cos(x)
	else:
		return (2 * cosinus(x/2, epsilon)**2 - 1)



#
# test de la fonction cosinus()
#
def test_cosinus(x, epsilon =0.000001):
	print("pour x = {0} (epsilon = {1}):".format(x, epsilon))

	print("    cos :", math.cos(x))
	print("cosinus :", cosinus(x, epsilon))
	print()

