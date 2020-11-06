#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

# Calcul de la factorielle d'un entier n :
# n! =
#       1 si n = 0
#       (n-1)! * n si n >= 1

def factorielle_iter(n):
    p = 1
    for i in range(2, n+1):
        p *= i
    return p

def factorielle_rec(n):
    if n == 0: return 1
    else: return (n * factorielle_rec(n-1))
