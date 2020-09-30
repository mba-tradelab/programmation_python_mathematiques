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


class Diff(object):
    def __init__(self, f, h=1e-8):
        self.f = f
        self.h = h

class DiffAvant1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h

class DiffCentre2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)

if __name__ == '__main__':

    import math as m

    #####################
    ### Premier test  ###
    #####################
    print('{:^7} | {:^20}'.format('h', 'cos'))
    print('-'*28)
    for n in range(1, 16):
        x, h = 0, 10**(-n)
        cos = DiffAvant1(m.sin, h)
        print('{:7.1e} | {:.15f}'.format(h, cos(x)))

    #####################
    ### Deuxième test ###
    #####################
    def f(x):
        return m.sqrt(1+x)

    for n in range(1, 16):
        x, h = 0, 10**(-n)
        g1 = DiffAvant1(f, h)
        g2 = DiffCentre2(f, h)
        print('{0:7.1e} | {1:.15f} | {2:.15f}'.format(h, g1(x), g2(x)))

