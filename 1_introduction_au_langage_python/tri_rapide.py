#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

# Génération aléatoire d'une liste
from random import randrange
n = 20; liste = [randrange(100) for i in range(n)]

# Tri rapide
# On choisit un élément au hasard que l'on appelle "pivot"
# On le met à sa place définitive en plaçant
# tous les éléments qui sont plus petits à sa gauche
# et tous les éléments qui sont plus grands à sa droite
# On recommence ensuite le tri sur les deux sous-listes obtenues
# jusqu'à ce que la liste soit triée
# Par exemple pour [10, 1, 5, 19, 3, 3, 2, 17] choisissons 10 comme premier pivot
# On place les éléments plus petits que 10 à gauche et les plus grands à droite
# [1, 5, 3, 3, 2,  10,  19, 17]
# Il reste deux sous-listes à trier selon la même méthode
# [1, 5, 3, 3, 2] et [19, 17]

def tri_rapide(liste):
    # Effectue un tri de liste en utilisant l'algorithme de tri rapide
    if liste == []: return []
    return (tri_rapide([x for x in liste[1:] if x < liste[0]))
            + [liste[0]] + tri_rapide([x for x in liste[1:] if x >= liste[0]))
