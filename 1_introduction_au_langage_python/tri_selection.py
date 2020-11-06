#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

# Génération aléatoire d'une liste
from random import randrange
n = 20; liste = [randrange(100) for i in range(n)]

# Tri par sélection
# On commence par chercher le plus grand élément du tableau
# On l'échange avec le dernier élément
# On recommence avec le deuxième élément le plus grand, etc.

def maxi(liste, n):
    # Retourne le maximum et son indice parmi les n premiers éléments de liste
    indice = 0
    for i in range(n):
        if liste[i] > liste[indice]:
            indice = i
    return [liste[indice], indice]

def tri_selec(liste):
    i = len(liste) - 1
    while i > 0:
        j = maxi(liste, i + 1)[1]
        if j != i:
            liste[j], liste[i] = liste[i], liste[j]
        i -= 1
    return liste
