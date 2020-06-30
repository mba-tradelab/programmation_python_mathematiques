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
# fichier: utile_tests.py
# version: 0.5.0
#  auteur: Pascal CHAUVIN
#    date: 2014/10/28
#
# (tous les symboles non internationaux sont volontairement omis)
#

import utile

def test_unitaire_0(visible =False):
	print("*** utile: test_unitaire_0 ***")
	
	s = utile.en_ordre_alphabetique("GNU is not Unix")
	if visible: print(s)
	
	ok = not utile.contient_erreur(s)
	return ok
	
	
	
def test_unitaire_1(visible =False):
	print("*** utile: test_unitaire_1 ***")
		
	s = utile.en_ordre_alphabetique("GNU is not Unix!")
	if visible: print(s)
	
	ok = utile.contient_erreur(s)
	return ok
	
	
	
def test_unitaire_2(visible =False):
	print("*** utile: test_unitaire_2 ***")
	
	s = utile.en_ordre_alphabetique("lapin ? malin???")
	if visible: print(s)
	
	ok = not utile.contient_erreur(s)
	return ok



def test_unitaire_3(visible =False):
	print("*** utile: test_unitaire_3 ***")
	
	s = utile.en_ordre_alphabetique("malin???")
	if visible: print(utile.reduction(s))
	
	s = utile.en_ordre_alphabetique("???malin")
	if visible: print(utile.reduction(s))
	
	ok = True
	return ok



def test_unitaire_4(visible =False):
	print("*** utile: test_unitaire_4 ***")
	
	ok = True
	return ok



def test_unitaire_5(visible =False):
	print("*** utile: test_unitaire_5 ***")
	
	ok = True
	return ok



def test_unitaire_6(visible =False):
	print("*** utile: test_unitaire_6 ***")
	
	ok = True
	return ok



def test_unitaire_7(visible =False):
	print("*** utile: test_unitaire_7 ***")
	
	ok = True
	return ok



def test_unitaire_8(visible =False):
	print("*** utile: test_unitaire_8 ***")
	
	ok = True
	return ok



def test_unitaire_9(visible =False):
	print("*** utile: test_unitaire_9 ***")
	
	ok = True
	return ok



def test_unitaire_(visible =False):
	print("*** utile: test_unitaire_ ***")
	
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
		print("*** utile: tests unitaires OK ***")

