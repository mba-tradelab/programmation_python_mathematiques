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
#    date: 2014/11/26
#
# (tous les symboles non internationaux sont volontairement omis)
#

def est_vide(l):
	return len(l) == 0



def tete(l):
	if est_vide(l):
		return None
	else:
		return l[0]



def suite(l):
	if est_vide(l):
		return []
	else:
		return l[1:]



def longueur(l):
	if est_vide(l):
		return 0
	else:
		return 1 + longueur(suite(l))



def debut_rec(n, l, acc):
	if n == 0:
		return acc
	else:
		x = tete(l)
		if x is not None:
			acc.append(x)
			debut_rec(n - 1, suite(l), acc)



def debut(n, l):
	acc = []
	debut_rec(n, l, acc)
	return acc



def coupe(n, l):
	if n == 0:
		return l
	else:
		return coupe(n - 1, suite(l))

