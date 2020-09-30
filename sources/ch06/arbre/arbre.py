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

import random
from string import *

from noeud import *

class arbre(object):
	""" arbre binaire de recherche """

	def __init__(self):
		""" constructeur """
		self.__racine = None

	def montrer(self):
		""" imprimer l'arbre """
		if self.__racine:
			self.__racine.montrer()
		else:
			print("(arbre vide)")

	def chercher(self, num):
		""" rechercher une valeur """
		if self.__racine:
			return self.__racine.chercher(num)
		else:
			return False

	def inserer(self, num):
		""" inserer une nouvelle valeur """
		if self.__racine:
			self.__racine.inserer(num)
		else:
			self.__racine = noeud(num)

	def supprimer(self, num):
		""" supprimer une valeur """
		if self.chercher(num):
			if self.__racine.get_num() == num:
				if self.__racine.fils_gauche():
					fils = self.__racine.fils_gauche()
				else:
					fils = self.__racine.fils_droite()
				if fils is None:
					self.__racine = None
				else:
					if self.__racine.fils_gauche():
						x = fils.plus_grand()
					else:
						x = fils.plus_petit()
					self.__racine.supprimer(x)
					self.__racine.set_num(x)
			else:
				self.__racine.supprimer(num)
		else:
			print("(valeur inexistante)")

	def montrer_ordre_croissant(self):
		""" montrer la liste en ordre croissant """
		if self.__racine:
			self.__racine.montrer_ordre_croissant()
		else:
			print("(liste vide)")

	def montrer_ordre_decroissant(self):
		""" montrer la liste en arbre decroissant """
		if self.__racine:
			self.__racine.montrer_ordre_decroissant()		
		else:
			print("(liste vide)")

	def liste_croissante(self):
		""" liste en ordre croissant """
		if self.__racine:
			return self.__racine.liste_croissante()
		else:
			return []

	def liste_decroissante(self):
		""" liste en ordre decroissant """
		if self.__racine:
			return self.__racine.liste_decroissante()
		else:
			return []

	def noeuds(self):
		""" nombre de noeuds de l'arbre """
		if self.__racine:
			return self.__racine.noeuds()
		else:
			return 0

if __name__ == "__main__":
	a = arbre()
	for n in range(10):
		a.inserer(random.randrange(100))

	a.montrer()

	print("(" + str(a.noeuds()) + " noeud(s) dans l'arbre)")

	fin = False
	while fin == False:
		print("***************************************")
		print("(a)jouter ou (c)roissant ou (d)ecroissant")
		print("ou (s)upprimer ou (q)uitter ?")
		ch = str(input())
		if ch == 'a' or ch == 's':
			n = int(input())
			print("---------------------------------------")
			if ch == 'a':
				a.inserer(n)
			if ch == 's':
				a.supprimer(n)
			a.montrer()
		if ch == 'c':
			print(a.liste_croissante())
		if ch == 'd':
			print(a.liste_decroissante())
		if ch == 'q':
			fin = True
		if not (ch in "acdsq"):
			print("touches a, c, d, s, q uniquement !")

