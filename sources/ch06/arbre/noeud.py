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

class noeud(object):
	""" noeud double (deux fils) """



	def __init__(self, num, gauche =None, droite =None):
		""" constructeur """
		self.__num = num
		self.__gauche = gauche
		self.__droite = droite

	

	def montrer(self, decal_horiz =0):
		""" imprimer le noeud avec ses fils """
		if self.__droite:
			self.__droite.montrer(decal_horiz + 3)
		print(" " * decal_horiz, self.__num)
		if self.__gauche:
			self.__gauche.montrer(decal_horiz + 3)



	def chercher(self, num):
		""" chercher une valeur """
		if num == self.__num:
			return True

		if num < self.__num:
			if self.__gauche:
				return self.__gauche.chercher(num)
			else:
				return False
		else:
			if self.__droite:
				return self.__droite.chercher(num)
			else:
				return False



	def inserer(self, num):
		""" insérer une valeur """
		if num != self.__num:
			if num < self.__num:
				if self.__gauche:
					self.__gauche.inserer(num)
				else:
					self.__gauche = noeud(num)
			else:
				if self.__droite:
					self.__droite.inserer(num)
				else:
					self.__droite = noeud(num)
		else:
			print("(pas de doublon dans un arbre binaire de recherche)")



	def plus_grand(self):
		if self.__droite:
			return self.__droite.plus_grand()
		else:
			return self.__num

	def plus_petit(self):
		if self.__gauche:
			return self.__gauche.plus_petit()
		else:
			return self.__num



	def get_num(self):
		return self.__num

	def set_num(self, num):
		self.__num = num



	def fils_gauche(self):
		""" accesseur fils gauche """
		return self.__gauche

	def fils_droite(self):
		""" accesseur fils droit """
		return self.__droite



	def noeuds(self):
		n = 1
		if self.__gauche:
			n = n + self.__gauche.noeuds()
		if self.__droite:
			n = n + self.__droite.noeuds()
		return n



	def chercher_parent(self, num):
		if num == self.__num:
			return None

		if num < self.__num:
			if self.__gauche.__num == num:
				return self
			else:
				return self.__gauche.chercher_parent(num)
		else:
			if self.__droite.__num == num:
				return self
			else:
				return self.__droite.chercher_parent(num)

	def supprimer_noeud(self, num, parent):
		if num < self.__num:
			self.__gauche.supprimer_noeud(num, parent)
		else:
			if num > self.__num:
				self.__droite.supprimer_noeud(num, parent)
			else:
				if self.__gauche is None and self.__droite is None: # aucun fils
					if parent.__gauche is self:
						parent.__gauche = None
					else:
						parent.__droite = None
				else:
					if self.__gauche is None or self.__droite is None: # fils unique

						if self.__gauche:
							t = self.__gauche
						else:
							t = self.__droite

						if parent.__gauche is self:
							s = parent.__gauche
							parent.__gauche = t
						else:
							s = parent.__droite
							parent.__droite = t
						s.__gauche = None
						s.__droite = None

					else: # deux fils
						if self.__gauche.noeuds() > self.__droite.noeuds():
							x = self.__gauche.plus_grand()
						else:
							x =  self.__droite.plus_petit()
						self.supprimer(x)
						self.__num = x

	def supprimer(self, num):
		""" supprimer une valeur (existante) """
		parent = self.chercher_parent(num)
		self.supprimer_noeud(num, parent)



	def montrer_ordre_croissant(self):
		if self.__gauche:
			self.__gauche.montrer_ordre_croissant()
		print(self.__num)
		if self.__droite:
			self.__droite.montrer_ordre_croissant()

	def montrer_ordre_decroissant(self):
		if self.__droite:
			self.__droite.montrer_ordre_decroissant()
		print(self.__num)
		if self.__gauche:
			self.__gauche.montrer_ordre_decroissant()



	def __liste_ordre_croissant(self, liste):
		if self.__gauche:
			self.__gauche.__liste_ordre_croissant(liste)
		liste.append(self.__num)
		if self.__droite:
			self.__droite.__liste_ordre_croissant(liste)

	def liste_croissante(self):
		liste = []
		self.__liste_ordre_croissant(liste)
		return liste



	def __liste_ordre_decroissant(self, liste):
		if self.__droite:
			self.__droite.__liste_ordre_decroissant(liste)
		liste.append(self.__num)
		if self.__gauche:
			self.__gauche.__liste_ordre_decroissant(liste)

	def liste_decroissante(self):
		liste = []
		self.__liste_ordre_decroissant(liste)
		return liste

