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

from turtle import *

def drapeau(longueur, niveau):
	if niveau == 0:
		down()
		cap = heading()
		if cap == 0 or cap == 180:
			color("red")
		if cap == 60 or cap == 240:
			color("green")
		if cap == 120 or cap == 300:
			color("blue")
		forward(longueur)
		up()
	else:
		drapeau(longueur/2, niveau-1)
		left(120)
		drapeau(longueur/2, niveau-1)
		left(120)
		drapeau(longueur/2, niveau-1)
		left(120)
		forward(longueur)

def triangle(longueur, niveau):
	for i in range(3):
		drapeau(longueur, niveau)
		left(120)

def figure():
	triangle(600, 6)

if __name__ == "__main__":
    up()
    goto(-300, -280)
    down()
    speed("fastest")
    figure()
    up()

    nomFichier = "sierpinsky2"
    from tkinter import *
    import turtle
    turtle.ht()
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="{0}.eps".format(nomFichier))
    import os
    os.system("epstopdf {0}.eps".format(nomFichier))
    turtle.mainloop()
