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


from decimal import *

def prod(x, y):
	return x*y

def diff(x, y):
	return ((x+y)/2)**2 - ((x-y)/2)**2

def euclide(a, b):
    c, d = Decimal(str(a)), Decimal(str(b))
    print('-'*53)
    print('{:<25s} | {:<25s}'.format('type float', 'type Decimal'))
    print('-'*53)
    for n in range(6):
        u, v = prod(a, b), diff(a, b)
        w, x = prod(c, d), diff(c, d)
        print('{:>25g} | {:>25g}'.format(u - v, w - x))
        a, b = u, a + 1
        c, d = w, c + 1
    print('-'*53)

a = 6553.99
b = a + 1

print('{:*^53}'.format(' getcontext().prec = 28 '))
euclide(a, b)
print()
getcontext().prec = 128
print('{:*^53}'.format(' getcontext().prec = 128 '))
euclide(a, b)
