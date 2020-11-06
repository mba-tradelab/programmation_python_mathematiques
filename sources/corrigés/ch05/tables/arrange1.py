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
# fichier: arrange1.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/11/27
#
# (tous les symboles non internationaux sont volontairement omis)
#

def arrangement(k, n):
	if n >= k:
		return n * arrangement(k, n - 1)
	else:
		return 1



print(arrangement(7, 10))

