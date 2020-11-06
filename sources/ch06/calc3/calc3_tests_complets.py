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
# fichier: calc3_tests.py
# version: 0.5.0
#  auteur: Pascal CHAUVIN
#    date: 2014/10/29
#
# (tous les symboles non internationaux sont volontairement omis)
#

import sys
sys.path.append('./calc_mod')
sys.path.append('./calc_mod/math_mod')
sys.path.append('./calc_mod/math_mod/entier_mod')
sys.path.append('./calc_mod/math_mod/rationnel_mod')
sys.path.append('./calc_mod/math_mod/monome_mod')
sys.path.append('./calc_mod/math_mod/monome_mod/joli_mod')
sys.path.append('./calc_mod/math_mod/polynome_mod')
sys.path.append('./calc_mod/math_mod/fraction_mod')
sys.path.append('./calc_mod/math_mod/utile_mod')
sys.path.append('./calc_mod/erreur_mod')
sys.path.append('./calc_mod/expression_mod')
sys.path.append('./calc_mod/calcul_mod')

import calc_mod.math_mod.entier_mod.entier_tests
import calc_mod.math_mod.rationnel_mod.rationnel_tests as ratio_t
import calc_mod.math_mod.monome_mod.monome_tests as mono_t
import calc_mod.math_mod.monome_mod.joli_mod.joli_tests as jo
import calc_mod.math_mod.polynome_mod.polynome_tests as poly_t
import calc_mod.math_mod.fraction_mod.fraction_tests as frac_t
import calc_mod.math_mod.utile_mod.utile_tests as util
import calc_mod.erreur_mod.erreur_tests as err_t
import calc_mod.expression_mod.expression_tests as ex_t
import calc_mod.calcul_mod.calcul_tests as calc_t

def test_unitaire_0(visible =False):
	print("\n--- entier: tests unitaires ---")
	return calc_mod.math_mod.entier_mod.entier_tests.tests_unitaires()



def test_unitaire_1(visible =False):
	print("\n--- rationnel: tests unitaires ---")
	return ratio_t.tests_unitaires()



def test_unitaire_2(visible =False):
	print("\n--- monome: tests unitaires ---")
	return mono_t.tests_unitaires()



def test_unitaire_3(visible =False):
	print("\n--- polynome: tests unitaires ---")
	return poly_t.tests_unitaires()



def test_unitaire_4(visible =False):
	print("\n--- fraction: tests unitaires ---")
	return frac_t.tests_unitaires()



def test_unitaire_5(visible =False):
	print("\n--- utile : tests unitaires ---")
	return util.tests_unitaires()



def test_unitaire_6(visible =False):
	print("\n--- erreur : tests unitaires ---")
	return err_t.tests_unitaires()



def test_unitaire_7(visible =False):
	print("\n--- expression : tests unitaires ---")
	return ex_t.tests_unitaires()



def test_unitaire_8(visible =False):
	print("\n--- calcul : tests unitaires ---")
	return calc_t.tests_unitaires()



def test_unitaire_9(visible =False):
	print("\n--- joli : tests unitaires ---")
	return jo.tests_unitaires()



def test_unitaire_(visible =False):
	print("\n--- : tests unitaires ---")
	return True



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
		print("\n--- calc3: tests unitaires complets OK ---")
	
