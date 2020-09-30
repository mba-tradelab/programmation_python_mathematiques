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
# fichier: calcul_tests.py
# version: 0.5.0
#  auteur: Pascal CHAUVIN
#    date: 2014/10/28
#
# (tous les symboles non internationaux sont volontairement omis)
#

import calcul as calc

def test_unitaire_0(visible =False):
	print("*** calcul: test_unitaire_0 ***")
	
	c = calc.calcul()
	c.executer()
	if visible: print(c)
	
	ok = c.est_valide()
	return ok
	
	
	
def test_unitaire_1(visible =False):
	print("*** calcul: test_unitaire_1 ***")
		
	ok = True
	return ok
	
	
	
def test_unitaire_2(visible =False):
	print("*** calcul: test_unitaire_2 ***")
	
	ok = True
	return ok



def test_unitaire_3(visible =False):
	print("*** calcul: test_unitaire_3 ***")
	
	ok = True
	return ok



def test_unitaire_4(visible =False):
	print("*** calcul: test_unitaire_4 ***")
	
	ok = True
	return ok



def test_unitaire_5(visible =False):
	print("*** calcul: test_unitaire_5 ***")
	
	ok = True
	return ok



def test_unitaire_6(visible =False):
	print("*** calcul: test_unitaire_6 ***")
	
	ok = True
	return ok



def test_unitaire_7(visible =False):
	print("*** calcul: test_unitaire_7 ***")
	
	ok = True
	return ok



def test_unitaire_8(visible =False):
	print("*** calcul: test_unitaire_8 ***")
	
	ok = True
	return ok



def test_unitaire_9(visible =False):
	print("*** calcul: test_unitaire_9 ***")
	
	ok = True
	return ok



def test_unitaire_10(visible =False):
	print("*** calcul: test_unitaire_10 ***")
		
	ok = True
	return ok
	
	
	
def test_unitaire_11(visible =False):
	print("*** calcul: test_unitaire_11 ***")
		
	ok = True
	return ok
	
	
	
def test_unitaire_12(visible =False):
	print("*** calcul: test_unitaire_12 ***")
	
	ok = True
	return ok



def test_unitaire_13(visible =False):
	print("*** calcul: test_unitaire_13 ***")
	
	ok = True
	return ok



def test_unitaire_14(visible =False):
	print("*** calcul: test_unitaire_14 ***")
	
	ok = True
	return ok



def test_unitaire_15(visible =False):
	print("*** calcul: test_unitaire_15 ***")
	
	ok = True
	return ok



def test_unitaire_16(visible =False):
	print("*** calcul: test_unitaire_16 ***")
	
	ok = True
	return ok



def test_unitaire_17(visible =False):
	print("*** calcul: test_unitaire_17 ***")
	
	ok = True
	return ok



def test_unitaire_18(visible =False):
	print("*** calcul: test_unitaire_18 ***")
	
	ok = True
	return ok



def test_unitaire_19(visible =False):
	print("*** calcul: test_unitaire_19 ***")
	
	ok = True
	return ok



def test_unitaire_(visible =False):
	print("*** calcul: test_unitaire_ ***")
	
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
		test_unitaire_9() and \
		test_unitaire_10() and \
		test_unitaire_11() and \
		test_unitaire_12() and \
		test_unitaire_13() and \
		test_unitaire_14() and \
		test_unitaire_15() and \
		test_unitaire_16() and \
		test_unitaire_17() and \
		test_unitaire_18() and \
		test_unitaire_19()
	)
	
	
	
if __name__ == "__main__":
	ok = tests_unitaires()
	if ok:
		print("*** calcul: tests unitaires OK ***")

