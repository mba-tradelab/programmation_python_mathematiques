#!/usr/bin/python3
#-*- coding: utf-8 -*-

########################################################################
# (C) Alexandre Casamayou-Boucau, Pascal Chauvin, Guillaume Connan     #
#                                                                      #
# Complément de l'ouvrage :                                            #
# Programmation en Python pour les mathématiques                       #
# Editeur : Dunod                   -        Collection : Sciences Sup #
# ISBN-13: 978-2100738311           -                  Licence : GPLv2 #
########################################################################

from numpy.random import randint
from collections  import Counter
from itertools import product


def piece(n):
    T = []
    for k in range(n):
        X = 0
        for j in range(3):
            X += randint(0,2)
        T.append(X)
    return([ (T.count(i) / float(n)) for i in range(0,4) ])


def boules(n):
    T = []
    for k in range(n):
        X = 0
        X += randint(1,12) <= 7
        X += randint(1,8)  <= 5
        X += randint(1,10)  <= 6
        T.append(X)
    return([ ( T.count(j) / float(n) ) for j in range(0,4) ])


def boule(n,nb):
    X=0
    for k in range(n):
        B = 0
        for j in range(1,6):
            B += randint(1,11) <= 7
        X += B == nb
    return X / n


def toscane(n):
    T = n*[0]
    for k in range(n):
        T[k] = randint(1,7) + randint(1,7) + randint(1,7)
    return 'Obtenir 9 :' + str(T.count(9)*100.0/n) + '%, Obtenir 10 :' + str(T.count(10)*100.0/n) + '%'


nObs = 144000

# séries d'observations de séries de lancers de 3 dés
sObs  = lambda n : [sum( randint(1,7,size = n) )  for k in range(nObs)]
sTheo = lambda n : [sum(t) for t in product(range(1,7), repeat = n)]

# dictionnaire des fréquences de ces séries
# dico.items() renvoie la liste des couples (clé,valeur) de dico
def pObs(n) :
    s = sObs(n)
    return {x: 100*v/len(s)  for x,v in Counter(s).items()}

def pTheo(n):
    s = sTheo(n)
    return {x: 100*v/len(s) for x,v in Counter(s).items()}


def piece_max(n):
    S = n*[1]
    for k in range(n):
        s = []
        P = [randint(0,2) for z in range(10)]
        p = 0
        while p < 9:
            j = p + 1
            while (P[j] == P[p] and j < 9):
                j += 1
            s . append(j - p)
            p = j
        s.sort(reverse=True)
        S[k] = s[0]
    m = sum(S) / n
    return 'Sur '+str(n)+'  séries de 10 lancers, la moyenne du nombre maximal de résultats consécutifs égaux est '+str(m)




def monty(n):
    gagne_sans_changer = 0
    gagne_en_changeant = 0
    for j in range(n):
        voiture = randint(0,3)
        choix   = randint(0,3)
        if choix == voiture:
            ouverte = (voiture + 1 + randint(0,1)) % 3
        else:
            ouverte = 0 + 1 + 2 - choix - voiture
        changement = 0 + 1 + 2 - choix - ouverte
        if choix == voiture:
            gagne_sans_changer += 1
        if changement == voiture:
            gagne_en_changeant += 1
    return 'Gagne en changeant : '+str(100.*gagne_en_changeant/n)+'%   Gagne sans changer : '+ str(100.*gagne_sans_changer/n)+'%'
