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
		"Angers": ["Le Mans", "Nantes", "Tours"], 
		"Le Mans": ["Angers", "Tours"], 
		"Nantes": ["Angers"], 
		"Tours": ["Angers", "Le Mans"]
	}
)

print("Liaison(s) par autoroute entre Angers et Nantes:")
for c in g.recherche_chaines("Angers", "Nantes"):
	print(c)
print()

print("Liaison(s) par autoroute entre Angers et Tours:")
for c in g.recherche_chaines("Angers", "Tours"):
	print(c)
print()

print("Liaison(s) par autoroute entre Angers et Le Mans:")
for c in g.recherche_chaines("Angers", "Le Mans"):
	print(c)
print()

print("Liaison(s) par autoroute entre Le Mans et Nantes:")
for c in g.recherche_chaines("Le Mans", "Nantes"):
	print(c)

