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
# fichier: calc3.py
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

import calc_mod.calcul_mod.calcul as calc

if __name__ == "__main__":
	c = calc.calcul()
	c.executer()

