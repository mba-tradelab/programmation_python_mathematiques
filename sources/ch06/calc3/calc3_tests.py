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

def test_unitaire_0(test =True, visible =False):
	if test:
		print("\n--- entier: tests unitaires ---")
		return calc_mod.math_mod.entier_mod.entier_tests.tests_unitaires()
	else:
		return True



def test_unitaire_1(test =True, visible =False):
	if test:
		print("\n--- rationnel: tests unitaires ---")
		return ratio_t.tests_unitaires()
	else:
		return True



def test_unitaire_2(test =True, visible =False):
	if test:
		print("\n--- monome: tests unitaires ---")
		return mono_t.tests_unitaires()
	else:
		return True



def test_unitaire_3(test =True, visible =False):
	if test:
		print("\n--- polynome: tests unitaires ---")
		return poly_t.tests_unitaires()
	else:
		return True



def test_unitaire_4(test =True, visible =False):
	if test:
		print("\n--- fraction: tests unitaires ---")
		return frac_t.tests_unitaires()
	else:
		return True



def test_unitaire_5(test =True, visible =False):
	if test:
		print("\n--- utile : tests unitaires ---")
		return util.tests_unitaires()
	else:
		return True



def test_unitaire_6(test =True, visible =False):
	if test:
		print("\n--- erreur : tests unitaires ---")
		return err_t.tests_unitaires()
	else:
		return True



def test_unitaire_7(test =True, visible =False):
	if test:
		print("\n--- expression : tests unitaires ---")
		return ex_t.tests_unitaires()
	else:
		return True



def test_unitaire_8(test =True, visible =False):
	if test:
		print("\n--- calcul : tests unitaires ---")
		return calc_t.tests_unitaires()
	else:
		return True



def test_unitaire_9(test =True, visible =False):
	if test:
		print("\n--- joli : tests unitaires ---")
		return jo.tests_unitaires()
	else:
		return True



def test_unitaire_10(test =True, visible =False):
	if test:
		print("\n--- : tests unitaires ---")
		return True
	else:
		return True



def tests_unitaires():
	""" - """
	
	""" tests du module 'entier' """
	ok = test_unitaire_0(False) 
	
	""" tests du module 'rationnel' """
	ok = ok and test_unitaire_1(False)
	
	""" tests du module 'monome' """
	ok = ok and test_unitaire_2(False)
	
	""" tests du module 'polynome' """
	ok = ok and test_unitaire_3(False) 
	
	""" tests du module 'fraction' """
	ok = ok and test_unitaire_4() 
	
	""" tests du module 'utile' """
	ok = ok and test_unitaire_5(False) 
	
	""" tests du module 'erreur' """
	ok = ok and test_unitaire_6(False) 
	
	""" tests du module 'expression' """
	ok = ok and test_unitaire_7(False) 
	
	""" tests du module 'calc' """
	ok = ok and test_unitaire_8() 
	
	""" tests du module 'joli' """
	ok = ok and test_unitaire_9(False) 
	
	""" tests du module '?' """
	ok = ok and test_unitaire_10(False) 

	return ok



if __name__ == "__main__":
	ok = tests_unitaires()
	if ok:
		print("\n--- calc3: tests unitaires OK ---")
	
