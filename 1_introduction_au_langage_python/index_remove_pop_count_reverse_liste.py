#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

def index(liste, x):
    for i in range(len(liste)):
        if liste[i] == x:
            return i
    return -1

def remove(liste, x):
    i = index(liste, x)
    if i >= 0:
        del liste[i]

def pop(liste, i):
    x = liste[i]
    del liste[i]
    return x

def count(liste, x):
    c = 0
    for e in liste:
        if e == x:
            c += 1
    return c

def reverse(liste):
    L = liste[:]
    for i in range(len(liste)):
        liste[i] = L[len(liste)-1-i]
