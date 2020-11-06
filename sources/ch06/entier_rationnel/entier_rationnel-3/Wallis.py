#!/usr/bin/env python3
# -*- coding:utf-8 -*-

########################################################################
# (C) Alexandre Casamayou-Boucau, Pascal Chauvin, Guillaume Connan     #
#                                                                      #
# Complément de l'ouvrage :                                            #
# Programmation en Python pour les mathématiques                       #
# Editeur : Dunod                   -        Collection : Sciences Sup #
# ISBN-13: 978-2100738311           -                  Licence : GPLv2 #
########################################################################

from entier import *
from rationnel import *

#
# Formule de Wallis (approximation du nombre pi)
#
p = rationnel(entier(2))
for n in range(1, 20):
	p *= rationnel((2*n)**2, (2*n-1)*(2*n+1))
print("Une approximation du nombre pi est", p)
print(float(p))

