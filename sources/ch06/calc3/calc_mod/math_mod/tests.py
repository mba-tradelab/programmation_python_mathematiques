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
# fichier: prog_tests.py
# version: 0.5.0
#  auteur: Pascal CHAUVIN
#    date: 2014/10/28
#
# (tous les symboles non internationaux sont volontairement omis)
#

import sys
sys.path.append('./entier_mod')
sys.path.append('./rationnel_mod')
sys.path.append('./monome_mod')
sys.path.append('./polynome_mod')
sys.path.append('./fraction_mod')
sys.path.append('./utile_mod')

import entier_mod.entier_tests as te
import rationnel_mod.rationnel_tests as tr
import monome_mod.monome_tests as tm
import polynome_mod.polynome_tests as tp
import fraction_mod.fraction_tests as tf
import utile_mod.utile_tests as tu



def test_unitaire_0():
	print("*** prog: test_unitaire_0 ***")
	ok = te.tests_unitaires()
	return ok



def test_unitaire_1():
	print("*** prog: test_unitaire_1 ***")
	return tr.tests_unitaires()



def test_unitaire_2():
	print("*** prog: test_unitaire_2 ***")
	return tm.tests_unitaires()



def test_unitaire_3():
	print("*** prog: test_unitaire_3 ***")
	return tp.tests_unitaires()



def test_unitaire_4():
	print("*** prog: test_unitaire_4 ***")
	return tf.tests_unitaires()



def test_unitaire_5():
	print("*** prog: test_unitaire_5 ***")
	return tu.tests_unitaires()



def test_unitaire_6():
	print("*** prog: test_unitaire_6 ***")
	return True



def tests_unitaires():
	return (
		test_unitaire_0() and \
		test_unitaire_1() and \
		test_unitaire_2() and \
		test_unitaire_3() and \
		test_unitaire_4() and \
		test_unitaire_5() and \
		test_unitaire_6()
	)



if __name__ == "__main__":
	ok = tests_unitaires()
	if ok:
		print("*** tests: tests unitaires OK ***")
	
