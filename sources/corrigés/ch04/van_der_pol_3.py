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

t = np.linspace(0, 40, 1000)


plt.figure()
plt.subplots_adjust(hspace=0.25,wspace=0.3)

CI = [0.01, 0.01]
y = odeint(f, CI, t)

plt.subplot(2, 2, 1)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.plot(t, y[:, 0], color=(1, 0, 0))

plt.subplot(2, 2, 3)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.plot(t, y[:, 1], color=(1, 0, 0))

plt.subplot(1, 2, 2)
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.plot(y[:, 0], y[:, 1], color=(1, 0, 0))

for k in np.arange(0, 20, 4):

    CI = [0.3*k-3, 3]
    y = odeint(f, CI, t)
    plt.subplot(2, 2, 1)
    plt.plot(t, y[:, 0], color=(k/20, 0.32, 0.48-k/44))
    plt.subplot(2, 2, 3)
    plt.plot(t, y[:, 1], color=(k/20, 0.32, 0.48-k/44))
    plt.subplot(1, 2, 2)
    plt.plot(y[:, 0], y[:, 1], color=(k/20, 0.32, 0.48-k/44))

    CI = [3-0.3*k, -3]
    y = odeint(f, CI, t)
    plt.subplot(2, 2, 1)
    plt.plot(t, y[:, 0], color=(k/20, 0.32, 0.48-k/44))
    plt.subplot(2, 2, 3)
    plt.plot(t, y[:, 1], color=(k/20, 0.32, 0.48-k/44))
    plt.subplot(1, 2, 2)
    plt.plot(y[:, 0], y[:, 1], color=(k/20, 0.32, 0.48-k/44))

plt.show()
