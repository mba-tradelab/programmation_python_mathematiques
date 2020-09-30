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


from random import randrange, random

##########################
## 1) Tri par sélection ##
##########################

#   a)
def maxi(l, n):
	indice = 0
	maximum = l[0]
	for i in range(n):
		if l[i] > maximum:
			maximum, indice = l[i], i
	return([maximum, indice])

# b)
def tri_selec(l):
	i = len(l) - 1
	while i > 0:
		j = maxi(l, i + 1)[1]
		if j != i:
			l[j], l[i] = l[i], l[j]
		i -= 1
	return(l)

##########################
# 2) Tri par insertion ###
##########################

# a)
def insertion(l, n):
	while l[n] < l[n - 1] and n > 0:
		l[n - 1], l[n] = l[n], l[n - 1]
		n -= 1
	return(l)

# b)
def tri_insert(l):
	n = len(l)
	for i in range(1, n):
		l = insertion(l, i)
	return(l)


##########################
#### 3) Tri rapide #######
##########################

def tri_rapide(l):
    if l == []:
        return []
    return (tri_rapide([x for x in l[1:] if x < l[0]])
            + [l[0]] + tri_rapide([x for x in l[1:] if x >= l[0]]))


##########################
#### benchmark ###########
##########################
import time

def benchmark(instruction, formater, fresultat=None):
    """Calcule le temps d'exécution d'une instruction."""
    if fresultat == None:
        t = time.clock()
        exec(instruction)
        t = time.clock() - t
        s = "{" + formater + "} ---> {:.2f} s."
        print(s.format(instruction, t))
    else:
        t = time.clock()
        res = eval(instruction)
        t = time.clock() - t
        s = "{" + formater + "} = {" + fresultat + "} ---> {:.2f} s."
        print(s.format(instruction, res, t))

##########################
#### les tests ###########
##########################
n = 20
liste = [randrange(100) for i in range(n)]

s = (['{}(l)'.format(n) for n in
        ['tri_selec', 'tri_insert', 'tri_rapide']])

for instruction in s:
    l = liste[:]
    benchmark(instruction, ':>20', '')


####################
import sys
sys.setrecursionlimit(100000)

n = 10**3
s = (['{}(l)'.format(n) for n in ['tri_selec', 'tri_insert', 'tri_rapide']])

print('random')
liste = [random() for i in range(n)]

for instruction in s:
    l = liste[:]
    benchmark(instruction, ':>20')

print('sorted')
liste = list(range(n))

for instruction in s:
    l = liste[:]
    benchmark(instruction, ':>20')

print('reversed')
liste = list(reversed(range(n)))

for instruction in s:
    l = liste[:]
    benchmark(instruction, ':>20')

####################
print('n=10**4')
n = 10**4
liste = [random() for i in range(n)]

s = (['{}(l)'.format(n) for n in ['tri_selec', 'tri_insert', 'tri_rapide']])

for instruction in s:
    l = liste[:]
    benchmark(instruction, ':>20')


