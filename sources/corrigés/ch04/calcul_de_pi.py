#!/usr/bin/python3
#-*- coding: Utf-8 -*-

########################################################################
# (C) Alexandre Casamayou-Boucau, Pascal Chauvin, Guillaume Connan     #
#                                                                      #
# Complément de l'ouvrage :                                            #
# Programmation en Python pour les mathématiques                       #
# Editeur : Dunod                   -        Collection : Sciences Sup #
# ISBN-13: 978-2100738311           -                  Licence : GPLv2 #
########################################################################

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import numpy as np
from scipy import integrate

I = integrate.quad(lambda x: np.sqrt(1-x**2), 0, 0.5)
J = integrate.quad(lambda x: np.sqrt(1-x**2), 0, 1)

print('             4*I = {}'.format(4*J[0]))
print('12*(J-sqrt(3)/8) = {}'.format(12*(I[0]-np.sqrt(3)/8)))
print('        numpy.pi = {}'.format(np.pi))


