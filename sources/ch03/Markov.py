#!/usr/bin/python3
#-*- coding: utf-8 -*-

########################################################################
# (C) Alexandre Casamayou-Boucau, Pascal Chauvin, Guillaume Connan     #
#                                                                      #
# Complément de l'ouvrage :                                            #
# Programmation en Python pour les mathématiques                       #
# Editeur : Dunod                   -        Collection : Sciences Sup #
# ISBN-13: 978-2100738311           -                  Licence : GPLv2 #
########################################################################


from codecs import open
from urllib.request import urlretrieve
from random import choice
from itertools import chain


class Markov(object):

    def __init__(self,fichier):
        self.dicAssoc = {}
        self.fichier = fichier
        self.lettres = self.fichierVersLettres()
        self.baseDeTuplets()
        fichier.close()

    # def fichierVersLettres(self):
    #     """
    #     Renvoie les lettres du texte sous forme d'une liste
    #     """
    #     data = self.fichier.read() # le fichier entier de type string
    #     lettres = map(lambda lettre: ','.join(lettre),data) # on sépare chaque caractère du texte par une virgule
    #     return list(chain.from_iterable(lettres)) # on en fait une liste

    def fichierVersLettres(self):
        data = self.fichier.read()
        return data.split()

    def tuplets(self):
        """
        Crée un générateur de triplets de lettres successives

        """
        for i in range(len(self.lettres) - 2):
            yield (self.lettres[i], self.lettres[i+1], self.lettres[i+2])

    def baseDeTuplets(self):
        """
        Crée un dictionnaire dont les clés sont des couples de lettres successives et la valeur la liste des successeurs observés.

        """
        for l1,l2,l3 in self.tuplets():
            key = l1,l2
            if key in self.dicAssoc:
                self.dicAssoc[key].append(l3)
            else:
                self.dicAssoc[key] = [l3]

    def genereMarkovText(self, nbLettres = 100):
        """
        Génère un texte selon la distribution du dictionnaire d'association
        """
        (l1,l2) = choice(list(self.dicAssoc.keys())) # on choisit un couple de lettres au hasard dans le dico
        gen_lettres = "" # on initialise le texte généré
        for i in range(nbLettres):
            gen_lettres += ' ' + l1 # + l1 # on écrit l1 dans letexte
            l1,l2 = l2,choice(self.dicAssoc[(l1,l2)]) # on avance d'un cran
        print(gen_lettres)
