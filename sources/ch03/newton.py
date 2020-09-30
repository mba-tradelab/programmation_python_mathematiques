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

import numpy as np
import math

def reduit_liste(L) :
    """ Calcule la liste des différences 2 à 2 d'une liste de nbs """
    return [a - b for (a,b) in zip(L[1:], L)]

def reduit(L) :
    """ Renvoie la liste des listes de différences : le triangle de Newton applati """
    if L == [] :
        return L
    return [L] + reduit(reduit_liste(L))

def diff_newton(L) :
    """ Renvoie les y1, Dy1, D2y1, etc. """
    return [liste[0] for liste in reduit(L)]

def base_newton(alpha, x, n) :
    """ Renvoie la liste des évaluations des (x-a)(x-a-1).../n! accumulées dans une liste """
    terme = 1
    base  = [terme]
    for k in range(1,n) :
        terme *= ((x - alpha - (k - 1)) / k )
        base.append(terme)
    return base

def interpol_newton(liste, alpha, x) :
    """ renvoie l'évaluation du poly de Newton en x en partant de a avec une liste de valeurs donnée """
    return sum([ a * b for (a,b) in zip(diff_newton(liste), base_newton(alpha, x, len(liste))) ])

def liste_log_entiers(a,b) :
    """ renvoie la liste des logarithmes décimaux des entiers de a à b inclus """
    return [math.log10(k) for k in range(a, b + 1)]


