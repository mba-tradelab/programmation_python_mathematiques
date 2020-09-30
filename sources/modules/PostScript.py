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
   Module de tracé d'une liste de points dans un fichier PostScript.
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

################################
# Définition de la classe Plot #
################################

class Plot(object):
    def __init__(self, nomFichier, boite, zoom,
        marge=1.1, epaisseurTrait=0.4, epaisseurAxes=0.2,
        ratioY=1, gradX=1, gradY=1, gradH=0.05, taillePolice=10,
        axes=True, etiquette=True, PDF=True):
        self.nomFichier = nomFichier
        self.boite, self.zoom = boite, zoom
        self.marge = marge
        self.epaisseurTrait = epaisseurTrait
        self.epaisseurAxes = epaisseurAxes
        self.ratioY, self.gradX, self.gradY = ratioY, gradX, gradY
        self.gradH, self.taillePolice = gradH, taillePolice
        self.axes, self.etiquette, self.PDF = axes, etiquette, PDF


    def ecrire(self, s, flag='a'):
        """ Écrit une chaîne de caractères dans le fichier."""
        with open(self.nomFichier + ".eps", flag) as fichier:
            fichier.write(s)


    def preambule(self):
        """ Écrit le préambule du fichier EPS."""
        boiteRedim = [self.boite[0], self.boite[1] * self.ratioY, self.boite[2],
                self.boite[3] * self.ratioY]
        cadre = [x * self.zoom * self.marge for x in boiteRedim]
        s = ("%!PS-Adobe-2.0 EPSF-2.0\n"
        "%%BoundingBox: {0[0]:.1f} {0[1]:.1f} {0[2]:.1f} {0[3]:.1f}\n"
        "{1} {1} scale\n"
        "\n").format(cadre, self.zoom)
        self.ecrire(s, flag='w')


    def cadre(self):
        """Rogne ce qui dépasse."""
        boiteRedim = [self.boite[0], self.boite[1] * self.ratioY, self.boite[2],
                self.boite[3] * self.ratioY]
        s = ("newpath\n"
        "    {0[0]:.1f} {0[1]:.1f} moveto\n"
        "    {0[2]:.1f} {0[1]:.1f} lineto\n"
        "    {0[2]:.1f} {0[3]:.1f} lineto\n"
        "    {0[0]:.1f} {0[3]:.1f} lineto\n"
        "closepath\n"
        "clip\n").format(boiteRedim, self.zoom)
        self.ecrire(s)


    def fin(self):
        """Clôture le fichier EPS."""
        self.ecrire("\nshowpage\n")


    def ajouteCourbe(self, liste, rgb=(0, 0, 0),
            trait=0.4, fill=False, style=None):
        """Ajoute une courbe donnée sous forme de liste."""
        s = "\nnewpath"

        for i, point in enumerate(liste):
            s += "\n    {0: .4f}  {1: .4f}  ".format(point[0], point[1] * self.ratioY)
            if i == 0:
                s += "moveto"
            else:
                s += "lineto"

        s += ("\n"
        "{1} {0} div setlinewidth\n"
        "{2[0]} {2[1]} {2[2]} setrgbcolor\n").format(self.zoom, trait, rgb)

        if style != None:
            s += "{} 0 setdash\n".format(style).replace(',', '')

        if fill == False:
            s += "stroke\n"
        else:
            s += "fill\n"

        self.ecrire(s)


    def ajouteTexte(self, texte, position, rgb):
        """Ajoute du texte."""
        s = ("\n"
        "/Helvetica findfont {3} scalefont setfont\n"
        "{2[0]} {2[1]} {2[2]} setrgbcolor\n"
        "newpath\n"
        "{0[0]: .4f} {0[1]: .4f} moveto\n"
        "({1}) show\n").format((position[0], position[1] * self.ratioY),
                texte, rgb, self.taillePolice)
        self.ecrire(s)


    def ajouteAxes(self):
        """Ajoute les axes du repère."""
        demiMarge = (1 + self.marge) / 2
        boiteRedim = [self.boite[0] * demiMarge, self.boite[1] * demiMarge,
                self.boite[2] * demiMarge, self.boite[3] * demiMarge]
        self.ajouteCourbe([[boiteRedim[0], 0], [boiteRedim[2], 0]])
        self.ajouteCourbe([[0, boiteRedim[1]], [0, boiteRedim[3]]])

        fleche = [[boiteRedim[2] - 1.8 * self.gradH, self.gradH / 2],
                [boiteRedim[2] - self.gradH, 0],
                [boiteRedim[2] - 1.8 * self.gradH, - self.gradH / 2],
                [boiteRedim[2], 0]]
        self.ajouteCourbe(fleche, fill=True)
        fleche = [[self.gradH / 2, boiteRedim[3] - 1.8 * self.gradH],
                [0, boiteRedim[3] - self.gradH],
                [-self.gradH / 2, boiteRedim[3] - 1.8 * self.gradH],
                [0, boiteRedim[3]]]
        self.ajouteCourbe(fleche, fill=True)

        for i in srange(0, boiteRedim[2], self.gradX):
            graduation = [[i * self.gradX, -self.gradH],
                    [i * self.gradX, self.gradH]]
            self.ajouteCourbe(graduation)

        for i in srange(0, -boiteRedim[0], self.gradX):
            graduation = [[-i * self.gradX, -self.gradH],
                    [-i * self.gradX, self.gradH]]
            self.ajouteCourbe(graduation)

        for i in srange(0, boiteRedim[3], self.gradY):
            graduation = [[-self.gradH, i * self.gradY],
                    [self.gradH, i * self.gradY]]
            self.ajouteCourbe(graduation)

        for i in srange(0, -boiteRedim[1], self.gradY):
            graduation = [[-self.gradH, -i * self.gradY],
                    [self.gradH, -i * self.gradY]]
            self.ajouteCourbe(graduation)


    def ajouteEtiquette(self):
        """Ajoute des étiquettes sur les axes."""
        s = ("\n"
        "/Helvetica findfont {3} scalefont setfont\n"
        "newpath\n"
        "{0} {1} moveto\n"
        "({2}) show\n").format(self.gradX,
                -1.4 * self.taillePolice, self.gradX, self.taillePolice)
        s += ("\n"
        "/Helvetica findfont {3} scalefont setfont\n"
        "newpath\n"
        "{0} {1} moveto\n"
        "({2:.2g}) show\n").format(-1.7 * self.taillePolice,
                1.02 * self.gradY, self.gradY / self.ratioY, self.taillePolice)
        self.ecrire(s)


    def exportePDF(self):
        """Exporte au format PDF."""
        os.system("epstopdf {0}.eps".format(self.nomFichier))


    def affichePS(self):
        """Affiche le graphique avec Ghostview."""
        os.system("gv {0}.eps &".format(self.nomFichier))


##################################
# Définition de la fonction plot #
##################################

def plot(nomFichier, boite, zoom, courbes, *textes,
        marge=1.1, epaisseurTrait=0.4, epaisseurAxes=0.2,
        ratioY=1, gradX=1, gradY=1, gradH=0.05,
        taillePolice=10, axes=True, etiquette=True, PDF=True):
    taillePolice /= zoom
    graphique = Plot(nomFichier, boite, zoom,
        marge, epaisseurTrait, epaisseurAxes, ratioY,
        gradX, gradY, gradH, taillePolice,
        axes, etiquette, PDF)
    graphique.preambule()

    if axes == True:
        graphique.ajouteAxes()
        if etiquette == True:
            graphique.ajouteEtiquette()

    graphique.cadre()

    for courbe in courbes:
        if len(courbe) == 1:
            # par défaut le bleu est la couleur de tracé
            [liste] = courbe
            graphique.ajouteCourbe(liste, (0, 0, 1), epaisseurTrait)
        elif len(courbe) == 2:
            # le deuxième argument est la couleur donnée sous la forme d'un t-uplet RGB
            [liste, couleur] = courbe
            graphique.ajouteCourbe(liste, couleur, epaisseurTrait)
        elif len(courbe) == 3:
            # le troisième argument est l'épaisseur du trait
            [liste, couleur, trait] = courbe
            graphique.ajouteCourbe(liste, couleur, trait)
        elif len(courbe) == 4:
            [liste, couleur, trait] = courbe[:-1]
            option = courbe[-1]
            if option == 'fill':
                # si le quatrième argument est 'fill', l'enveloppe convexe de la
                # courbe est remplie
                graphique.ajouteCourbe(liste, couleur, trait, fill=True)
            else:
                # si le quatrième argument est une liste, le tracé est en pointillé
                graphique.ajouteCourbe(liste, couleur, trait, style=option)

    for texte in textes:
        [texte, position, couleur] = texte
        graphique.ajouteTexte(texte, position, couleur)

    graphique.fin()

    # Conversion au format PDF
    if PDF==True:
        graphique.exportePDF()

    # Affichage du résultat
    graphique.affichePS()



################
# Les exemples #
################

if __name__ == "__main__":

    from math import *

    #########################################
    # Tracé des fonctions sinus et cosinus  #
    #########################################
    numpoints, a, b, zoom = 100, - 1.4 , 2 * pi, 40
    nomFichier = "sin_cos"
    rouge, bleu = (1, 0, 0), (0, 0, 1)
    boite = [-1.7, -1.7, 6.4, 1.7] # xmin, ymin, xmax, ymax

    # Liste de points à tracer
    liste_s = ((x, sin(x)) for x in nrange(a, b, numpoints))
    liste_c = ((x, cos(x)) for x in nrange(a, b, numpoints))

    # Création du fichier EPS - Tracé en couleurs et en traits pleins
    plot(nomFichier, boite, zoom,
            [[liste_s, bleu], [liste_c, rouge, 0.4]],
            ['sin', [6, -0.5], bleu], ['cos', [6, 1.1], rouge])

    # Création du fichier EPS - Tracé en N&B, en traits pleins et discontinus
    #plot(nomFichier, boite, zoom,
    #        [[liste_s, (0.3,) * 3, 0.7], [liste_c, (0.1,) * 3, 0.7, [0.25, 0.15, 0.05, 0.1]]],
    #        ['sin', [6, -0.5], (0.3,) * 3], ['cos', [6, 1.1], (0.1,) * 3])

    #################################################################
    # Tracé de la rosace d'équation rho = 1 + cos(theta*20/19) / 3  #
    #################################################################
    N, a, b = 1000, 0, 1 + floor(38 * pi)
    nomFichier, zoom = "polar", 100
    boite = [-1.5, -1.5, 1.5, 1.5] # xmin , ymin, xmax, ymax

    # Fonction définissant la courbe polaire
    def f(theta):
        return 1 + cos(theta*20/19) / 3

    # Liste de points à tracer
    liste = ((f(theta) * cos(theta), f(theta) * sin(theta))
            for theta in nrange(a, b, N))

    # Création du fichier EPS
    plot(nomFichier, boite, zoom, [[liste]])

    #########################################
    # Suite de fonctions  x |-> (1-x^2)^n   #
    #########################################
    numpoints, a, b, fichier, zoom = 100, -1.2 , 1.2, "suite", 100
    boite = [-1.3, -0.3, 1.3, 1.3] # xmin, ymin, xmax, ymax

    # Liste de points à tracer
    liste = ((((x, (1-x**2)**n)
            for x in nrange(a, b, numpoints)),
            (n/30, 0.32, 0.47 - n/64))
            for n in range(1, 31))

    # Création du fichier EPS
    plot(fichier, boite, zoom, liste, gradH=.03, etiquette=False)



