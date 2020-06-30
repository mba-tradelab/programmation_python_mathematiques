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


def f(x, t):
    alpha = 0.5
    return [x[1], (alpha**2 - t**2) / t**2 * x[0] - x[1] / t]

plt.figure()
plt.xlabel('t')
plt.ylabel('x')

t = np.linspace(0.001, 18.9, 1000)

for k in np.arange(0, 20, 0.4):

    CI = [0.2*k-2, 0]
    x = odeint(f, CI, t)
    plt.plot(t, x[:, 0], color=(k/20, 0.32, 0.48-k/44))

plt.show()

