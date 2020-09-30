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

def triangle_vert(c):
	color("green")
	begin_fill()
	for i in range(3):
		forward(c)
		left(120)
	end_fill()
	color("black")
	for i in range(3):
		forward(c)
		left(120)

def triangle_blanc(c):
	color("white")
	begin_fill()
	for i in range(3):
		forward(c)
		left(120)
	end_fill()
	color("black")
	for i in range(3):
		forward(c)
		left(120)

def triangle_marron(c):
	color("maroon")
	begin_fill()
	for i in range(3):
		forward(c)
		left(120)
	end_fill()
	color("black")
	for i in range(3):
		forward(c)
		left(120)

def complet(n, c):
	if n > 0:
		triangle_vert(c)
		triangle_blanc(c/2)
		forward(c/2)
		triangle_marron(c/2)
		backward(c/2)
		left(60)
		forward(c/2)
		right(60)
		complet(n-1, c/2)

up()
goto(-300,-240)
down()
complet(6, 512)

nomFichier = "somme-geom"
ht()
ts = getscreen()
ts.getcanvas().postscript(file="{0}.eps".format(nomFichier))
import os
os.system("epstopdf {0}.eps".format(nomFichier))
mainloop()
