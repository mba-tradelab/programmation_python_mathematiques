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
# fichier: mapile.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/12/03
#
# (tous les symboles non internationaux sont volontairement omis)
#

import maliste



class mapile(maliste.maliste):

	def __init__(self, l =[]):
		super().__init__(l, -1)



	def empiler(self, x):
		self.inscrire(x)



	def depiler(self):
		return self.extraire() 



	def lire_sommet(self):
		return self.lire()



if __name__ == "__main__":	
	p = mapile()

	for x in "Programmez avec Python3":
		p.inscrire(x)
	
	print(p)
	
	x = p.extraire()
	while x is not None:
		print(x)
		x = p.extraire()

