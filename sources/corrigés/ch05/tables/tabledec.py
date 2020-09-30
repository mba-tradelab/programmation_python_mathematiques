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
# fichier: tabledec.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/11/27
#
# (tous les symboles non internationaux sont volontairement omis)
#

def table_decroissante(multiplicande, multiplicateur):
	print("{0:4d} * {1:4d} = {2}".format(\
		multiplicande, multiplicateur, multiplicande * multiplicateur))

	if multiplicateur > 0:
		table_decroissante(multiplicande, multiplicateur - 1)



table_decroissante(7, 10)
