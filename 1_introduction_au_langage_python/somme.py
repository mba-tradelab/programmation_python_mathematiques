#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

def somme(n):
    # fonction qui renvoie la somme des carrés des n premiers entiers
    s, i = 0, 0
    while i < n:
        i += 1
        s += i ** 2
    return s

def depasse(M):
    # pour tout entier M, renvoie le plus petit entier n tel que
    # 1**2 + 2**2 + ... + n**2 >= M
    s, i = 0, 0
    while s < M:
        i += 1
        s += i ** 2
    return i
