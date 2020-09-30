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

def fibo_rec_term(n, i, a, b):
	if i == n:
		return b
	else:
		return fibo_rec_term(n, i + 1, a + b, a)

#
# fonction d'enveloppe
#
def fibo(n):
	return fibo_rec_term(n, 0, 1, 1)

#
# appels
#
for n in range(12):
	print(fibo(n))

print(fibo(40))
