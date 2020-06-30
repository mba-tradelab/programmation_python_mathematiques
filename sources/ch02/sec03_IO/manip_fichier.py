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


# Création d'un nouveau fichier et écriture
nom = 'mon_fichier.txt'
fichier = open(nom, 'w')
for i in range(1, 4):
    fichier.write('Ceci est la ligne {}\n'.format(i))
fichier.close()

# Lecture
fichier = open(nom, 'r')
liste = fichier.read()
print(liste)
fichier.close()

# Ajout en fin de fichier
fichier = open(nom, 'a')
for i in range(4, 6):
    fichier.write('Ceci est la ligne {}\n'.format(i))
fichier.close()

# Variante pour la lecture
fichier = open(nom, 'r')
liste = fichier.readlines()
print(liste)
fichier.close()

# Variante pour la lecture
fichier = open(nom, 'r')
for ligne in fichier:
    print(ligne, end='')
fichier.close()

# Exercice nbre_lignes.py
def nbre_lignes(nom):
    fichier = open(nom, 'r')
    n = len(fichier.readlines())
    fichier.close()
    return n

print(nbre_lignes(nom))

# Exercice
def extraction(nom):
    liste = []
    fichier = open(nom, 'r')
    for ligne in fichier:
        for mot in ligne.split():
           liste.append(mot)
    fichier.close()
    return(liste)

print(extraction(nom))

from os.path import *
print(exists(nom))
print(abspath(nom))


