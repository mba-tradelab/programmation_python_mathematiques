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
# fichier: exemple1.py
# version: 0.5.0
#  auteur: Pascal CHAUVIN
#    date: 2014/12/25
#
# (tous les symboles non internationaux sont volontairement omis)
#

from modules_calc3 import *



#
# suite u (définie par récurrence)
#
def u_suivant(u, v):
	return (-u - v)



#
# suite v (définie par récurrence)
#
a = ex_t.expression("4/3").lire_valeur()
b = ex_t.expression("5/3").lire_valeur()

def v_suivant(u, v):
	global a
	global b
	return (a*u + b*v)



#
# suite t (combinaison linéaire de u et v)
#
def t(u, v, k):
	return (u + k*v)



#
# premiers termes
#
u_0 = ex_t.expression("2").lire_valeur()
v_0 = ex_t.expression("-3").lire_valeur()



#
# calcul et impression des dix premiers termes de chaque suite
#
def calculs(k):
	u, v = u_0, v_0
	for n in range(10):
		print("u_" + str(n), "=", u)
		print("v_" + str(n), "=", v)

		d = t(u, v, k)
		print("k_" + str(n), "=", d)
		if n > 0:
			print("quotient =", d/m)
		m = d
		print()

		u, v = u_suivant(u, v), v_suivant(u, v)

#
# quelques calculs
#
print("-----")
k = ex_t.expression("k").lire_valeur()
calculs(k)

print("-----")
k = ex_t.expression("1/2").lire_valeur()
calculs(k)

print("-----")
k = ex_t.expression("3/2").lire_valeur()
calculs(k)

