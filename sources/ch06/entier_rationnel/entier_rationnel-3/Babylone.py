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

from rationnel import *

#
# Algorithme de Babylone
#
a = rationnel(5) # on choisit a = 5

deux = rationnel(2)

r = rationnel(1)
for n in range(5):
	r = (r + a/r)/deux

print("Une approximation rationnelle de la racine carree de", a, "est", r)
print(float(r))

