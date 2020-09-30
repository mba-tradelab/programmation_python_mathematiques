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

import os
import sys

def parcours(repertoire):
    arborescence = os.walk(repertoire)

    for dossier in arborescence:
        for fichier in dossier[2]:
            if fichier.endswith('.py'):
                print(os.path.join(dossier[0], fichier))
                #variante : print(os.path.abspath(fichier))


if __name__ == "__main__":
    try:
        parcours(sys.argv[1])
    except IndexError:
        parcours(os.getcwd())

