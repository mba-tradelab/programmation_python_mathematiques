#!/usr/bin/python3:
#-*- coding: Utf-8 -*-

########################################################################
# (C) Alexandre Casamayou-Boucau, Pascal Chauvin, Guillaume Connan     #
#                                                                      #
# Complément de l'ouvrage :                                            #
# Programmation en Python pour les mathématiques                       #
# Editeur : Dunod                   -        Collection : Sciences Sup #
# ISBN-13: 978-2100738311           -                  Licence : GPLv2 #
########################################################################


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-15, 15, 150)
y = np.sin(x) / x

plt.plot(x, y)
plt.show()

