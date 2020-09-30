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


def horner_rec(p, x):
    """Programmation récursive de la méthode de Hörner."""
    if len(p) == 1:
        return p[0]
    p[-2] += x * p[-1]
    return horner_rec(p[:-1], x)

def horner(p, x):
    """Programmation itérative de la méthode de Hörner."""
    somme = 0
    for c in reversed(p):
        somme = c + x*somme
    return somme

# Évaluation de P = 1 + 5X + 4X^2 - 8X^3 + 2X^4 en X = 3.14 :
print(horner([1, 5, 4, -8, 2], 3.14))

