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
# fichier: utile.py
# version: 0.5.0
#  auteur: Pascal CHAUVIN
#    date: 2014/10/28
#
# (tous les symboles non internationaux sont volontairement omis)
#

import string

JOKER = "?" # pour le monome de degre nul

def en_ordre_alphabetique(s):
	""" - """
	t = "".join(s.split())
	t = "".join(sorted(list(t.lower()), key=str.lower))
	return t
	
	
	
def contient_erreur(s):
	""" - """
	erreurs = 0
	for car in s:
		erreurs += not (car in string.ascii_letters or car == JOKER)		
	return (erreurs > 0)
			


def reduction(s):
	""" - """
	t = ""
	for car in s:
		if car != JOKER: t += car # '?'
					
	if len(t) == 0:
		return JOKER
	else:
		return t
			


def correction_math(s):
	""" quelques ajustements syntaxiques """
	t = ""
	for x in s:
		if (x in string.digits) or (x in string.ascii_letters):
			t += x
		if x in "{[": x = "("
		if x in "}]": x = ")"
		
		if x in "+-*^:/()":
			t += x
	return t
	


if __name__ == "__main__":
	pass
