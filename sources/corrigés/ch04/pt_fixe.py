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
print("Point fixe du cosinus")
import numpy as np
from scipy import optimize

print('{} <--- {}'.format(optimize.bisect(lambda x:np.cos(x)-x, 0, 1), "par dichotomie"))
print('{} <--- {}'.format(optimize.newton(lambda x:np.cos(x)-x, 1)   , "par la méthode de Newton"))
print('{} <--- {}'.format(optimize.brentq(lambda x:np.cos(x)-x, 0, 1), "par la méthode de Brent une variante subtile de la méthode de la sécante"))
print('{} <--- {}'.format(optimize.fixed_point(lambda x:np.cos(x), 1), "par la méthode de Steffensen"))
print('{} <--- {}'.format(optimize.fsolve(lambda x:np.cos(x)-x, 1)   , "fonctionne aussi avec des systèmes"))

