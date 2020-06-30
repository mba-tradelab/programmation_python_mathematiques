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

#
# fichier: dessin.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/11/27
#
# (tous les symboles non internationaux sont volontairement omis)
#

from turtle import *



def carre_rec(n, a):
	if n > 0:
		forward(a)
		left(90)
		carre_rec(n - 1, a)



def carre(c):
	carre_rec(4, c)



def dessin(num, cote):
	if num > 0:
		carre(cote)
		forward(cote)
		left(90)
		cote += 10
		dessin(num - 1, cote)



if __name__ == "__main__":
	dessin(15, 50)
	exitonclick()

