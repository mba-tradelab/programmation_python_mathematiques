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
# fichier: appcos.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/11/27
#
# (tous les symboles non internationaux sont volontairement omis)
#

import cosinus

import math



def test_unitaire_0():
	print("*** cosinus: test_unitaire_0 ***")

	cosinus.test_cosinus(0.1)

	ok = True
	return ok



def test_unitaire_1():
	print("*** cosinus: test_unitaire_1 ***")

	cosinus.test_cosinus(10)
	cosinus.test_cosinus(200)
	cosinus.test_cosinus(-4)

	ok = True
	return ok



def test_unitaire_2():
	print("*** cosinus: test_unitaire_2 ***")

#	cosinus.test_cosinus(math.pi / 1000)
#	cosinus.test_cosinus(math.pi / 1000, 0.1)
#	cosinus.test_cosinus(math.pi / 1000, 0.01)
#	cosinus.test_cosinus(math.pi / 1000, 0.001)
#	cosinus.test_cosinus(math.pi / 1000, 0.0001)
#	cosinus.test_cosinus(math.pi / 1000, 0.0000001)
#	cosinus.test_cosinus(math.pi / 1000, 0.00000001)
#	cosinus.test_cosinus(math.pi / 1000, 0.000000001)

	for k in range(1, 10):
		cosinus.test_cosinus(math.pi / 1000, (1/(10**k)))

	ok = True
	return ok



def test_unitaire_():
	print("*** cosinus: test_unitaire_ ***")

	ok = True
	return ok



def tests_unitaires():
	return (
		test_unitaire_0() and \
		test_unitaire_1() and \
		test_unitaire_2()
	)



if __name__ == "__main__":
	ok = tests_unitaires()
	if ok:
		print("*** cosinus: tests unitaires OK ***")

