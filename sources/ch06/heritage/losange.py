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

from quadrilatere import *

class losange(quadrilatere):
	"""losange"""

	def __init__(self, a =0):
		quadrilatere.__init__(self, a, a, a, a)
		self.type = "losange"
	
	def perimetre(self):
		return self.a*4

if __name__ == "__main__":
	l = losange(5)
	print(l)
	print(l.perimetre())
