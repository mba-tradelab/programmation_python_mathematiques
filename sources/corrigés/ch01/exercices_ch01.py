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


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("\n *** Palindrome *** \n")
# version itérative
def palindrome(chaine):
    i, n = 0, len(chaine) - 1
    while i < n and chaine[i] == chaine[n]:
        i += 1
        n -= 1
    return n <= i

print(palindrome('ressasser'), palindrome('ressassir'), palindrome('serres'))

# version récursive
def palindrome(chaine):
    if len(chaine) <= 1:
        return True
    if chaine[0] != chaine[-1]:
        return False
    else:
        return palindrome(chaine[1:-1])

print(palindrome('ressasser'), palindrome('ressassir'), palindrome('serres'))

# variante
def palindrome(chaine):
    return chaine == chaine[::-1]

print(palindrome('ressasser'), palindrome('ressassir'), palindrome('serres'))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("\n *** Constante de champernowne *** \n")
def champernowne(n):
    x = '0.'
    k = 0
    while len(x) <= n+2:
        k += 1
        x += str(k)
    return x[0:n+2]

print(champernowne(75))

# variante avec join
def champernowne(n):
    return '0.' + ''.join(str(i) for i in range(1, n))[:n]

print(champernowne(75))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("\n *** Approximation du cosinus *** \n")
def cosinus(x, epsilon):
    p = 0
    somme = 1
    terme = 1
    reste = abs(x)
    while reste > epsilon:
        p += 2
        terme *= - x**2 / (p * (p - 1))
        somme += terme
        reste *= abs(x)**2 / (p * (p + 1))
    return somme

import math

print(cosinus(1, 1e-5))
print(cosinus(1, 1e-14))
print(math.cos(1))

print(cosinus(math.pi/3, 1e-5))
print(cosinus(math.pi/3, 1e-14))
print(math.cos(math.pi/3))

print(cosinus(math.pi/4, 1e-5))
print(cosinus(math.pi/4, 1e-14))
print(math.sqrt(2)/2)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("\n *** Utilisation de la méthode join *** \n")
for n in range(2, 20):
   print(' + '.join('{:2}^2'.format(i) for i in range(1, n))
           + ' = {}'.format(sum(i**2 for i in range(1, n))))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("\n *** Triplets pythagoriciens *** \n")
def pythagoriciens(n):
    return [(x, y, z) for x in range(1, n) for y in range(x, n)
            for z in range(y, n) if x**2 + y**2 == z**2]

print(pythagoriciens(100))
print("Au total, on trouve {} triplets.".format(len(pythagoriciens(100))))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("\n *** Nombres parfaits *** \n")
def parfait(n):
    return sum([d for d in range(1, n) if n % d == 0]) == n

def liste_parfaits(n):
    return [i for i in range(2, n) if parfait(i)]

print(liste_parfaits(1000))

def somme(n):
    diviseurs = [d for d in range(1, n) if n % d == 0]
    if sum(diviseurs) == n:
        print('{} = '.format(n) + ' + '.join(str(d) for d in diviseurs))

for i in liste_parfaits(1000):
    somme(i)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("\n *** Crible d'Erathostène *** \n")
def crible(prems):
    if prems == []:
        return []
    return [prems[0]] + crible([p for p in prems[1:] if p % prems[0] != 0])

print(crible(range(2, 100)))


