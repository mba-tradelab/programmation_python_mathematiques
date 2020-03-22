#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

def trouve(mot, lettre):
    # renvoie l'indice de la première occurrence de lettre dans la chaîne de caractères mot
    # renvoie -1 si lettre n'apparaît pas dans mot
    indice = 0
    while indice < len(mot):
        if mot[indice] == lettre:
            return indice
        indice += 1
    return -1
