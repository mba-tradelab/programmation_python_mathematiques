#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
# (C) Alexandre Casamayou-Boucau, Pascal Chauvin, Guillaume Connan     #
#                                                                      #
# Complément de l'ouvrage :                                            #
# Programmation en Python pour les mathématiques                       #
# Editeur : Dunod                   -        Collection : Sciences Sup #
# ISBN-13: 978-2100738311           -                  Licence : GPLv2 #
########################################################################

from math import sqrt
from turtle import *

def dragon_gauche(taille, niveau):
	color("red")
	if niveau == 0:
		forward(taille)
	else:
		left(45)
		dragon_gauche(taille/sqrt(2), niveau-1)
		right(90)
		dragon_droite(taille/sqrt(2), niveau-1)
		left(45)

def dragon_droite(taille, niveau):
	color("blue")
	if niveau == 0:
		forward(taille)
	else:
		right(45)
		dragon_gauche(taille/sqrt(2), niveau-1)
		left(90)
		dragon_droite(taille/sqrt(2), niveau-1)
		right(45)

def figure():
	dragon_droite(400, 12)

if __name__ == "__main__":
    #
    speed("fastest")
    up()
    goto(-200, 0)
    down()
    #
    figure()

    nomFichier = "dragon1"
    from tkinter import *
    import turtle
    turtle.ht()
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="{0}.eps".format(nomFichier))
    import os
    os.system("epstopdf {0}.eps".format(nomFichier))
    turtle.mainloop()
