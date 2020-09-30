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



def test5():
	print("----- test 5 -----")
	g = graphe(
		{
			'1': ['2', '3', '4'], 
			'2': ['1', '3'], 
			'3': ['1', '2', '4'], 
			'4': ['1', '3']
		}
	)
	print()

	for c in g.recherche_chaines('1', '3'):
		print(c)
	print()

	print(g.degre_sommet('1'))
	print()

	print(g.existence_chaine_eulerienne())
	print()

	for c in g.recherche_cycles('1'):
		print(c)
	print()

	for c in g.recherche_cycles('2'):
		print(c)
	print()

	print(g.nombre_aretes())
	print()



def test6():
	print("----- test 6 -----")
	g = graphe(
		{
			'A': ['B', 'C'], 
			'B': ['A', 'C'], 
			'C': ['A', 'B', 'D'], 
			'D': ['C', 'E'],
			'E': ['D', 'F'], 
			'F': ['E']
		}
	)

#	for c in g.recherche_chaines('C', 'F'):	# ne donne pas C-A-B-C-D-E-F 
#		print(c)							# ni C-B-A-C-D-E-F (car l'algorithme 
#	print()									# impose de ne pas repasser par 
											# le même sommet)

#	print(g.degre_sommet('F'))
#	print()

#	print(g.existence_chaine_eulerienne())
#	print()

#	for c in g.recherche_cycles('A'):
#		print(c)
#	print()

#	for c in g.recherche_cycles('C'):
#		print(c)
#	print()

#	print(g.nombre_aretes())
#	print()

#	for k in g.sommets():
#		print(k, ":", g.adjacents(k))
#	print()

#	h = g.graphe_reduit('A', 'B')
#	for k in h.sommets():
#		print(k, ":", h.adjacents(k))
#	print()

#	h = g.graphe_reduit('E', 'F')
#	for k in h.sommets():
#		print(k, ":", h.adjacents(k))
#	print()

#	print(g.est_un_pont('A', 'C'))
#	print()

#	print g.est_un_pont('C', 'D')
#	print

	h = g.graphe_reduit('A', 'C')
	for s in h.sommets():
		print(s, ":", h.adjacents(s))
	print()

	h = h.graphe_reduit('A', 'B')
	for s in h.sommets():
		print(s, ":", h.adjacents(s))
	print()

	h = h.graphe_reduit('B', 'C')
	for s in h.sommets():
		print(s, ":", h.adjacents(s))
	print()

	h = h.graphe_reduit('C', 'D')
	for s in h.sommets():
		print(s, ":", h.adjacents(s))
	print()

	h = h.graphe_reduit('D', 'E')
	for s in h.sommets():
		print( s, ":", h.adjacents(s))
	print()



def test7():
	print("----- test 7 -----")
	g = graphe(
		{
			'A': ['B', 'C'], 
			'B': ['A', 'C'], 
			'C': ['A', 'B', 'D'], 
			'D': ['C', 'E'],
			'E': ['D', 'F'], 
			'F': ['E']
		}
	)
	print(g.recherche_Euler())



def test8():
	print("----- test 8 -----")
	g = graphe(
		{
			'1': ['2', '3', '4'], 
			'2': ['1', '3'], 
			'3': ['1', '2', '4'], 
			'4': ['1', '3']
		}
	)
	print(g.recherche_Euler())



def test9():
	print("----- test 9 -----")
	g = graphe(
		{
			'1': ['2'], 
			'2': ['1']
		}
	)
	print(g.recherche_Euler())



def test10():
	print("----- test 10 -----")
	g = graphe(
		{
			'a': ['b', 'd', 'e', 'g'], 
			'b': ['a', 'c'], 
			'c': ['b', 'd'], 
			'd': ['a', 'c'], 
			'e': ['a', 'f'], 
			'f': ['e', 'g'], 
			'g': ['a', 'f']
		}
	)

	print(g.recherche_Euler())



def test11():
	print("----- test 11 -----")
	g = graphe(
		{
			'1': ['2', '3', '5', '6'], 
			'2': ['1', '3', '5', '6'], 
			'3': ['1', '2', '4'], 
			'4': ['3', '5', '6'], 
			'5': ['1', '2', '4', '6'], 
			'6': ['1', '2', '4', '5']
		}
	)

	print(g.recherche_Euler())



if __name__ == "__main__":
#	test1()
#	test2()
#	test3()
#	test4()
#	test5()
#	test6()
	test7()
	test8()
	test9()
	test10()
	test11()

