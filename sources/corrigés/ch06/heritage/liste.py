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
# fichier: liste.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/12/01
#
# (tous les symboles non internationaux sont volontairement omis)
#

class liste(object):

	def __init__(self, l =[], indice_ext =0):
		self.__elements = l
		self.__indice_ext = indice_ext



	def __str__(self):
		return str(self.__elements)



	def extraire(self):
		if len(self.__elements) == 0:
			return None
		
		x = self.__elements[self.__indice_ext]
		del self.__elements[self.__indice_ext]
		
		return x



	def inscrire(self, x):
		return self.__elements.append(x)



	def lire(self):
		return self.__elements[self.__indice_ext]

