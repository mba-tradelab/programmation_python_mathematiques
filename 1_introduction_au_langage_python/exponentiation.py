#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

# Algorithme d'exponentiation rapide
# Etant donnés un réel positif a et un entier n, on remarque que :
# a^n =
#       (a^(n/2))^2 si n est pair,
#       a*(a^(n-1)/2)^2 si n est impair.
# Cet algorithme se programme naturellement par une fonction récursive

def expo(a, n):
    if n == 0: return 1
    else:
        if n%2 == 0: return expo(a, n//2)**2
        else: return a*(expo(a, (n-1)//2)**2)
