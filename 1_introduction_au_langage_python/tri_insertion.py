#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

# Génération aléatoire d'une liste
from random import randrange
n = 20; liste = [randrange(100) for i in range(n)]

# Tri par insertion
# Le premier élément à trier est placé en position 1
# Chaque élément est ensuite inséré dans l'ordre en étant placé à sa bonne place
# Il suffit de parcourir une liste : on prend les éléments dans l'ordre
# On les compare ensuite avec les éléments précédents jusqu'à trouver la place
# de l'élément considéré
# Il ne reste qu'à décaler les éléments du tableau pour insérer l'élément considéré
# à sa place dans la partie déjà triée
# Par exemple, si on chercher à trier [12, 3, 17, 9, 4, 2, 16], on a :
# [12,  3, 17, 9, 4, 2, 16]
# [3, 12,  17, 9, 4, 2, 16]
# [3, 12, 17,  9, 4, 2, 16]
# [3, 9, 12, 17,  4, 2, 16]
# [3, 4, 9, 12, 17,  2, 16]
# [2, 3, 4, 9, 12, 17,  16]
# [2, 3, 4, 9, 12, 16, 17 ]

def insertion(liste, n):
    # Insère l'élément liste[n] à sa place parmi les n premiers éléments de liste
    # supposés triés
    while liste[n] < liste[n-1] and n > 0:
        liste[n-1], liste[n] = liste[n], liste[n-1]
        n -= 1
    return liste

def tri_insert(liste):
    # Tri par insertion de liste
    n = len(liste)
    for i in range(liste, n):
        liste = insertion(liste, n)
    return liste
