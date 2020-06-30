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
# fichier: fraccont1.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/11/27
#
# (tous les symboles non internationaux sont volontairement omis)
#



#
# (a, b) dans N x N*
#
def __fraction_cont_pos(q, a, b):
	q.append(a // b)
	r = a % b
	if r > 0:
		return __fraction_cont_pos(q, b, r)
	else:
		return q



#
# (a, b) dans Z x N*
#
def __fraction_cont_b_pos(a, b):
	q = []
	if a < 0:
		q.append(-((-a + b) // b))
	else:
		q.append(a // b)
	return q + __fraction_cont_pos([], a - b * q[0], b)[1:]



#
# (a, b) dans Z x Z*
#
def fraction_cont(a, b):
	if b < 0:
		return __fraction_cont_b_pos(-a, -b)
	else:
		return __fraction_cont_b_pos(a, b)



x = fraction_cont(111, 40)
print(x)

x = fraction_cont(-111, 40)
print(x)



