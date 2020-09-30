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

from string import *
from rationnel import *

class noeud2(object):
	""" noeud double (pour un arbre binaire)"""

	def __init__(self, donnee =None, gauche =None, droite =None):
		self.__donnee = donnee
		self.__gauche = gauche
		self.__droite = droite

	def en_chaine_prefixe(self):
		if self.__donnee[-1] in digits:
			return str(self.__donnee)
		if isinstance(self.__gauche, rationnel):
			operande_gauche = str(self.__gauche)
		else:
			operande_gauche = self.__gauche.en_chaine_prefixe()
		if isinstance(self.__droite, rationnel):
			operande_droite = str(self.__droite)
		else:
			operande_droite = self.__droite.en_chaine_prefixe()
		op = self.__donnee
		return str(op) + '|' + str(operande_gauche) + '|' + str(operande_droite)

	def en_chaine_infixe(self):
		if self.__donnee[-1] in digits:
			return str(self.__donnee)
		if isinstance(self.__gauche, rationnel):
			operande_gauche = str(self.__gauche)
		else:
			operande_gauche = self.__gauche.en_chaine_infixe()
		if isinstance(self.__droite, rationnel):
			operande_droite = str(self.__droite)
		else:
			operande_droite = self.__droite.en_chaine_infixe()
		op = self.__donnee
		return '(' + str(operande_gauche) + str(op) + str(operande_droite) + ')'

	def en_chaine_postfixe(self):
		if self.__donnee[-1] in digits:
			return str(self.__donnee)
		if isinstance(self.__gauche, rationnel):
			operande_gauche = str(self.__gauche)
		else:
			operande_gauche = self.__gauche.en_chaine_postfixe()
		if isinstance(self.__droite, rationnel):
			operande_droite = str(self.__droite)
		else:
			operande_droite = self.__droite.en_chaine_postfixe()
		op = self.__donnee
		s = str(operande_gauche) + '|' + str(operande_droite)
		s = s + '|' + op
		return s

	def donnee(self):
		return self.__donnee

