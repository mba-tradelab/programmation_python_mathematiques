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
# fichier: partent.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/11/27
#
# (tous les symboles non internationaux sont volontairement omis)
#

import sys
sys.setrecursionlimit(100000)



def __partie_entiere_racine_rec(k, x):
	if k**2 > x:
		return (k - 1)
	else:
		return __partie_entiere_racine_rec(k + 1, x)
		
		
		
def partie_entiere_racine(x):
	return __partie_entiere_racine_rec(1, x)
	
	

if __name__ == "__main__":
	print(partie_entiere_racine(17))

	print(partie_entiere_racine(36703))

