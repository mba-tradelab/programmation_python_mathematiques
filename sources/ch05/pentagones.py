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

from math import *
from turtle import *

def pentagone(cote):
	for n in range(5):
		forward(cote)
		left(72)

def spirale(nombre_penta, cote):
	coeff = 0.1
	a = cote
	d = coeff * a
	for i in range(nombre_penta):
		pentagone(a)
		d = coeff * a
		forward(d)
		a_prime = sqrt((a-d)**2 + d**2 -2*(a-d)*d*(1-sqrt(5))/4)
		angle = (180/pi) * acos( (a_prime**2 + a**2 - 2*a*d)/(2*a_prime*(a-d)) )
		left(angle)
		a = a_prime

def dessin():
	up()
	goto(-190,-280)
	down()
	spirale(50, 370)
	up()

if __name__ == "__main__":
    speed("fastest")
    dessin()

    nomFichier = "pentagones"
    from tkinter import *
    import turtle
    turtle.ht()
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="{0}.eps".format(nomFichier))
    import os
    os.system("epstopdf {0}.eps".format(nomFichier))
    turtle.mainloop()

