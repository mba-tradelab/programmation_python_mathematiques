#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

# Algorithme des différences successives
# a, b ∈ ℕ et b ≠ 0
# a < b ?
# si NON : a <- b - a
# si OUI : le reste vaut r = a 

def reste(a, b):
    # renvoie le reste de la division euclidienne de a par b
    if b == 0:
        return 'b doit être non nul.'
    while a >= b:
        a = a - b
    return a
        
# Algorithme d'Euclide
# a, b ∈ ℕ* et a >= b
# calcul du reste r de la division euclidienne de a par b
# r = 0 ?
# si NON : a <- b et b <- r ; le PGCD est inchangé
# si OUI : le PGCD vaut b

def pgcd(a, b):
    while b > 0:
        a, b = b, reste(a, b)
    return a
