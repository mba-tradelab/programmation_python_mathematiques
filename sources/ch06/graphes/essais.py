#!/usr/bin/env python3
# -*- coding: utf8 -*-

########################################################################
# (C) Alexandre Casamayou-Boucau, Pascal Chauvin, Guillaume Connan     #
#                                                                      #
# Complément de l'ouvrage :                                            #
# Programmation en Python pour les mathématiques                       #
# Editeur : Dunod                   -        Collection : Sciences Sup #
# ISBN-13: 978-2100738311           -                  Licence : GPLv2 #
########################################################################

from graphe import *

def test1():
	print("----- test 1 -----")
	g = graphe(
		{
			'1': ['2', '3', '4'], 
			'2': ['1', '3'], 
			'3': ['1', '2', '4'], 
			'4': ['1', '3']
		}
	)

	for c in g.recherche_chaines('1', '3'):
		print(c)

	for c in g.recherche_chaines('1', '2'):
		print(c)



def test2():
	print("----- test 2 -----")
	g = graphe(
		{
			'A': ['B', 'D'], 
			'B': ['A', 'C', 'D', 'E', 'F'], 
			'C': ['B', 'F'], 
			'D': ['A', 'B', 'E'], 
			'E': ['B', 'D', 'F'], 
			'F': ['B', 'C', 'E'], 
			'G': ['H'], 
			'H': ['G']
		}
	)

	print(g)

	for k in g.sommets():
		print(k, ":", g.adjacents(k))

	for c in g.recherche_chaines('A', 'F'):
		print(c)

	print()

	for c in g.recherche_chaines('F', 'A'):
		print(c)

	for c in g.recherche_chaines('G', 'H'):
		print(c)



def test3():
	print("----- test 3 -----")
	g = graphe(
		{
			'*': ['+', '3'], 
			'+': ['5', ':', '*'], 
			':': ['6', '2', '+'], 
			'5': ['+'], 
			'6': [':'], 
			'2': [':'], 
			'3': ['*']
		}
	)

	print(g.composantes())

	print(g.composante_connexe('5'))

	for c in g.recherche_chaines('*', '3'):
		print(c)

	for c in g.recherche_chaines('*', '+'):
		print(c)

	for c in g.recherche_chaines('+', '*'):
		print(c)

	for c in g.recherche_chaines('*', '5'):
		print(c)

	for c in g.recherche_chaines('5', ':'):
		print(c)

	for c in g.recherche_chaines('6', '2'):
		print(c)

	for c in g.recherche_chaines('6', '3'):
		print(c)



def test4():
	print("----- test 4 -----")
	g = graphe(
		{
			"Angers": ["Nantes", "Paris", "Tours"], 
			"Nantes": ["Angers", "Tours"], 
			"Paris": ["Angers", "Tours"], 
			"Tours": ["Angers", "Nantes", "Paris"]
		}
	)

	for k in g.sommets():
		print(k, ":", g.adjacents(k))

	print(g.composante_connexe("Nantes"))
	
	if g.liaison("Nantes", "Angers"):
		print("autoroute")
	
	for c in g.recherche_chaines("Angers", "Paris"):
		print(c)

	for c in g.recherche_chaines("Angers", "Nantes"):
		print(c)



test1()
test2()
test3()
test4()
