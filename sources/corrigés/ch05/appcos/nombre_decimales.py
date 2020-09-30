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
# fichier: nombre_decimales.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/11/26
#
# (tous les symboles non internationaux sont volontairement omis)
#

def nombre_decimales(a, b):
	if float(a) + float(b) == float(a):
		return 0
	else:
		return 1 + nombre_decimales(a, b/10)



print(nombre_decimales(1, 1))

