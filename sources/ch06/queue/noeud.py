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

class noeud(object):
	""" noeud (liste simple) """

	def __init__(self, donnee =None, suivant =None):
		""" constructeur """
		self.__donnee = donnee
		self.__suivant = suivant

	def __str__(self):
		return str(self.__donnee)

	def get_donnee(self): 
		""" accesseur """
		return self.__donnee

	def set_donnee(self, d):
		""" mutateur """
		self.__donnee = d

	def get_suivant(self):
		return self.__suivant

	def set_suivant(self, s):
		self.__suivant = s

