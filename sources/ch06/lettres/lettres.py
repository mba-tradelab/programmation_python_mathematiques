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

from graphe import *

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

print("Chaînes(s) élémentaire(s) entre A et F:")
for c in g.recherche_chaines("A", "F"):
	print(c)
print()

print("Chaînes(s) élémentaires entre A et G:")
for c in g.recherche_chaines("A", "G"):
	print(c)
print()

