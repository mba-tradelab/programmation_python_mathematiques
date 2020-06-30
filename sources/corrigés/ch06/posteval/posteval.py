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
# fichier: posteval.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/12/03
#
# (tous les symboles non internationaux sont volontairement omis)
#

import mafile
import mapile



def boucle(acc, p):
	if not p.est_vide():
		x = p.extraire()
		if x in "0123456789":
			acc.inscrire(int(x))
		else:
			if x == "+":
				b = acc.extraire()
				a = acc.extraire()
				acc.inscrire(a + b)
			
			if x == "-":
				b = acc.extraire()
				a = acc.extraire()
				acc.inscrire(a - b)
			
			if x == "*":
				b = acc.extraire()
				a = acc.extraire()
				acc.inscrire(a * b)
			
			if x == "/":
				b = acc.extraire()
				a = acc.extraire()
				acc.inscrire(a / b)
			
		boucle(acc, p)



def evaluer(p):
	acc = mapile.mapile()
	boucle(acc, p)	
	print(acc.extraire())



if __name__ == "__main__":
	f = mafile.mafile()

	for c in "423+*5-":
		f.inscrire(c)
	
	evaluer(f)

