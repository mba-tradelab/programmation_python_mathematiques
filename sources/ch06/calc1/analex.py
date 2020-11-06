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

from os import *
from re import *
from string import *

def analyse_lexicale(s):
	s = s.replace('[', '(')
	s = s.replace(']', ')')
	s = s.replace('{', '(')
	s = s.replace('}', ')')
	s = s.replace('/', ':')
	s = ''.join(s.split())
	s = '{' + s + '}'
	s = s.replace('-', '+-1*')
	s = s.replace('{+', '{')
	s = s.replace('(+', '(')

	separateurs = compile(r'([+\-*:^(){}])')
	jetons = separateurs.split(s)

	while jetons.count('') > 0:
		jetons.remove('')

	l = []
	for t in jetons:
		if len(t) >= 1:
			l.append(t)
		else:
			if t.isdigit():
				l.append(t)
			else:
				n = len(t)
				for i in range(n):
					if l[-1] in ascii_letters:
						l.append('*')
					l.append(t[i])

	r = []
	r.append(l[0])
	moins = False
	for t in l[1:]:
		if t == '-':
			moins = True
			continue
		if t == '1' and moins == True:
			moins = False
			t = "-1"
		r.append(t)
	
	return r[1:-1]

