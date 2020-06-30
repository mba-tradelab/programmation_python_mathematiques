#!/usr/bin/python3
#-*- coding: Utf-8 -*-

########################################################################
# (C) Alexandre Casamayou-Boucau, Pascal Chauvin, Guillaume Connan     #
#                                                                      #
# Complément de l'ouvrage :                                            #
# Programmation en Python pour les mathématiques                       #
# Editeur : Dunod                   -        Collection : Sciences Sup #
# ISBN-13: 978-2100738311           -                  Licence : GPLv2 #
########################################################################


import time

def benchmark(instruction, formater, fresultat=None):
    """Calcule le temps d'éxécution d'une instruction."""
    if fresultat == None:
        t = time.clock()
        exec(instruction)
        t = time.clock() - t
        s = "{" + formater + "} ---> {} s."
        print(s.format(instruction, t))
    else:
        t = time.clock()
        res = eval(instruction)
        t = time.clock() - t
        s = "{" + formater + "} = {" + fresultat + "} ---> {} s."
        print(s.format(instruction, res, t))


if __name__ == '__main__':

    from math import sin

    def evaluation(p, x):
        """Évalue le polynôme p en x."""
        return sum(c * x**i for i, c in enumerate(p))

    def horner(p, x):
        """Évalue le polynôme p en x par la méthode de Hörner."""
        somme, i = p[-1], len(p) - 2
        while i >= 0:
            somme = p[i] + x*somme
            i -= 1
        return somme

    n = 10**7
    polynome = [sin(i) for i in range(n)]
    s = ['{}(polynome, -1)'.format(n) for n in ['evaluation', 'horner']]

    # Exemple sans affichage du résultat de l'instruction
    for instruction in s:
        benchmark(instruction, ':>30')

    # Exemple avec affichage du résultat de l'instruction
    for instruction in s:
        benchmark(instruction, ':>30', ':.15f')


