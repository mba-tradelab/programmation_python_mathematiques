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
# fichier: primliste.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/11/27
#
# (tous les symboles non internationaux sont volontairement omis)
#

import random

from outils import *

def recherche(x, liste):
	if len(liste) == 0:
		return False

	if tete(liste) == x:
		return True

	return recherche(x, suite(liste))



if __name__ == "__main__":
	hasard = [random.randrange(50) for t in range(20)]

	print(longueur(hasard)) # donne 20
	print(hasard)

	print(recherche(tete(hasard), hasard)) # donne True
	print(recherche(200, hasard)) # donne False

	print(tete(hasard))
	print(suite(hasard))

	print(debut(2, hasard))
	print(coupe(2, hasard))

	hasard = [random.randrange(50) for t in range(10)]
	print(hasard)

	n = longueur(hasard)
	for i in range(n):
		print(debut(1, hasard))
		hasard = coupe(1, hasard)

