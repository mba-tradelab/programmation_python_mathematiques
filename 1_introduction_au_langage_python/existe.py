#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

def existe(x, liste):
    # fonction booléenne qui cherche si un élément existe dans une liste
    for y in liste:
        if x == y: return True
    return False
