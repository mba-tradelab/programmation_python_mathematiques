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
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#f = lambda x, t: 1 + t**2 * x**2 if abs(x) < 5 else None
def f(x, t):
    if abs(x) < 5:
        return 1 + t**2 * x**2
    else:
        None

p = plt.figure()

for k in np.arange(-4, 4, 0.2):

    t = np.linspace(0, 4, 1000)
    x = odeint(f, k, t)
    plt.plot(t, x[:, 0], color='b')

    t = np.linspace(0, -4, 1000)
    x = odeint(f, k, t)
    plt.plot(t, x[:, 0], color='b')

plt.ylim(-4, 4)
plt.show()

