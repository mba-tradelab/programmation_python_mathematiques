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

from arbre import *

def calculer(expression):
	e = arbre(expression)
	print("- forme initiale ........ :", expression)
	print("- expression préfixe .... :", e.prefixe())
	print("- expression infixe ..... :", e.infixe())
	print("- expression postfixe ... :", e.postfixe())
	print("- valeur obtenue ........ :", e.evaluer())
	print()

def tests_automatiques():
	# donne 3 4 + 5 1 1 + ^ * 7 - = 168
	print("Exemple de calcul :")
	calculer("(3 + 4) * 5 ^ (1 + 1) - 7")

	# donne 2 3 2 2 ^ ^ ^ = 2417851639229258349412352
	print("Exemple de calcul :")
	calculer("2 ^ 3 ^ 2 ^ 2")

	# donne 9 1 + 7 2 5 * + *
	print("Exemple de calcul :")
	calculer(" ( 9 + 1 ) * ( 7 + 2 * 5 ) ")

	# donne 3 7 : 2 7 : 5 14 : : -
	print("Exemple de calcul :")
	calculer(" 3/7 - 2/7 : ( 5 : 14 ) ")

def lecture_expr():
	print("---")
	print("Calcul suivant (laisser vide et valider pour quitter):")
	return input()

def boucle():
	expr = lecture_expr()
	while len(expr) > 0:
		calculer(expr)
		expr = lecture_expr()

if __name__ == "__main__":
	tests_automatiques()
	boucle()

