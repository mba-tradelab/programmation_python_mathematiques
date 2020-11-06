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

import numpy

class ODE(object):
    def __init__(self, f, h):
        self.f = lambda u, t: numpy.asarray(f(u, t), float)   # 1ère modification
        self.h = h

    def iteration(self):
        raise NotImplementedError

    def CI(self, t0, x0):
        self.liste = [[t0, numpy.asarray(x0, float)]]         # 2ème modification
        self.k = 0

    def resolution(self, a, b, termine=None):
        if termine is None:
            termine = lambda x: False
        self.indice = -1
        while (self.liste[-1][0] <= b and
                not termine(self.liste[-1][1])):
            self.liste.append(self.iteration())
        self.h = - self.h
        self.indice = 0
        while (self.liste[0][0] >= a and
                not termine(self.liste[0][1])):
            self.liste.insert(0, self.iteration())
        return self.liste

class Euler(ODE):
    def iteration(self):
        f, h = self.f, self.h
        [t, x] = self.liste[self.indice]
        return [t + h, x + h * f(t, x)]

class RK4(ODE):
    def iteration(self):
        f, h = self.f, self.h
        [t, x] = self.liste[self.indice]
        k1 =  h * f(t, x)
        k2 =  h * f(t + h/2, x + k1/2)
        k3 =  h * f(t + h/2, x + k2/2)
        k4 =  h * f(t + h, x + k3)
        return [t + h, x + (k1 + 2*k2 + 2*k3 + k4) / 6]


if __name__ == '__main__':

    from math import exp, sin, cos
    import sys
    sys.path.append('../../modules')
    import PostScript as ps

    ######################################
    ### L'exponentielle : Euler vs RK4 ###
    ######################################

    print("Résolution numérique du système x'(t) = x(t) et x(0) = 1 "
            "par la méthode d'Euler et par la méthode de Runge Kutta d'ordre 4")

    def f(t, x):
        return x

    a, b, h = 0, 1, 0.1
    liste_exacte = ((t, exp(t)) for t in ps.srange(a, b, h))

    print("{:^10} | {:^17} | {:^17}"
            .format('h', 'erreur euler', 'erreur rk4'))
    print('-'*52)

    #for i in range(1, 7):
    for i in range(1, 6):
        h = 10**(-i)
        euler = Euler(f, h)
        euler.CI(0, 1.0)
        e = euler.resolution(a, b)[-1]
        rk4 = RK4(f, h)
        rk4.CI(0, 1.0)
        r = rk4.resolution(a, b)[-1]
        print("{0:>10g} | {1:> .10e} | {2:> .10e} "
                .format(h, exp(e[0]) - e[1], exp(r[0]) - r[1]))


    ######################################################################
    ### Un exemple d'équation différentielle non linéaire du 1er ordre ###
    ######################################################################

    print("Résolution numérique de l'équation x'(t) = 1 + t^2 * x(t)^2  "
            "par la méthode de Runge Kutta d'ordre 4")

    def f(t, x):
        return 1 + t**2 * x**2

    a, b, h = -4, 4, 0.01
    bleu = (0, 0, 1)
    boite = [-4.5, -4.5, 4.5, 4.5] # xmin, ymin, xmax, ymax

    def horscadre(x):
        return abs(x) > 4.5

    courbes = []
    for k in ps.srange(-4, 4, 0.2):
        sol = RK4(f, h)
        sol.CI(0, k)
        courbes.append([sol.resolution(a, b, horscadre), bleu])

    ps.plot("exemple_rk4", boite, 40, courbes)

    ######################################
    ### Un exemple de système autonome ###
    ######################################

    print("Résolution numérique de l'oscillateur de van der Pol")

    def f(t, x):
        return [x[1], 0.5 * x[1] - x[0] - x[1]**3]

    boite = [-3.6, -3.6, 3.6, 3.6] # xmin, ymin, xmax, ymax

    def horscadre(x):
        return abs(max(x)) > 4

    a, b, h = 0, 30, 0.01
    sol = RK4(f, h)
    sol.CI(0, [0.01, 0.01])
    solution = (x[1] for x in sol.resolution(a, b, horscadre))
    courbes = [[solution, (1, 0, 0)]]

    b = 15
    for k in ps.srange(0, 20, 0.4):
        sol = RK4(f, h)
        sol.CI(0, [0.3*k-3, 3])
        solution = (x[1] for x in sol.resolution(a, b, horscadre))
        courbes.append([solution, (k/20, 0.32, 0.48-k/44)])
        sol = RK4(f, h)
        sol.CI(0, [3-0.3*k, -3])
        solution = (x[1] for x in sol.resolution(a, b, horscadre))
        courbes.append([solution, (k/20, 0.32, 0.48-k/44)])

    ps.plot("syst_autonome", boite, 40, courbes, etiquette=False)

    ###################################################################
    ### Un exemple d'équation différentielle linéaire du 2eme ordre ###
    ###################################################################

    print("Résolution numérique de l'équation t^2 x'' + t x' + (t^2 - a^2) x = 0")

    def f(t, x):
        alpha = 0.5
        try:
            return [x[1], (alpha**2 - t**2) / t**2 * x[0] - x[1] / t]
        except ZeroDivisionError:
            return [x[1], 0]

    boite = [-1.5, -9.2, 19, 9.2] # xmin, ymin, xmax, ymax
    a, b, h = 0.01, 18.9, 0.02
    courbes = []

    for k in ps.srange(0, 20, 0.6):
        sol = RK4(f, h)
        sol.CI(a, [0.2*k-2, 0])
        solution = ([x[0], x[1][0]] for x in sol.resolution(a, b))
        courbes.append([solution, (k/20, 0.32, 0.48-k/44)])

    ps.plot("bessel", boite, 17, courbes, ratioY=0.5, gradH=0.2)



