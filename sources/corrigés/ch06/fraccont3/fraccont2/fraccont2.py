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
# fichier: fraccont2.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/12/04
#
# (tous les symboles non internationaux sont volontairement omis)
#

from outils import *

from rationnel import *



if __name__ == "__main__":
	r = rationnel(4291, 1329)
	print(r)
	
	a = r.fraction_continue()
	print(a)
	
	print(calcul_reduite(a))

