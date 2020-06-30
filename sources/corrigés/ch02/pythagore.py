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

from math import *
import sys
sys.path.append('../../modules')
from PostScript import *

def rectangle(base, k):
    [A, B] = base
    norme = hypot(B[0] - A[0], B[1] - A[1])
    orthog = [A[1]-B[1], B[0]-A[0]]
    D = [a + k*u for (a, u) in zip(A, orthog)]
    C = [b + k*u for (b, u) in zip(B, orthog)]
    return [A, B, C, D]

def triangle(base, theta):
    [A, B] = base
    C = [b - a for (a, b) in zip(A, B)]
    R = [(1+cos(2*theta))/2, sin(2*theta)/2]
    C = [R[0]*C[0] - R[1]*C[1],
            R[1]*C[0] + R[0]*C[1]]
    C = [a + c for (a, c) in zip(A, C)]
    return [A, B, C]

def pythagore(base, k, theta, niveau, N=None):
    if N == None: N = niveau
    q = niveau/N
    #couleur = (0, 1-niveau/N, 0) # tronc noir, feuilles vertes
    #couleur = (q, 4*q*(1-q), (1-q)) # arbre multicolore
    couleur = (1-niveau/N, )*3 # tronc noir, feuilles grises
    rc = rectangle(base, k)
    graphique.ajouteCourbe(rc, couleur, fill=True)
    tr = triangle(rc[:-3:-1], theta)
    if niveau > 1:
        pythagore([tr[0], tr[2]], k, theta, niveau - 1, N)
        pythagore([tr[2], tr[1]], k, theta, niveau - 1, N)


if __name__ == "__main__":
    N = 14
    #N = 2 ou 3
    base = [[0, 0], [2, 0]]
    nomFichier = "pythagore"
    boite = [-8, -1, 6, 9]
    #boite = [-2.0, -0.5, 3.5, 5.5]
    zoom, marge, ratioY, trait = 30, 1.02, 1, 0.1
    graphique = Plot(nomFichier, boite, zoom, marge, ratioY)
    graphique.preambule()
    graphique.cadre()
    pythagore(base, 0.9, pi/6, N)
    graphique.fin()
    graphique.exportePDF()
    graphique.affichePS()




