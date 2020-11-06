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

def composition(f, g):
    """Renvoie la composée de deux fonctions f et g.

    >>> from math import sin, cos
    >>> f = composition(cos, sin)
    >>> g = composition(sin, cos)
    >>> [f(x) - g(x) for x in range(0, 3)]
    [0.1585290151921035, 0.15197148686933137, 1.018539435968748]
    """
    return lambda x: f(g(x))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
