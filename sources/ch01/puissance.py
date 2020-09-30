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


def puissance(x,n):
  if n == 0: return 1
  else:
    print('--'*n + '> appel de puissance({},{})'.format(x, n-1))
    y = x * puissance(x, n - 1)
    print('--'*n + '> sortie de puissance({},{})'.format(x, n-1))
    return y

puissance(2,5)
