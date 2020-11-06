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
# fichier: fraccont3_tests.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/12/06
#
# (tous les symboles non internationaux sont volontairement omis)
#

import sys
sys.path.append('./fraccont2')

import fraccont2.fraccont2 as fc2

import fraccont3



def test_unitaire_0():
	print("*** fraccont3: test_unitaire_0 ***")
	
	c = fraccont3.calcul(61)
	print(c)
	
	ok = True
	return ok
	
	
	
def test_unitaire_1():
	print("*** fraccont3: test_unitaire_1 ***")

	for n in range(2, 300):
		print("* approximation de {0}^(1/2):".format(n))
	
		c = fraccont3.calcul(n)
		print("{0} = {1}\n".format(c ,fc2.calcul_reduite(c)))
	
	ok = True
	return ok
	
	
	
def test_unitaire_2():
	print("*** fraccont3: test_unitaire_2 ***")
	
	ok = True
	return ok



def test_unitaire_3():
	print("*** fraccont3: test_unitaire_3 ***")
	
	ok = True
	return ok



def test_unitaire_4():
	print("*** fraccont3: test_unitaire_4 ***")
	
	ok = True
	return ok



def test_unitaire_5():
	print("*** fraccont3: test_unitaire_5 ***")
	
	ok = True
	return ok



def test_unitaire_6():
	print("*** fraccont3: test_unitaire_6 ***")
	
	ok = True
	return ok



def test_unitaire_7():
	print("*** fraccont3: test_unitaire_7 ***")
	
	ok = True
	return ok



def test_unitaire_8():
	print("*** fraccont3: test_unitaire_8 ***")
	
	ok = True
	return ok



def test_unitaire_9():
	print("*** fraccont3: test_unitaire_9 ***")
	
	ok = True
	return ok



def test_unitaire_():
	print("*** fraccont3: test_unitaire_ ***")
	
	ok = True
	return ok



def tests_unitaires():
	return (
		test_unitaire_0() and \
		test_unitaire_1() and \
		test_unitaire_2() and \
		test_unitaire_3() and \
		test_unitaire_4() and \
		test_unitaire_5() and \
		test_unitaire_6() and \
		test_unitaire_7() and \
		test_unitaire_8() and \
		test_unitaire_9()
	)
	
	
	
if __name__ == "__main__":
	ok = tests_unitaires()
	if ok:
		print("*** fraccont3: tests unitaires OK ***")

