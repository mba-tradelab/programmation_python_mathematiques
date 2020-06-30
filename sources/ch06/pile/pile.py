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

class pile(object):
	""" pile """

	def __init__(self):
		self.__sommet = None

	def __str__(self):
		s = []
		n = self.__sommet
		while not (n is None):
			s.append(n.get_donnee())
			n = n.get_suivant()
		return str(s)

	def est_vide(self):
		return (self.__sommet is None)

	def empiler(self, d):
		n = noeud(d)
		n.set_suivant(self.__sommet)
		self.__sommet = n

	def depiler(self):
		if self.__sommet is None:
			return None
		n = self.__sommet
		d = n.get_donnee()
		self.__sommet = n.get_suivant()
		n = None
		return d

if __name__ == "__main__":
	p = pile()
	p.empiler("GNU")
	p.empiler("is")
	p.empiler("not")
	p.empiler("Unix")
	
	print(p)
	while not p.est_vide():
		print(p.depiler())

