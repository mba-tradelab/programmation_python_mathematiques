#!/usr/bin/env python
# -*- coding:Utf-8 -*-

########################################################################
# (C) Alexandre Casamayou-Boucau, Pascal Chauvin, Guillaume Connan     #
#                                                                      #
# Complément de l'ouvrage :                                            #
# Programmation en Python pour les mathématiques                       #
# Editeur : Dunod                   -        Collection : Sciences Sup #
# ISBN-13: 978-2100738311           -                  Licence : GPLv2 #
########################################################################


# simulation planche de Galton

from random import *
from turtle import *

def chute(niveaux):
	c = ""
	for n in range(niveaux):
		if random() < 0.5:
			c = c + 'G'
		else:
			c = c + 'D'
	return c

def tirage(niveaux):
	cibles = [n for n in range(niveaux + 1)]
	c = chute(niveaux)
	for n in c:
		if n == 'G':
			cibles.pop()
		else:
			cibles.pop(0)
	return cibles[0]

def simulation(billes, niveaux):
	print("simulation de", billes, "sur un crible de", niveaux, "niveaux :")
	tas = [0] * (niveaux + 1)
	for b in range(billes):
		tas[tirage(niveaux)] += 1
		print(tas)
	print()

def rectangle(largeur, hauteur):
	couleur = (random(), random(), random()) # en couleur
	#couleur = (random(), )*3                # en N&B
	color(couleur)
	begin_fill()
	for n in range(2):
		forward(largeur)
		left(90)
		forward(hauteur)
		left(90)
	end_fill()

def diagramme(billes, niveaux):

	### simulation ###
	tas = [0] * (niveaux + 1)
	for b in range(billes):
		tas[tirage(niveaux)] += 1
	print(tas)

	### dessin ###
	largeur = 50
	hauteur_max = 0
	billes_max = 0
	for n in tas:
		if n > hauteur_max:
			hauteur_max = n
			billes_max = n

	### centrage et mise a l'échelle ###
	up()
	goto( -largeur * (niveaux + 1)/2, -float(billes_max)/billes * hauteur_max/2)
	down()
	speed("fastest")

	for n in tas:
		rectangle(largeur, float(n)/billes * hauteur_max)
		forward(largeur)
	up()

if __name__ == "__main__":

    diagramme(5000, 10)

    from tkinter import *
    import os
    ht()
    ts = getscreen()
    ts.getcanvas().postscript(file="{0}.eps".format("galton"))
    os.system("epstopdf {0}.eps".format("galton"))
    mainloop()
