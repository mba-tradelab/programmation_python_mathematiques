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
# fichier: joli_tests.py
# version: 0.5.0
#  auteur: Pascal CHAUVIN
#    date: 2014/10/28
#
# (tous les symboles non internationaux sont volontairement omis)
#

import joli as jo

def test_unitaire0():
	print("\n*** test unitaire 0 ***")
	
	n = jo.joli('t')
	n.inserer('y')
	n.inserer('a')
	n.inserer('x')
	n.inserer('x')
	n.inserer('b')
	n.inserer('u')

	print("---")
	print(n.a_plat())
	
	print("---")
	print(n)
	
	print("---")
	print(repr(n))
	
	ok = (n.nombre_noeuds() == 6)
	return ok



def test_unitaire1():
	print("\n*** test unitaire 1 ***")
	
	s = "gnu is not unix"
	
	n = jo.joli(s[0])
	s = s[1:]
	for c in s:
		n.inserer(c)
	
	print(n.a_plat())
	
	ok = True
	return ok



def test_unitaire2():
	print("\n*** test unitaire 2 ***")
	
	print(jo.format_indet("ce matin un lapin"))

	ok = True
	return ok
	



def test_unitaire3():
	print("\n*** test unitaire 3 ***")
	
	ok = True
	return ok
	



def test_unitaire4():
	print("\n*** test unitaire 4 ***")
	
	ok = True
	return ok
	


def test_unitaire5():
	print("\n*** test unitaire 5 ***")

	ok = True
	return ok



def test_unitaire():
	print("\n*** test unitaire ***")
	
	ok = True
	return ok



def tests_unitaires():
	return (
		test_unitaire0() and \
		test_unitaire1() and \
		test_unitaire2() and \
		test_unitaire3() and \
		test_unitaire4() and \
		test_unitaire5()
	)



if __name__ == "__main__":
	print(tests_unitaires())

