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


def expo(a, n):
    if n == 0:
        return 1
    else:
        if n%2 == 0:
            return expo(a, n//2)**2
        else:
            return a*(expo(a, (n-1)//2)**2)

# Les tests
import os, sys, time
sys.setrecursionlimit(100000)

a = 92982829
n = 50000

import time

t0 = time.clock()
x = 1
for i in range(n):
    x = a * x
t1 = time.clock()
print('{:>25} ---> {} s'.format('méthode naïve', t1 - t0))

t0 = time.clock()
y = expo(a, n)
t1 = time.clock()
print('{:>25} ---> {} s'.format('fonction expo(a, n)', t1 - t0))

t0 = time.clock()
z = a ** n
t1 = time.clock()
print('{:>25} ---> {} s'.format('exponentiation Python', t1 - t0))

print(x == y and x == z)

