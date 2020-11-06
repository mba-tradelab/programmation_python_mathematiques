#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
# (C) Alexandre Casamayou-Boucau, Pascal Chauvin, Guillaume Connan     #
#                                                                      #
# Complément de l'ouvrage :                                            #
# Programmation en Python pour les mathématiques                       #
# Editeur : Dunod                   -        Collection : Sciences Sup #
# ISBN-13: 978-2100738311           -                  Licence : GPLv2 #
########################################################################

import sys
sys.path.append('../../modules')
from PostScript import *

def milieu(a, b):
    return [(a[0]+b[0])*0.5, (a[1]+b[1])*0.5]

def sierpinski(points, niveau):
    if niveau > 1:
        for i in range(3):
            j, k = (i+1) % 3, (i+2) % 3
            sierpinski([points[i], milieu(points[i], points[j]),\
                milieu(points[i], points[k])], niveau-1)
    else:
        graphique.ajouteCourbe(points, (0, 0, 0), 0.4, True)

for i in [3, 4, 5, 10]:
    nomFichier = "sierpinskiPS_{:d}".format(i)
    boite = [-1.1, -0.1, 1.1, 1.8]
    zoom, marge, ratioY, trait = 140, 1.02, 1, 0.4

    graphique = Plot(nomFichier, boite, zoom, marge, ratioY)
    graphique.preambule()
    graphique.cadre()
    points = [[-1, 0], [1, 0], [0, 1.7320508075]]
    sierpinski(points, i)
    graphique.fin()
    graphique.exportePDF()
    graphique.affichePS()

