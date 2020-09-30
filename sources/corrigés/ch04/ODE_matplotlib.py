#!/usr/bin/python3
#-*- coding: Utf-8 -*-

import numpy
import matplotlib.pyplot as plt

class ODE(object):
    def __init__(self, f, h):
        self.f = lambda u, t: numpy.asarray(f(u, t), float)
        self.h = h

    def iteration(self):
        raise NotImplementedError

    def CI(self, t0, x0):
        self.liste = [[t0, numpy.asarray(x0, float)]]
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

    ######################################################################
    ### Un exemple d'équation différentielle non linéaire du 1er ordre ###
    ######################################################################

    print("Résolution numérique de l'équation x'(t) = 1 + t^2 * x(t)^2  "
            "par la méthode de Runge Kutta d'ordre 4")

    def f(t, x):
        return 1 + t**2 * x**2

    a, b, h = -4, 4, 0.01

    def horscadre(x):
        return abs(x) > 4.5

    plt.figure()
    plt.ylim(-4, 4)
    plt.xlabel('t')
    plt.ylabel('x')

    for k in numpy.arange(-4, 4, 0.2):

        sol = RK4(f, h)
        sol.CI(0, k)
        x = numpy.array(sol.resolution(a, b, horscadre))
        plt.plot(x[:,0], x[:,1], color=(0, 0, 1))

    plt.show()

    ######################################
    ### Un exemple de système autonome ###
    ######################################

    print("Résolution numérique de l'oscillateur de van der Pol")

    def f(t, x):
        return [x[1], 0.5 * x[1] - x[0] - x[1]**3]

    def horscadre(x):
        return abs(max(x)) > 5

    a, b, h = 0, 30, 0.03

    plt.figure()
    plt.ylim(-4, 4)
    plt.xlabel('x')
    plt.ylabel('y')

    sol = RK4(f, h)
    sol.CI(0, [0.01, 0.01])
    x = numpy.array([x[1] for x in sol.resolution(a, b, horscadre)])
    plt.plot(x[:,0], x[:,1], color=(0, 0, 1))

    b = 15
    for k in numpy.arange(0, 20, 0.5):

        sol = RK4(f, h)
        sol.CI(0, [0.3*k-3, 3])
        x = numpy.array([x[1] for x in sol.resolution(a, b, horscadre)])
        plt.plot(x[:,0], x[:,1], color=(k/20, 0.32, 0.48-k/44))

        sol = RK4(f, h)
        sol.CI(0, [3-0.3*k, -3])
        x = numpy.array([x[1] for x in sol.resolution(a, b, horscadre)])
        plt.plot(x[:,0], x[:,1], color=(k/20, 0.32, 0.48-k/44))

    plt.show()


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

    a, b, h = 0.01, 18.9, 0.02

    plt.figure()
    plt.xlim(0, 19)
    plt.xlabel('x')
    plt.ylabel('y')

    for k in numpy.arange(0, 20, 0.6):

        sol = RK4(f, h)
        sol.CI(a, [0.2*k-2, 0])
        x = numpy.array([[x[0], x[1][0]] for x in sol.resolution(a, b)])
        plt.plot(x[:,0], x[:,1], color=(k/20, 0.32, 0.48-k/44))

    plt.show()



