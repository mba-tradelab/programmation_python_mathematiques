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
# fichier: outils.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/12/04
#
# (tous les symboles non internationaux sont volontairement omis)
#

import sys
sys.setrecursionlimit(10000)



#
# (a, b) dans N x N*
#
def reste(a, b):
	if a < b:
		return a
	else:
		return reste(a - b, b)



#
# (a, b) dans N x N*
#
def quotient_entier(a, b):
	if a < b:
		return 0
	else:
		return 1 + quotient_entier(a - b, b)



#
# (a, b) dans N x N
#
def pgcd(a, b):
	if b == 0:
		return a
	else:
		return pgcd(b, reste(a, b))



#
# (a, b) dans N x N*
#
def fraction_cont_pos(q, a, b):
	q.append(quotient_entier(a, b))
	if reste(a, b) > 0:
		return fraction_cont_pos(q, b, reste(a, b))
	else:
		return q



#
# (a, b) dans Z x N*
#
def fraction_cont_b_pos(a, b):
	q = []
	if a < 0:
		q.append(-quotient_entier(-a + b, b))
	else:
		q.append(quotient_entier(a, b))
	return q + fraction_cont_pos([], a - b * q[0], b)[1:]



#
# (a, b) dans Z x Z*
#
def fraction_cont(a, b):
	if b < 0:
		return fraction_cont_b_pos(-a, -b)
	else:
		return fraction_cont_b_pos(a, b)

