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
# fichier: erreur_tests.py
# version: 0.5.0
#  auteur: Pascal CHAUVIN
#    date: 2014/10/28
#
# (tous les symboles non internationaux sont volontairement omis)
#

import erreur

def test_unitaire_0(visible =False):
	print("*** erreur: test_unitaire_0 ***")
	
	e = erreur.ERREUR.NON_DOCUMENTEE
	if visible: print(e)

	ok = True	
	return ok



def test_unitaire_1(visible =False):
	print("*** erreur: test_unitaire_1 ***")
	
	ok = True	
	return ok
	


def test_unitaire_2(visible =False):
	print("*** erreur: test_unitaire_2 ***")
	
	ok = True	
	return ok



def test_unitaire_3(visible =False):
	print("*** erreur: test_unitaire_3 ***")
	
	ok = True	
	return ok
	


def test_unitaire_4(visible =False):
	print("*** erreur: test_unitaire_4 ***")
	
	ok = True	
	return ok
	



def test_unitaire_5(visible =False):
	print("*** erreur: test_unitaire_5 ***")
	
	ok = True	
	return ok



def test_unitaire_6(visible =False):
	print("*** erreur: test_unitaire_6 ***")
	
	ok = True	
	return ok



def test_unitaire_7(visible =False):
	print("*** erreur: test_unitaire_7 ***")
	
	ok = True	
	return ok



def test_unitaire_8(visible =False):
	print("*** erreur: test_unitaire_8 ***")
	
	ok = True	
	return ok



def test_unitaire_9(visible =False):
	print("*** erreur: test_unitaire_9 ***")
	
	ok = True	
	return ok



def test_unitaire_(visible =False):
	print("*** fraction: test_unitaire_ ***")
	
	ok = True
	return ok



def tests_unitaires():
	return (
		test_unitaire_0(True) and \
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
		print("*** erreur: tests unitaires OK ***")

