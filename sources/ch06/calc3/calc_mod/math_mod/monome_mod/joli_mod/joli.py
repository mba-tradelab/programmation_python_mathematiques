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
# fichier: joli.py
# version: 0.5.0
#  auteur: Pascal CHAUVIN
#    date: 2014/10/28
#
# (tous les symboles non internationaux sont volontairement omis)
#

import string

class joli(object):

	def __init__(self, car ="?"): # const. globale: "?" vaut monome.INDET_DEG_0
		""" - """
		self.__car = car
		self.__nombre = 1
		self.__gauche = None
		self.__droite = None



	def car(self):
		""" - """
		return self.__car



	def nombre(self):
		""" - """
		return self.__nombre



	def a_plat(self, concis =True):
		""" - """
		s = ""
		
		liaison = " * "
		if concis: liaison = "*"
		
		if self.__gauche is not None:
			s = liaison + self.__gauche.a_plat(concis)
			
		if self.__nombre == 1:
			s = "{}".format(self.__car) + s
		else:
			s = "{}^{}".format(self.__car, self.__nombre) + s
		
		if self.__droite is not None:
			s = self.__droite.a_plat(concis) + liaison + s
		
		return s


		
	def __repr__(self):
		""" - """
		return "[joli:\n__car={},\n__nombre={},\n__gauche={},\n__droite={}\n]\n"\
			.format(self.__car, self.__nombre, id(self.__gauche), id(self.__droite))



	def __str__(self):
		""" - """
		return self.a_plat()


		
	def inserer(self, x):
		""" - """
		if not(x in string.ascii_letters):
			return
			
		if self.__car == x:
			self.__nombre += 1
			return
		
		if self.__car < x:
			if self.__gauche is None:
				self.__gauche = joli(x)
			else:
				self.__gauche.inserer(x)
			return
				
		if self.__droite is None:
			self.__droite = joli(x)
		else:
			self.__droite.inserer(x)



	def nombre_noeuds(self):
		""" - """
		n = 1
		if self.__gauche is not None:
			n += self.__gauche.nombre_noeuds()
			
		if self.__droite is not None:
			n += self.__droite.nombre_noeuds()
		
		return n



def format_indet(s, concis =True):
	""" - """
	if len(s) == 0:
		return ""
		
	n = joli(s[0])
	s = s[1:]
	for c in s: n.inserer(c)
	
	return n.a_plat(concis)

