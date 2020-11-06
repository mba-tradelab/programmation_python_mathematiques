#!/usr/bin/python3
#-*- coding: Utf-8 -*-

########################################################################
# (C) Alexandre Casamayou-Boucau, Pascal Chauvin, Guillaume Connan     #
#                                                                      #
# Complément de l'ouvrage :                                            #
# Programmation en Python pour les mathématiques                       #
# Editeur : Dunod                   -        Collection : Sciences Sup #
# ISBN-13: 978-2100738311           -                  Licence : GPLv2 #
########################################################################


def diffDiv(liste):
    taille = len(liste)
    tableau = [[x[1]] for x in liste]
    for t in range(1, taille):
        for i in range(t, taille):
            diff = ((tableau[i][t-1] - tableau[i-1][t-1])
                    / (liste[i][0] - liste[i-t][0]))
            tableau[i].append(diff)
    return [ligne[-1] for ligne in tableau]

def interpol(x, liste):
    tableau = diffDiv(liste)
    valeur = tableau[-1]
    for k in range(len(liste)-2, -1, -1):
        valeur *= x - liste[k][0]
        valeur += tableau[k]
    return valeur


if __name__ == '__main__':

    from math import cos, acos, pi
    import sys
    sys.path.append('../../modules')
    from PostScript import plot, nrange

    ##########################
    ### Phénomène de Runge ###
    ##########################

    def f(x):
        return 1/(1+10*x**2)

    numpoints, a, b = 1000, -1.2 , 1.2
    nomFichier = "runge"
    zoom = 100
    rouge, vert, bleu = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    boite = [-1.5, -0.7, 1.7, 2.1] # xmin, ymin, xmax, ymax

    liste_f = [[x, f(x)] for x in nrange(a, b, numpoints)]

    subdiv = nrange(-1, 1, 11)
    l = [[x, f(x)] for x in subdiv]
    liste_p1 = [[x, interpol(x, l)] for x in nrange(a, b, numpoints)]

    subdiv = nrange(-1, 1, 19)
    l = [[x, f(x)] for x in subdiv]
    liste_p2 = [[x, interpol(x, l)] for x in nrange(a, b, numpoints)]

    plot(nomFichier, boite, zoom, [[liste_f, bleu], [liste_p1, vert],
        [liste_p2, rouge]], ['1/(1+10x^2)', [1.1, 0.1], bleu],
        ['p_11(x)', [1.1, -0.3], vert], ['p_19(x)', [1.1, 1], rouge])

    ############################################
    ### Tracé du polynôme de Tchebychev T_20 ###
    ############################################

    numpoints, a, b, zoom = 1000, - 1 , 1, 140
    nomFichier = "tchebychev"
    boite = [-1.1, -1.1, 1.1, 1.4] # xmin, ymin, xmax, ymax

    # Liste de points de la courbe
    liste = [[x, cos(20*acos(x))] for x in nrange(a, b, numpoints)]

    plot(nomFichier, boite, zoom, [[liste]],
            ['T_20', [0.8, 1.15], (0, 0, 1)], ratioY=.4, gradH=.02)

    #########################################################
    ### Utilisation des zéros des polynômes de Tchebychev ###
    #########################################################

    def tcheby(n):
        return [cos(pi * (2*i+1) / (2*n)) for i in range(n)]

    subdiv = tcheby(11)
    l = [[x, f(x)] for x in subdiv]
    liste_p1 = [[x, interpol(x, l)] for x in nrange(a, b, numpoints)]

    subdiv = tcheby(19)
    l = [[x, f(x)] for x in subdiv]
    liste_p2 = [[x, interpol(x, l)] for x in nrange(a, b, numpoints)]

    boite = [-1.5, -0.3, 1.7, 1.2] # xmin, ymin, xmax, ymax
    plot("tcheby", boite, zoom, [[liste_f, bleu], [liste_p1, vert],
        [liste_p2, rouge]], ['1/(1+10x^2)', [1.1, 0.1], bleu],
        ['p_11(x)', [1.1, -0.1], vert], ['p_19(x)', [1.1, 0.3], rouge])


