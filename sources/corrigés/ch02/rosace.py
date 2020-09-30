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

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 1 + int(38*np.pi), 1000)
r = 1 +  np.cos(20 * theta / 19) / 3

plt.polar(theta, r, linewidth=0.8)
plt.show()
