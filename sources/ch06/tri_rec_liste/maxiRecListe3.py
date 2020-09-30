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

from random import *

#
# recherche recursive du maximum
#
def maxi_rec(l):
	if len(l) > 1:
		maxi = maxi_rec(l[:-1])
		if maxi > l[-1]:
			return maxi
		else:
			return l[-1]
	else:
		return l[0]

class table(object):

	def __init__(self, taille):
		self.__liste = [randrange(1, 100) for n in range(taille)]

	def __str__(self):
		return str(self.__liste)

	def maximum(self):
		return maxi_rec(self.__liste)

if __name__ == "__main__":
	liste = table(10)
	print(liste)
	print(liste.maximum())
