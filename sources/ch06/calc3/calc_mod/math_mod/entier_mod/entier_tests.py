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
# fichier: entier_tests.py
# version: 0.5.0
#  auteur: Pascal CHAUVIN
#    date: 2014/10/28
#
# (tous les symboles non internationaux sont volontairement omis)
#

import entier

def test_unitaire_0(visible =False):
	print("*** entier: test_unitaire_0 ***")
	
	a = entier.entier(5)
	if visible:
		print(a)
		print(repr(a))
	
	ok = True
	
	return ok



def test_unitaire_1(visible =False):
	print("*** entier: test_unitaire_1 ***")
	
	a = entier.entier(5, 0 == 1)
	
	ok = (not a.est_valide())
	
	return ok
	


def test_unitaire_2(visible =False):
	print("*** entier: test_unitaire_2 ***")
	
	a = entier.entier(5, 0 == 1)
	
	ok = (not a.est_valide())
	
	return ok



def test_unitaire_3(visible =False):
	print("*** entier: test_unitaire_3 ***")
	
	a = entier.entier(5)	
	b = entier.entier(6)
	x = a + b
	
	ok = (x.est_valide() and x.lire_valeur() == 11)
	
	return ok
	


def test_unitaire_4(visible =False):
	print("*** entier: test_unitaire_4 ***")
	
	a = entier.entier(5)	
	b = entier.entier(6, False)
	x = a + b
	
	ok = (x.est_valide() == False and x.lire_valeur() == 0)
	
	return ok
	



def test_unitaire_5(visible =False):
	print("*** entier: test_unitaire_5 ***")
	
	a = entier.entier(5)	
	b = entier.entier(6)
	x = a - b
	
	ok = (x.est_valide() and x.lire_valeur() == -1)
	
	return ok



def test_unitaire_6(visible =False):
	print("*** entier: test_unitaire_6 ***")
	
	a = entier.entier(5)
	x = -a
	y = a.oppose()
		
	ok = ((x.est_valide() and x.lire_valeur() == -5) and \
		(y.est_valide() and y.lire_valeur() == -5))
	
	return ok



def test_unitaire_7(visible =False):
	print("*** entier: test_unitaire_7 ***")
	
	a = entier.entier(5, False)
	x = -a
	
	ok = (x.est_valide() == False and x.lire_valeur() == 0)
	
	return ok



def test_unitaire_8(visible =False):
	print("*** entier: test_unitaire_8 ***")
	
	a = entier.entier(5)
	n = entier.entier(6)
	x = a ** n
	
	ok = (x.est_valide() and x.lire_valeur() == 15625)
	
	return ok



def test_unitaire_9(visible =False):
	print("*** entier: test_unitaire_9 ***")
	
	a = entier.entier(5)
	n = entier.entier(-6)
	x = a ** n
	
	ok = (not x.est_valide())
	
	return ok



def test_unitaire_10(visible =False):
	print("*** entier: test_unitaire_10 ***")
	
	a = entier.entier(0)
	n = entier.entier(6)
	x = a ** n
	
	ok = (x.est_valide() and x.lire_valeur() == 0)
	
	return ok



def test_unitaire_11(visible =False):
	print("*** entier: test_unitaire_11 ***")
	
	a = entier.entier(0)
	n = entier.entier(0)
	x = a ** n
	
	ok = (not x.est_valide())
	
	return ok



def test_unitaire_12(visible =False):
	print("*** entier: test_unitaire_12 ***")
	
	a = entier.entier(-1)
	n = entier.entier(-10)
	x = a ** n
	
	ok = (x.est_valide() and x.lire_valeur() == 1)
	
	return ok



def test_unitaire_13(visible =False):
	print("*** entier: test_unitaire_13 ***")
	
	a = entier.entier(-54)
	b = entier.entier(6)
	x = a / b
	
	ok = (x.est_valide() and x.lire_valeur() == -9)
	
	return ok



def test_unitaire_14(visible =False):
	print("*** entier: test_unitaire_14 ***")
	
	a = entier.entier(-55)
	b = entier.entier(6)
	x = a / b
	
	ok = (x.est_valide() == False)
	
	return ok



def test_unitaire_15(visible =False):
	print("*** entier: test_unitaire_15 ***")
	
	a = entier.entier(-55)
	b = entier.entier()
	x = a / b
	
	ok = (x.est_valide() == False)
	
	return ok



def test_unitaire_(visible =False):
	print("*** fraction: test_unitaire_ ***")
	
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
		test_unitaire_15()
	)



if __name__ == "__main__":
	ok = tests_unitaires()
	if ok:
		print("*** entier: tests unitaires OK ***")

