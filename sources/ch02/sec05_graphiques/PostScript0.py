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


"""
   Module de tracé d'une liste de points dans un fichier PostScript
"""
import os

def nrange(a, b, numpoints):
    """Renvoie une subdivision de [a, b] à N+1 points."""
    pas = (b - a) / numpoints
    return (a + i * pas for i in range(numpoints + 1))

def srange(a, b, pas):
    """Renvoie une subdivision de [a, b] avec un pas donné."""
    numpoints = int((b - a) / pas)
    return (a + i * pas for i in range(numpoints + 1))

def preambule(nomFichier, boite, zoom, delta):
    """ Écrit le préambule du fichier EPS."""
    cadre = [x * zoom * delta for x in boite]
    s_debut = ("%!PS-Adobe-2.0 EPSF-2.0\n"
    "%%BoundingBox: {0[0]:.1f} {0[1]:.1f} {0[2]:.1f} {0[3]:.1f}\n"
    "{1} {1} scale\n").format(cadre, zoom)
    with open(nomFichier + ".eps", 'w') as f:
        f.write(s_debut)

def fin(nomFichier):
    """ Cloture le fichier EPS."""
    s_fin = "\nshowpage\n"
    with open(nomFichier + ".eps", 'a') as f:
        f.write(s_fin)

def ajouteCourbe(nomFichier, liste, boite, zoom, epaisseurTrait, rgb):
    """Ajoute une courbe donnée sous forme de liste."""
    with open(nomFichier + ".eps", 'a') as f:
        f.write("\nnewpath\n")
        for i, point in enumerate(liste):
            if i == 0:
                f.write("    {0[0]: .4f}  {0[1]: .4f}   ".format(point))
                f.write("moveto\n")
            elif (boite[0] <= point[0] <= boite[2]
                    and boite[1] <= point[1] <= boite[3]):
                f.write("    {0[0]: .4f}  {0[1]: .4f}   ".format(point))
                f.write("lineto\n")
        f.write("{1} {0} div setlinewidth\n"
                "{2[0]} {2[1]} {2[2]} setrgbcolor\n"
                "stroke\n".format(zoom, epaisseurTrait, rgb))

def affiche(nomFichier):
    """Affiche le graphique via ghostview."""
    os.system("gv {0}.eps &".format(nomFichier))

if __name__ == "__main__":
    from math import pi, cos, sin, floor

    N, a, b = 1000, 0, 1 + floor(38 * pi)
    nomFichier, zoom, epaisseurTrait = "polar", 100, 0.4
    rgb = (0, 0, 1) # tracé en bleu
    # rgb = (0.2, 0.2, 0.2) # tracé en gris
    boite = [-1.5, -1.5, 1.5, 1.5] # xmin , ymin, xmax, ymax

    # Fonction définissant la courbe polaire
    def f(theta):
        return 1 + cos(theta*20/19) / 3

    # Liste de points de la courbe
    liste = ([f(theta) * cos(theta), f(theta) * sin(theta)]
            for theta in nrange(a, b, N))

    # Création du fichier EPS
    preambule(nomFichier, boite, zoom, 1.1)
    ajouteCourbe(nomFichier, liste, boite, zoom, epaisseurTrait, rgb)
    fin(nomFichier)
    affiche(nomFichier)

