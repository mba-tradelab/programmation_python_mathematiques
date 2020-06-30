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
# fichier: rationnel.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/12/04
#
# (tous les symboles non internationaux sont volontairement omis)
#

import outils



class rationnel(object):

	def __init__(self, num =0, denom =1):
		"""  """
		self.__num, self.__denom = num, denom

		if denom < 0:
			p = -num
			q = -denom
		else:
			p = num
			q = denom

		d = outils.pgcd(abs(p), q)

		self.__num = p // d
		self.__denom = q // d



	def __str__(self):
		"""  """
		if self.__denom == 1:
			return str(self.__num)
		else:
			return str(self.__num) + "/" + str(self.__denom)



	def __add__(self, autre):
		"""  """
		num = self.__num * autre.__denom + self.__denom * autre.__num
		denom = self.__denom * autre.__denom
		return rationnel(num, denom)



	def __truediv__(self, autre):
		"""  """
		if autre.__num == 0:
			return rationnel() # il conviendrait de lever une exception ici.
		
		num = self.__num * autre.__denom
		denom = self.__denom * autre.__num
		return rationnel(num, denom)



	def fraction_continue(self):
		"""  """
		return outils.fraction_cont(self.__num, self.__denom)



def reduite(quotients, r):
	if len(quotients) > 0:
		return rationnel(quotients[0]) + rationnel(1) / reduite(quotients[1:], r)
	else:
		return r



def calcul_reduite(quotients):
	return reduite(quotients, rationnel())

