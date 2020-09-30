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


import turtle

turtle.pen(speed = 0)

def von_koch(longueur, n):
   if n == 1:
       turtle.forward(longueur)
   else:
       d = longueur / 3.
       von_koch(d, n - 1)
       turtle.left(60)
       von_koch(d, n - 1)
       turtle.right(120)
       von_koch(d, n - 1)
       turtle.left(60)
       von_koch(d, n - 1)

def flocon(longueur, n):
   turtle.up()
   turtle.goto(- longueur / 2, longueur / 3)
   turtle.down()
   for i in range(3):
       von_koch(longueur, n)
       turtle.right(120)

flocon(300, 6)

# Pour exporter le graphique au format eps :
from tkinter import *
import os
nomFichier = "von_koch"
turtle.ht()
ts = turtle.getscreen()
ts.getcanvas().postscript(file="{0}.eps".format(nomFichier))
os.system("epstopdf {0}.eps".format(nomFichier))
turtle.mainloop()
