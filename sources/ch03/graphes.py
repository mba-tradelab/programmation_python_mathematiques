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

from numpy.random import shuffle, random
from copy import deepcopy

def compose(R,S):
    """ R suivi de S """
    C = {} # Le dictionnaire de la composée est vide au départ
    for u in R: # pour chaque sommet u de E
        C[u] = set([]) # u n'est encore en relation avec personne par C
        for v in R[u]: # pour chaque v tel que uRv
            C[u] |= S[v] # uCw <-> vSw
    return C

def ens(R):
    return set(list(R))

def id(E):
    D = {}
    for u in E: # chaque sommet u vérifie uRu
        D[u] = set([u])
    return D

def iter_compo(R,n):
    """ R^n version récursive """
    if n == 0:
        return id(ens(R)) # R^0 = id
    else: # sinon R^n = R.R^(n-1)
        return compose(R,iter_compo(R,n-1))


def est_reflexive(R):
    for u in R:
        if not(u in R[u]): # dès qu'on trouve un contre-exemple, on sort
            return False
    return True # si on n'est pas déjà sorti c'est que la relation est réflexive

def est_symetrique(R):
    for u in R:
        if u not in [R[v] for v in R[u]]:
            return False
    return True


def est_antisymetrique(R):
    for u in R:
        if u in [R[v] for v in R[u] if v != u]:
            return False
    return True


def est_transitive(R):
    R2 = compose(R,R)
    for u in R2:
        if not(R2[u] <= R[u]):
            return False
    return True

def r_plus(R):
    Rp = deepcopy(R)
    for k in range(1,len(Rp)+1):
        Rk = iter_compo(R,k)
        for u in Rp:
            Rp[u] |= Rk[u]
    return Rp

def bellman_ford(graphe, source):
    """ Programme direct sans les chemins """
    pi = {}
    for s in graphe:
        pi[s] = float('inf')
    pi[source] = 0
    pi0 = {}
    k = 1
    while pi != pi0 :
        pi0 = deepcopy(pi)
        for u in graphe:
            for v in graphe[u]:
                if pi[v] > pi[u] + graphe[u][v]:
                    pi[v]  = pi[u] + graphe[u][v]
        k+=1
    return pi

def affiche_peres(pere,depart,extremite,trajet):
    """
    À partir du dictionnaire des pères de chaque sommet on renvoie
    la liste des sommets du plus court chemin trouvé. Calcul récursif.
    On part de la fin et on remonte vers le départ du chemin.

    """
    if extremite == depart:
        return [depart] + trajet
    else:
        return (affiche_peres(pere, depart, pere[extremite], [extremite] + trajet))

def plus_court(graphe,etape,fin,visites,dist,pere,depart):
    """
    Trouve récursivement la plus courte chaine entre debut et fin avec l'algo de Dijkstra
    visites est une liste et dist et pere des dictionnaires
    graphe  : le graphe étudié                                                               (dictionnaire)
    étape   : le sommet en cours d'étude                                                     (sommet)
    fin     : but du trajet                                                                  (sommet)
    visites : liste des sommets déjà visités                                                 (liste de sommets)
    dist    : dictionnaire meilleure distance actuelle entre départ et les sommets du graphe (dict sommet : int)
    pere    : dictionnaire des pères actuels des sommets correspondant aux meilleurs chemins (dict sommet : sommet)
    depart  : sommet global de départ                                                        (sommet)
    Retourne le couple (longueur mini (int), trajet correspondant (liste sommets))

    """
    # si on arrive à la fin, on affiche la distance et les peres
    if etape == fin:
       return dist[fin], affiche_peres(pere,depart,fin,[])
    # si c'est la première visite, c'est que l'étape actuelle est le départ : on met dist[etape] à 0
    if  len(visites) == 0 : dist[etape]=0
    # on commence à tester les voisins non visités
    for voisin in graphe[etape]:
        if voisin not in visites:
            # la distance est soit la distance calculée précédemment soit l'infini
            dist_voisin = dist.get(voisin,float('inf'))
            # on calcule la nouvelle distance calculée en passant par l'étape
            candidat_dist = dist[etape] + graphe[etape][voisin]
            # on effectue les changements si cela donne un chemin plus court
            if candidat_dist < dist_voisin:
                dist[voisin] = candidat_dist
                pere[voisin] = etape
    # on a regardé tous les voisins : le noeud entier est visité
    visites.append(etape)
    # on cherche le sommet *non visité* le plus proche du départ
    non_visites = dict((s, dist.get(s,float('inf'))) for s in graphe if s not in visites)
    noeud_plus_proche = min(non_visites, key = non_visites.get)
    # on applique récursivement en prenant comme nouvelle étape le sommet le plus proche
    return plus_court(graphe,noeud_plus_proche,fin,visites,dist,pere,depart)


def dij_rec(graphe,debut,fin):
    return plus_court(graphe,debut,fin,[],{},[],1)


def colo(g):
    n = len(g) # nb de sommets
    couleurs_dispo = set(range(1,n+1)) # ensemble des couleurs disponibles
    g_color = {} # le dictionnaire des sommets colorés avec leurs couleurs
    for u in g: # pour chaque sommet du graphe
        couleurs_interdites  = set([g_color[v] for v in g[u] if v in g_color])
        # on interdit les couleurs des adjacents
        g_color[u] = min(couleurs_dispo - couleurs_interdites)
        # on choisit celle qui porte le plus petit numéro
    return g_color,max(g_color.values())

def colo_rand(g):
    n = len(g) # nb de sommets
    dic_col = {} # dictionnaire des meilleures colorations indexé par le nb chromatique provisoire
    liste_sommets = list(g)
    for k in range(1000):
        shuffle(liste_sommets,random = random.random) # les sommets mélangés en place
        couleurs_dispo = set(range(1,n+1)) # ens des couleurs disponibles
        g_color = {} # le dic des sommets colorés avec leurs couleurs
        for u in liste_sommets: # pour chaque sommet du graphe ordre aléatoire
            couleurs_interdites = set([g_color[v] for v in g[u] if v in g_color])
            g_color[u] = min(couleurs_dispo - couleurs_interdites)
        m = max(g_color.values())
        dic_col[m] = g_color # on associe le dictionnaire de coloration à chi_provisoire
    mi = min(dic_col.keys()) # le plus petit nb chromatique provisoire
    return 'chi(g) <= '+str(mi),dic_col[mi]  # on affiche une plus petite coloration possible
