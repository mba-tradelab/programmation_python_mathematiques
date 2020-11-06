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

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-3, 3, 0.07)
Y = np.arange(-3, 3, 0.07)
X, Y = np.meshgrid(X, Y)
Z = X * Y / (X**2 + Y**2)
ax.plot_surface(X, Y, Z, linewidth=0.1, rstride=1, cstride=1, cmap=cm.jet)
#ax.plot_surface(X, Y, Z, rstride=1, cstride=1,  color='b')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

