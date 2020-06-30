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


table = [['Noms', 'maths', 'physique', 'chimie'],
['Achille', '12', '14', '15'],
['Ajax', '17', '11', '9'],
['Alceste', '15', '15', '16'],
['Alcibiade', '11', '13', '12'],
['Aspasie', '19', '15', '18']]

import csv
with open('test2.csv', 'w', newline='') as f:
    ecrire = csv.writer(f)
    for ligne in table:
        ecrire.writerow(ligne)

with open('test2.csv', 'a', newline='') as f:
    ecrire = csv.writer(f)
    ecrire.writerow(['Berenice', '14', '17', '17'])

