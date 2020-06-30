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

class rectangle(quadrilatere):
	"""rectangle"""

	def __init__(self, a =0, b =0):
		quadrilatere.__init__(self, a, b, a, b)
		self.type = "rectangle"

#	def perimetre(self):
#		return (self.a + self.b)*2

if __name__ == "__main__":
	r = rectangle(4, 3)
	print(r)
	print(r.perimetre())
