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


"""
   Module pour afficher une liste longue sur plusieurs lignes.
"""

def lprint(liste, largeur, forme):
    n = len(liste)
    lignes = int(n / largeur)
    print('[', end='')

    for i in range(n):
        s = '{:' + forme + '}'

        if i != n-1:
            print(s.format(liste[i]), end=',')
        else:
            print(s.format(liste[i]), end=' ]')

        if i != 0 and i % largeur == largeur - 1:
            print()
            print(' ', end='')

    print()

if __name__ == "__main__":
    l = list(range(50))
    print(l)
    lprint(l, 12, '3d')

