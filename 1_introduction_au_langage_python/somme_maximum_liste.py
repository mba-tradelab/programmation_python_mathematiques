#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

def somme(liste):
    # fonction renvoyant la somme d'une liste d'entiers
    s = 0
    for e in liste:
        s += e
    return s

def maximum(liste):
    # fonction renvoyant le maximum d'une liste d'entiers
    max_liste = liste[0]
    for e in liste:
        if e > max_liste:
            max_liste = e
    return max_liste
