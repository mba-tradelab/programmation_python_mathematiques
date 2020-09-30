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
# fichier: mafile.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/12/03
#
# (tous les symboles non internationaux sont volontairement omis)
#

import maliste



class mafile(maliste.maliste):

	def __init__(self, l =[]):
		super().__init__(l, 0)
		


	def inscrire_dernier(self, x):
		self.inscrire(x) 
		


	def extraire_premier(self):
		return self.extraire()
		


	def lire_premier(self):
		return self.lire()



