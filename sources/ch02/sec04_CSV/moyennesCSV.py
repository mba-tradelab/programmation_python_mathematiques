#!/usr/bin/python3
#-*- coding: Utf-8 -*-

########################################################################
# Fichier moyennesCSV.py                                               #
# (C) Alexandre Casamayou-Boucau, Pascal Chauvin, Guillaume Connan     #
#                                                                      #
# Complément de l'ouvrage :                                            #
# Programmation en Python pour les mathématiques                       #
# Editeur : Dunod                   -        Collection : Sciences Sup #
# ISBN-10: 2100574221               -          ISBN-13: 978-2100574223 #
#                                   -                                  #
# Version du 18/01/2012             -                  Licence : GPLv2 #
########################################################################


import csv
with open('test.csv', newline='') as f:
    lignes = [ligne for ligne in csv.reader(f)]

def moy(liste):
    liste = [eval(x) for x in liste]
    return str(round(sum(liste)/len(liste), 1))

lignes[0].append('moyennes')
for ligne in lignes[1:]:
    ligne.append(moy(ligne[1:]))

classe = [moy([lig[i] for lig in lignes[1:]])
        for i in range(1, 5)]
classe[0:0] = ['moyennes']
lignes.append(classe)

with open('test3.csv', 'w', newline='') as f:
    ecrire = csv.writer(f)
    for ligne in lignes:
        ecrire.writerow(ligne)

