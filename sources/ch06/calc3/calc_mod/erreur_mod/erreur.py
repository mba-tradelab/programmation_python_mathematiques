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
# fichier: erreur.py
# version: 0.5.0
#  auteur: Pascal CHAUVIN
#    date: 2014/10/28
#
# (tous les symboles non internationaux sont volontairement omis)
#

def constante(**constantes):
    return type('const', (), constantes)



ERREUR = constante(\
	AUCUNE_ERREUR = 0,\
	ACC_OUVRANTE_MANQUANTE = 1,\
	ACC_FERMANTE_MANQUANTE = 2,\
	SYNTAXE_NON_CONFORME = 3,\
	DIVISION_PAR_0 = 4,\
	EXPOSANT_INVALIDE = 5,\
	MANQUE_NOMBRE_OU_PER_OUVRANTE = 6,\
	MANQUE_PAR_FERMANTE = 7,\
	
	NON_DOCUMENTEE = 1000
)



if __name__ == "__main__":	
	pass

