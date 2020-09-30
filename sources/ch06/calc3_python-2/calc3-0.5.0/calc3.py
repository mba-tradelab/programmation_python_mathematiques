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
#    date: 2014/08/10
#
# (tous les symboles non internationaux sont volontairement omis)
#

from expression import *

class calc3(object):
	""" une classe qui represente le calculateur calc3 """

	def __init__(self):
		""" constructeur """
#		self.__fichier = open("calculs.txt", "wt")
		self.__compteur = 1

	def exemples(self):
		""" tests automatiques """
		print("*** quelques exemples ***\n")

		e = expression("(3 + 4) * 5 ^ (1 + 1) - 7")
		print("exemple de calcul :", e.get_source())
		print(e, '\n') # donne 168

		e = expression("2 ^ 3 ^ 2 ^ 2")
		print("exemple de calcul :", e.get_source())
		print(e, '\n') # donne 2417851639229258349412352
	
		e = expression("-(5 - 1) : 5^3 + ( 9 + 1 ) * ( 7 + 2 * 5 )")
		print("exemple de calcul :", e.get_source())
		print(e, '\n') # donne 169.968

		e = expression("3/7 - 2/7 : ( 5 : 14 )")
		print("exemple de calcul :", e.get_source())
		print(e, '\n') # donne -13/35

		e = expression("((a + b)/2)^2 - ((a - b)/2)^2")
		print("exemple de calcul :", e.get_source())
		print(e, '\n') # donne a*b

		e = expression("(x+2/3)^(-3)")
		print("exemple de calcul :", e.get_source())
		print(e, '\n') # donne 27/(27*x^3 + 54*x^2 + 36*x + 8)

		e = expression("(8*(16/10)*10^8)/((4/10)*10^10)")
		print("exemple de calcul :", e.get_source())
		print(e, '\n') # donne 0.32

	def notice(self):
		""" notice """
		print()
		print("*** calc3: programme de calcul formel (corps de fractions) ***")
		print()
		print("                \"Python pour le lyc\\'{e}e et la pr\\'{e}pa\"")
		print("                                Alexandre CASAMAYOU-BOUCAU")
		print("                                            Pascal CHAUVIN")
		print("                                          Guillaume CONNAN")
		print()
		print("    (version 0.5.0)")
		print()

	def remarque(self):
		""" remarque """
		print("*** remarque importante ***")
		print()
		print("    Les calculs sont enregistres dans un fichier (en format texte pur)")
		print("    nomme \"calculs.txt\" dans le repertoire courant d'execution du pro-")
		print("    gramme. Il est donc indispensable d'executer le programme \"calc3\"")
		print("    depuis un repertoire ou l'utilisateur possede le droit d'ecriture.")
		print()

	def lecture(self):
		""" saisie d'une expression """
		invite = "calc3:" + str(self.__compteur) + "> "
		s = str(input(invite))
		print(invite + s + "\n", file=self.__fichier)
		if len(s) > 0:
			self.__compteur += 1
		return s

	def boucle(self):
		""" boucle d'evaluation """
		print("*** boucle interactive ***")
		print()
		print("    Entrer une expression mathematique a evaluer (ou laisser vide pour")
		print("    finir) puis valider.")
		print()
		entree = self.lecture()
		while len(entree) > 0:
			e = expression(entree)
			print(e)
			print(str(e) + "\n\n", file=self.__fichier)
			print()
			entree = self.lecture()
		print()
		self.__fichier.close()

	def executer(self):
		""" execution du programme """
		self.notice()
		self.exemples()
		self.remarque()
		self.boucle()

if __name__ == "__main__":
	c = calc3()
	c.executer()

