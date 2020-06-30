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



%%cython -a

cimport cython

cdef float mod_exp(int a, int b, int m):
    cdef int bb, p
    cdef long aa
    aa = a
    bb = b
    p = 1
    while bb > 0:
        p = cython.cmod(p * (aa**(bb & 1 == 1)) , m)
        aa = cython.cmod(aa * aa,m)
        bb = bb >> 1
    return p

@cython.cdivision(True)
cdef float s1part(int n, int k, int j):
    cdef float nu, de
    nu = mod_exp(16, n - 1 - k, 8*k + j)
    de = (k * 8.0 + j)
    return nu / de

@cython.cdivision(True)
cdef float s2part(int n, int k, int j):
    cdef float de
    de = (((k << 3) + j) << ((k + 1 - n) << 2))
    return 1.0 / de

cdef float s1(int n):
    cdef float s
    cdef int k
    s = 0.0
    for k from 0 <= k < n:
        s = s + 4.0*s1part(n,k,1) - 2.0*s1part(n,k,4) - 1.0*s1part(n,k,5) - 1.0*s1part(n,k,6)
    return s

cdef float s2(int n):
    cdef float s
    cdef int k
    s = 0.0
    for k from n <= k < n + 5:
        s = s + 4.0*s2part(n,k,1) - 2.0*s2part(n,k,4) - 1.0*s2part(n,k,5) - 1.0*s2part(n,k,6)
    return s

cdef extern from "math.h":
    float floor(float r)

cdef float prem_hexa(float r):
        cdef float x
        x = r - floor(r)
        return floor(16*x)


def pi_plouffe(int n):
    cdef float s
    s = s1(n) + s2(n)
    return hex(int(prem_hexa(s)))[2:]
