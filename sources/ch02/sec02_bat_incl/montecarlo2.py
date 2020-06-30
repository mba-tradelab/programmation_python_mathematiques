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


import random
from math import sqrt, hypot, pi

def f(x, y, a, b):
    c = sqrt(a**2-b**2)
    return hypot(x-c, y) + hypot(x+c, y)

def montecarlo2(a, b, n):
    xrandom = [random.uniform(-a, a) for i in range(n)]
    yrandom = [random.uniform(-b, b) for i in range(n)]
    somme = sum(f(x, y, a, b) for x in xrandom
            for y in yrandom if hypot(x/a, y/b) <= 1)
    return somme * (4 * a * b) / n**2

print('-'*63)
print('{0:>7s} | {1:^15s} | {2:^15s} | {3:^15s} |'.format('n',
        'approximation', 'erreur absolue', 'erreur relative'))
print('-'*63)
for i in range(1, 5):
    a, b, n = 2, 1, 10**i
    approx = montecarlo2(a, b, n)
    exacte = 2*pi*b*(3*a**2-b**2)/3
    erreur = exacte - approx
    print('{0:7d} | {1: 15.10f} | {2:^ 15.3e} | {3:^ 15.3e} |'
            .format(n, approx, erreur, abs(erreur / exacte)))
print('-'*63)

def montecarlo3(a, b, n):
    somme = 0
    for i in range(n):
        x = random.uniform(-a, a)
        for j in range(n):
            y = random.uniform(-b, b)
            if hypot(x/a, y/b) <= 1:
                somme += f(x, y, a, b)
    return somme * (4 * a * b) / n**2


from time import *
debut = clock()
print(montecarlo2(2, 1, 2000))
fin = clock()
print(fin - debut, 'sec')
debut = clock()
print(montecarlo3(2, 1, 2000))
fin = clock()
print(fin - debut, 'sec')

