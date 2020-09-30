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
# fichier: test_arbre.py
# version: 0.0.1
#  auteur: Pascal CHAUVIN
#    date: 2014/12/22
#
# (tous les symboles non internationaux sont volontairement omis)
#

import random

import arbre_AVL as avl

def test_unitaire_0(visible =False):
	print("*** arbre: test_unitaire_0 ***")
	
	nombre_noeuds = random.randrange(5, 20)

	noeuds = [random.randrange(1, 10)]

	for i in range(nombre_noeuds):
		noeuds.append(noeuds[-1] + random.randrange(1, 10))

	i = random.randrange(nombre_noeuds)
	t = noeuds[i]
	del noeuds[i]

	a = avl.arbre(t)
	for n in range(len(noeuds)):
		a.inserer(noeuds[n])

	if visible: a.afficher()
	
	ok = True
	return ok
	
	
	
def test_unitaire_1(visible =False):
	print("*** arbre: test_unitaire_1 ***")
		
	nombre_noeuds = random.randrange(5, 20)

	noeuds = [random.randrange(1, 10)]

	for i in range(nombre_noeuds):
		noeuds.append(noeuds[-1] + random.randrange(1, 10))

	if visible: print(noeuds)

	#
	# on prend une copie (profonde) de a
	#
	copie = list(noeuds)

	i = random.randrange(nombre_noeuds)
	t = noeuds[i]
	del noeuds[i]

	a = avl.arbre(t)
	for n in range(len(noeuds)):
		a.inserer(noeuds[n])

	if visible: a.afficher()

	if visible: print("-----")

	#
	# on prend la copie de a et on y met un peu d'entropie.
	#
	if visible: print(copie)

	k = random.randrange(1, 10)
	for i in range(1, k):
		t = copie[0]
		copie.append(t)
		del copie[0]

	if visible: print(copie)

	i = random.randrange(nombre_noeuds)
	t = copie[i]
	del copie[i]

	b = avl.arbre(t)
	for n in range(len(copie)):
		b.inserer(copie[n])

	if visible: b.afficher()

	ok = True
	return ok
	
	
	
def test_unitaire_2(visible =False):
	print("*** arbre: test_unitaire_2 ***")
	
	ok = True
	return ok



def test_unitaire_(visible =False):
	print("*** arbre: test_unitaire_ ***")
	
	ok = True
	return ok



def tests_unitaires():
	return (
		test_unitaire_0(True) and \
		test_unitaire_1(True) and \
		test_unitaire_2()
	)
	
	
	
if __name__ == "__main__":
	ok = tests_unitaires()
	if ok:
		print("*** arbre: tests unitaires OK ***")

