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
# fichier: fraccont3.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/12/06
#
# (tous les symboles non internationaux sont volontairement omis)
#

import partent



def f(u):
	m, d, a, k, p_e_k = u[0], u[1], u[2], u[3], u[4]
	
	mp = d*a - m
	dp = (k - mp**2) // d
	ap = (p_e_k + mp) // dp
	
	return (mp, dp, ap, k, p_e_k)



def terme(n, u_0):
	if n > 0:
		return f(terme(n - 1, u_0))	
	else:
		return u_0



def boucle_rec(acc, n, u_0):
	u = terme(n, u_0)
	if not (u in acc):
		acc.append(u)
		boucle_rec(acc, (n+1), u_0)



def boucle(u_0):
	n = 0
	acc = []
	boucle_rec(acc, n, u_0)
	return [u[2] for u in acc]


	
def calcul(k):
	p_e_k = partent.partie_entiere_racine(k)
	if p_e_k**2 == k:
		return [p_e_k]
	else:
		u_0 = (0, 1, p_e_k, k, p_e_k)
		return boucle(u_0)


	
if __name__ == "__main__":
	print(calcul(8))
	print(calcul(9))
	print(calcul(11))
	print(calcul(12))
	print(calcul(13))
	print(calcul(61))
	print(calcul(227))
	print(calcul(263))
#	print(calcul(61))
#	print(calcul(61))
