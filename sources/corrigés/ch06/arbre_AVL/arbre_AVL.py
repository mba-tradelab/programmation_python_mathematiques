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
# fichier: arbre_AVL.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/12/20
#
# (tous les symboles non internationaux sont volontairement omis)
#

class arbre(object):

	def __init__(self, clef =0, gauche =None, droit =None):
		self.__clef = clef
		self.__gauche = gauche
		self.__droit = droit



	def __hauteur(self):
		hauteur_a_gauche = 0
		if self.__gauche is not None:
			hauteur_a_gauche = self.__gauche.__hauteur()
			
		hauteur_a_droite = 0
		if self.__droit is not None:
			hauteur_a_droite = self.__droit.__hauteur()
			
		return (1 + max(hauteur_a_gauche, hauteur_a_droite))



	def __delta_hauteur(self):
		hauteur_a_gauche = 0
		if self.__gauche is not None:
			hauteur_a_gauche = self.__gauche.__hauteur()
			
		hauteur_a_droite = 0
		if self.__droit is not None:
			hauteur_a_droite = self.__droit.__hauteur()
			
		return (hauteur_a_gauche - hauteur_a_droite)



	def __rotation_a_gauche(self):
		self.__clef, self.__droit.__clef = self.__droit.__clef, self.__clef

		t = self.__gauche

		self.__gauche = self.__droit
		self.__droit = self.__droit.__droit

		self.__gauche.__droit = self.__gauche.__gauche
		self.__gauche.__gauche = t



	def __rotation_a_droite(self):
		self.__clef, self.__gauche.__clef = self.__gauche.__clef, self.__clef

		t = self.__droit

		self.__droit = self.__gauche
		self.__gauche = self.__gauche.__gauche

		self.__droit.__gauche = self.__droit.__droit
		self.__droit.__droit = t



	def __equilibrer(self):
		d = self.__delta_hauteur()
		if d > 1:
			if self.__gauche.__delta_hauteur() < 1:
				self.__gauche.__rotation_a_gauche()
			self.__rotation_a_droite()

		if d < -1:
			if self.__droit.__delta_hauteur() > -1:
				self.__droit.__rotation_a_droite()
			self.__rotation_a_gauche()



	def inserer(self, clef):
		if clef < self.__clef:
			if self.__gauche is None:
				self.__gauche = arbre(clef)
			else:
				self.__gauche.inserer(clef)
		else:
			if self.__droit is None:
				self.__droit = arbre(clef)
			else:
				self.__droit.inserer(clef)
				
		self.__equilibrer()



	def afficher(self, decalage =0):
		if self.__droit is not None:
			self.__droit.afficher(decalage + 2)
			
		print("    " * decalage + ("{:3d}".format(self.__clef)))
		
		if self.__gauche is not None:
			self.__gauche.afficher(decalage + 2)

