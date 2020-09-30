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
import random
from turtle import *

delta = -300
loupe = 600

class point(object):
	""" Point du plan """

	def __init__(self, x = 0, y = 0, couleur = "black"):
		self.x = x
		self.y = y
		self.couleur = couleur

	def milieu(self, p, couleur = "black"):
		self.x = (self.x + p.x)/2
		self.y = (self.y + p.y)/2
		self.couleur = couleur

	def rouge(self):
		self.couleur = "red"

	def vert(self):
		self.couleur = "green"

	def bleu(self):
		self.couleur = "blue"

	def croix(self):
		down()
		for i in range(4):
			forward(3)
			backward(3)
			left(90)
		up()

	def imprime(self):
		goto(self.x*loupe + delta, self.y*loupe + delta)
		color(self.couleur)
		self.croix()

def figure(points):

	a = point(0.0, 0.0, "red")
	b = point(1.0, 0.0, "green")
	c = point(0.5, sqrt(3)/2, "blue")

	# premier point m, i.e. m(0) choisi ici comme isobarycentre
	m = point(0.5, sqrt(3)/6)

	if points <= 0:
		points = 200

	for i in range(points):
		# obtention aléatoire du point suivant: m(i+1) = milieu [m(i), a ou b ou c]
		alea = random.randrange(3)
		if alea == 0:
			m.milieu(a)
		if alea == 1:
			m.milieu(b)
		if alea == 2:
			m.milieu(c)
		# obtention aléatoire de la couleur du point
		alea = random.randrange(3)
		if alea == 0:
			m.rouge()
		if alea == 1:
			m.vert()
		if alea == 2:
			m.bleu()
		m.imprime()

if __name__ == "__main__":
    print("Triangle de Sierpinsky (génération aléatoire)")

    up()
    speed("fastest")

    figure(2000)

    nomFichier = "sierpinsky3"
    from tkinter import *
    import turtle
    turtle.ht()
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="{0}.eps".format(nomFichier))
    import os
    os.system("epstopdf {0}.eps".format(nomFichier))
    turtle.mainloop()
