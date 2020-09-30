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


def dotprod(u, v):
    if len(u) != len(v):
        raise IndexError("Les vecteurs n'ont pas la même taille !")
    return sum(x*y for x, y in zip(u, v))


print(dotprod([3, 9], [5, -1]))
print(dotprod([3, 9, 0], [5, -1]))
