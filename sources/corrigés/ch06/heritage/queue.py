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
# fichier: queue.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/12/01
#
# (tous les symboles non internationaux sont volontairement omis)
#

import liste



class queue(liste.liste):

	def __init__(self, l =[]):
		super().__init__(l, 0)
		


	def inscrire_dernier(self, x):
		self.inscrire(x) 
		


	def extraire_premier(self):
		return self.extraire()
		


	def lire_premier(self):
		return self.lire()



if __name__ == "__main__":	
	q = queue()

	for x in "Programmez avec Python3":
		q.inscrire(x)	# i.e. q.inscrire_dernier()
	
	print(q)
	
	x = q.extraire_premier()	# i.e. x = q.extraire()
	while x is not None:
		print(x)
		x = q.extraire_premier()

