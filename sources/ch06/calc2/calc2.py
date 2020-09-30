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

from expression import *

def tests_automatiques():
	e = expression("{ (3 + 4) * 5 ^ (1 + 1) - 7 }")
	print("Exemple de calcul :", e)
	print(e.valeur(), '\n') # donne 168

	e = expression("{ 2 ^ 3 ^ 2 ^ 2 }")
	print("Exemple de calcul :", e)
	print(e.valeur(), '\n') # donne 2417851639229258349412352
	
	e = expression("{ ( 9 + 1 ) * ( 7 + 2 * 5 ) }")
	print("Exemple de calcul :", e)
	print(e.valeur(), '\n') # donne 170

	e = expression("{ 3/7 - 2/7 : ( 5 : 14 ) }")
	print("Exemple de calcul :", e)
	print(e.valeur(), '\n') # donne -13/35

def lecture_expr():
	print("---")
	print("Calcul suivant (laisser vide et valider pour quitter):")
	return input()

def boucle():
	expr = lecture_expr()
	while len(expr) > 0:
		e = expression("{" + expr + "}")
		print((e.valeur()))
		print()
		expr = lecture_expr()

if __name__ == "__main__":
	tests_automatiques()
	boucle()

