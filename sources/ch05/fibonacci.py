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

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        u, v  = 1, 1
        for k in range(2, n+1):
            u, v = v, u+v
        return v

def fibo(n):
    if n == 0 or n == 1:
        return(1)
    else:
        return(fibo(n - 1) + fibo(n - 2))

def fibo2(n):
    global compteur
    if (n == 0) or (n == 1) :
        return(1)
    else:
        compteur += 2
        return(fibo2(n-1)\
        + fibo2(n-2))

n = 20
compteur = 0
print("{}! = {}".format(n, fibo2(n)))
print("nombre d'appels recursifs : {}".format(compteur))

# version récursive terminale
def fibo(n, f_n_1 = 1, f_n = 0):  # (n, F_{n-1}, F_n)
    if (n == 0):  # cas de base
        return f_n
    else:         # récurrence
        return fibo(n - 1, f_n, f_n + f_n_1)

print(fibo(990))

# autre variante
def fibo2(n):
    """Renvoie F_{n-1}, F_n"""
    if (n == 0):  # cas de base
        return 1, 0  # F_{-1}, F_0
    else:         # récurrence
        f_k_1, f_k = fibo2(n//2)        # F_{k-1}, F_k   avec k = n/2
        f2_k = f_k**2                   # F_k^2
        if n%2 == 0:  # n pair
            return f2_k + f_k_1**2,    f_k*f_k_1*2 + f2_k       # F_{2k-1}, F_{2k}
        else:         # n impair
            return f_k*f_k_1*2 + f2_k, (f_k + f_k_1)**2 + f2_k  # F_{2k},   F_{2k+1}

def fibo(n):
    """Renvoie F_n"""
    return fibo2(n)[1]

print(fibo(990))
