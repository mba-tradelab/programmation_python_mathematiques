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

class quadrilatere(object):
	"""quadrilatere quelconque"""

	def __init__(self, a =0, b =0, c =0 , d=0):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.type = "quadrilatere"

	def __str__(self):
		return self.type
	
	def perimetre(self):
		return (self.a + self.b + self.c + self.d)

if __name__ == "__main__":
	q = quadrilatere(5, 7, 10, 3.4)
	print(q)
	print(q.perimetre())
