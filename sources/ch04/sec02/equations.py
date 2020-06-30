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


class NonLineaire(object):
    def __init__(self, approx, eps=1e-14, maxIter=10**7):
        self.approx = approx
        self.eps = eps
        self.maxIter = maxIter

    def resolution(self, f):
        raise NotImplementedError

class Dichotomie(NonLineaire):
    def subdivise(self, a, b, f):
        return (a+b) * 0.5

    def resolution(self, f):
        [a, b] = self.approx
        a, b = min(a, b), max(a, b)
        eps, maxIter = self.eps, self.maxIter
        for i in range(maxIter):
            c = self.subdivise(a, b, f)
            if b-a < eps:
                return c
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
        return c

class RegulaFalsi(Dichotomie):
    def subdivise(self, a, b, f):
        return a - f(a) * (b-a) / (f(b) - f(a))

class PointFixe(NonLineaire):
    def resolution(self, f):
        eps, maxIter = self.eps, self.maxIter
        x0, x1 = self.approx, f(self.approx)
        for i in range(maxIter):
            if abs(x0 - x1) < eps:
                return x1
            x0, x1 = x1, f(x1)
        return x1

class Steffensen(NonLineaire):
    def resolution(self, f):
        eps, maxIter = self.eps, self.maxIter
        x0 = self.approx
        for i in range(maxIter):
            x1 = f(x0)
            x2 = f(x1)
            xe = x0 - (x1-x0)**2 / (x2 - 2*x1 + x0)
            if abs(x0 - xe) < eps:
                    return xe
            x0 = xe
        return xe

class Newton(PointFixe):
    def resolution(self, f, fp):
        return PointFixe.resolution(self, lambda x:x - f(x)/fp(x))

class Secante(NonLineaire):
    def resolution(self, f):
        eps, maxIter = self.eps, self.maxIter
        [x0, x1] = self.approx
        for i in range(maxIter):
            x2 = x1 - f(x1) * (x1-x0) / (f(x1) - f(x0))
            if abs(x0 - x2) < eps:
                    return x2
            x0, x1 = x1, x2
        return x2

if __name__ == "__main__":

    from math import *
    print("{:>7}| {:^9}|{:^9}| {:^9} | {:^9} | {:^9} "
            .format("maxIter", "Dichotomie", "RegulaFalsi",
            "Sécante", "PointFixe", "Newton"))
    for i in range(1, 8):
        di = Dichotomie([1, 2], maxIter=i)
        rg = RegulaFalsi([1, 2], maxIter=i)
        pf = PointFixe(2, maxIter=i)
        nw = Newton(2, maxIter=i)
        se = Secante([1, 2], maxIter=i)
        comp = [eval(m).resolution(lambda x:x**2-2)
                for m in ['di', 'rg', 'se']]
        comp.append(pf.resolution(lambda x:0.5*(x+2/x)))
        comp.append(nw.resolution(lambda x:x**2-2, lambda x:2*x))
        comp = [sqrt(2) - c for c in comp]
        print("{:>6d} | {: .2e} | {: .2e} | {: .2e} | {: .2e} | {: .2e}"
                .format(i, comp[0], comp[1], comp[2], comp[3], comp[4]))

