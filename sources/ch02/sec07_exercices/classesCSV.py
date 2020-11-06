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


import csv
import sys
sys.path.append('../../modules')
from PostScript import *

try:
    # Nom du fichier à ouvrir (sans l'extension)
    fichier = sys.argv[1]
    # Numéro de la colonne, des lignes mini/maxi à extraire
    colonne, ligne1, ligne2 = (eval(x) for x in sys.argv[2:5])
except IndexError:
    fichier = 'notes'
    colonne, ligne1, ligne2 = 2, 2, 39

# Lecture des notes dans le fichier CSV
with open(fichier + '.csv', newline='') as f:
    notes = [ligne[colonne - 1] for ligne in csv.reader(f)]

notes = [round(eval(x), 2) for x in notes[ligne1 - 1:ligne2] if x !='']

# Calcul des classes
classes = [sum([1 for x in notes if i < x <= i+1]) for i in range(20)]

# Paramètres du tracé
boite, zoom, marge, ratioY, trait = [-1.5, -1.5, 21.5, 10.5], 15, 1.1, 1, 0.6
grisFoncé, gris, noir = (0.2, 0.2, 0.2), (0.8, 0.8, 0.8), (0, 0, 0)

rectangles = []
for i in range(20):
    f = classes[i]
    # remplissage des rectangles
    rectangles.append([[[i, 0], [i+1, 0],
        [i+1, f], [i, f]], gris, trait, 'fill'])
    # tracé des rectangles
    rectangles.append([[[i, 0], [i+1, 0],
        [i+1, f], [i, f], [i, 0]], grisFoncé, trait])

plot(fichier, boite, zoom, rectangles,
        ["10", [10, -1], noir], ["20", [20, -1], noir], gradH=0.1)

