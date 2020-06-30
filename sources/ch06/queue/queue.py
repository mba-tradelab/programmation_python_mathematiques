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

from noeud import *

class queue(object):
	""" queue """

	def __init__(self):
		self.__premier = None
		self.__dernier = None

	def __str__(self):
		s = []
		n = self.__premier
		while not (n is None):
			s.append(n.get_donnee())
			n = n.get_suivant()
		return str(s)

	def est_vide(self):
		return (self.__premier is None)

	def ecrire_dernier(self, d):
		n = noeud(d)
		if self.__premier is None:
			self.__premier = n
		else:
			self.__dernier.set_suivant(n)
		self.__dernier = n

	def lire_premier(self):
		if self.__premier is None:
			return None
		n = self.__premier
		d = n.get_donnee()
		self.__premier = n.get_suivant()
		n = None
		return d

if __name__ == "__main__":
	q = queue()
	q.ecrire_dernier("lapin")
	q.ecrire_dernier("chasseur")
	q.ecrire_dernier(2)
	q.ecrire_dernier("le")
	q.ecrire_dernier("retour")

	print(q)
	while not q.est_vide():
		print(q.lire_premier())

