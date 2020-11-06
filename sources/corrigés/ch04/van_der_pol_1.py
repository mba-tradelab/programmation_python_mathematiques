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

def f(x,t):
    return [x[1], 0.5 * x[1] - x[0] - x[1]**3]

plt.figure()
plt.xlabel('x')
plt.ylabel('y')

t = np.linspace(0, 30, 1000)

CI = [0.01, 0.01]
y = odeint(f, CI, t)
plt.plot(y[:, 0], y[:, 1], color=(1, 0, 0))

for k in np.arange(0, 20, 0.4):

    CI = [0.3*k-3, 3]
    y = odeint(f, CI, t)
    plt.plot(y[:, 0], y[:, 1], color=(k/20, 0.32, 0.48-k/44))

    CI = [0.3*k-3, -3]
    y = odeint(f, CI, t)
    plt.plot(y[:, 0], y[:, 1], color=(k/20, 0.32, 0.48-k/44))

plt.show()

