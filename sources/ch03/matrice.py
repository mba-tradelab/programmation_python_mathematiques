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

#from functools import reduce
from operator  import mul, floordiv, truediv,add
from numpy.random    import randint, random
from math      import log,ceil
from fractions import Fraction
import numpy as np
from scipy import misc, linalg
from matplotlib import cm
from pylab import imshow
from sympy import randMatrix
from math import floor, sqrt
import matplotlib.pyplot as plt

from subprocess import call

import os


class Mat:
    """ une matrice sous la forme Mat([nb lignes, nb cols], fonction(i,j))"""

    def __init__(self, dim, f):
        self.F = f   # fonction (i,j) -> coeff en position i,j
        self.D = dim # liste [nb de lignes, nb de cols]

    def ligne(self,i):
        for j in range(self.D[1]):
            yield self.F(i,j)

    def col(self,j):
        for i in range(self.D[0]):
            yield self.F(i,j)

    def indices(self):
        [r,c] = self.D
        for i in range(r):
            for j in range(c):
                yield (i,j)

    def __getitem__(self,cle):
        """ permet d'obtenir Mij avec M[i,j]"""
        return self.F(*cle)

    def __iter__(self):
        """ pour itérer sur la liste des coefficients """
        [r,c] = self.D
        for j in range(c):
            for i in range(r):
                yield self.F(i,j)

    def __str__(self):
        """ joli affichage d'une matrice"""
        [r,c],f = self.D, self.F
        lmax = len(str(max(iter(self)))) + 1
        s = '\n'.join( (' '.join('{0:{l}G}'.format(f(i,j),l=lmax) if isinstance(f(i,j), int) or isinstance(f(i,j), float) else str(f(i,j)) for j in range(c))) for i in range(r))
        return s

    def __repr__(self):
        """ représentation dans le REPL"""
        return str(self)

    def __neg__(self):
        """ opposé d'une matrice : utilisation du symbole -"""
        return Mat(self.D,lambda  i,j : - self.F(i,j))

    def __add__(self,other):
        """ somme de deux matrices : utilisation du symbole +"""
        assert self.D == other.D, "tailles incompatibles"
        return Mat(self.D, lambda i,j : self.F(i,j) + other.F(i,j))

    def __sub__(self,other):
        """ différence de deux matrices : utilisation dyu symbole -"""
        return self + (-other)

    def transpose(self):
        """ transposée d'une matrice """
        [r,c] = self.D
        return Mat([c,r], lambda i,j : self.F(j,i))

    def prod_par_scal(self,k):
        """ renvoie le produit d'une matrice par un scalaire"""
        return Mat(self.D, lambda i,j: k*self.F(i,j))

    def prod_mat(self,other):
        """ renvoie le produit de deux matrices"""
        [rs,cs],[ro,co] = self.D,other.D
        assert cs == ro, "tailles incompatibles"
        return Mat([rs,co], lambda i,j : prod_scal(self.ligne(i),other.col(j)))

    def map(self,f):
        return Mat(self.D, lambda i,j: f(self.F(i,j)))

    def __mul__(self,other):
        """ produit d'une matrice par un scalaire ou une matrice : utilisation du symbole *"""
        if Mat == type(other):
            return self.prod_mat(other)
        else:
            return self.prod_par_scal(other)


    def powr(self,n):
        """ expo rapide : version récursive"""
        r = self.D[0]
        if n == 0:
            return unite(r)
        def pui(m,k,acc):
            if k == 0:
                return acc
            return pui((m*m),k//2,acc if k % 2 == 0 else (m*acc))
        return pui(self,n,unite(r))

    def __pow__(self,n):
        """expo rapide version impérative"""
        r   = self.D[0]
        k   = n
        m   = self
        acc = unite(r)
        while k > 0:
            if k % 2 == 1:
                acc *= m
            m *= m
            k //= 2
        return acc

    def __eq__(self,other):
        """test d'égalité de deux matrices"""
        if (self.D != other.D):
            return False
        f,g = self.F, other.F
        for (i,j) in self.indices():
            if f(i,j) != g(i,j):
                return False
        return True

    def est_ortho(self):
        r,c = self.D
        assert r == c, "La matrice doit être carrée"
        cols = [list(self.col(j)) for j in range(c)]
        ln = map(lambda c : prod_scal(c,c) == 1, cols)
        p = lambda j : (prod_scal(cols[j],cols[k]) == 0 for k in range(j+1,c))
        lp = (p(j) for j in range(c - 1))
        return all(ln) and all(lp)


    def coupe_en_4(self):
        """
        Coupe une matrice en 4 carrés de même dimension après avoir
        éventuellement complété par des lignes et (ou) des colonnes de
        0 pour obtenir un carré de dimension une puissance de 2
        """
        [r,c] = self.D
        t = max(next_pow_2(r),next_pow_2(c))
        m = Mat([t,t], lambda i,j: self[i,j] if (i < r and j < c) else 0)
        s = t//2
        A = Mat([s, s], lambda i,j: m[i    ,j    ])
        B = Mat([s, s], lambda i,j: m[i    ,j + s])
        C = Mat([s, s], lambda i,j: m[i + s,j    ])
        D = Mat([s, s], lambda i,j: m[i + s,j + s])
        return(A,B,C,D)

    def strassen(self,other):
        ld = self.D + other.D
        t = max(map(next_pow_2,ld))
        if t <= 32:
            return self*other
        a,b,c,d = self.coupe_en_4()
        e,f,g,h = other.coupe_en_4()
        [li,co] = a.D
        p1 = a.strassen(f - h)
        p2 = (a + b).strassen(h)
        p3 = (c + d).strassen(e)
        p4 = d.strassen(g - e)
        p5 = (a + d).strassen(e + h)
        p6 = (b - d).strassen(g + h)
        p7 = (c - a).strassen(e + f)
        w  = p4 + p5 + p6 - p2
        x  = p1 + p2
        y  = p3 + p4
        z  = p1 + p5 - p3 + p7
        def fs(i,j):
            if i < li:
                if j < li:
                    return w.F(i,j)
                else:
                    return x.F(i,j - li)
            elif j < li:
                return y.F(i - li,j)
            else:
                return z.F(i - li,j - li)
        return Mat(self.D, fs)

    def trace(self):
        r,c = self.D
        assert r == c, "La matrice doit être carrée"
        return sum(self[i,i] for i in range(r))


    def comb_lignes(self,ki,kj,i,j):
        """Li <- ki*Li + kj * Lj"""
        f = self.F
        g = lambda r,c : ki*f(i,c) + kj*f(j,c) if r == i else f(r,c)
        return Mat(self.D,g)

    def mult_ligne(self,k,i):
        """Li <- k*Li"""
        f = self.F
        g = lambda r,c : k*f(i,c) if r == i else f(r,c)
        return Mat(self.D,g)

    def cat_carre_droite(self):
        """
        Colle l'identité à droite pour la méthode de GJ

        """
        [lig, col], f = self.D, self.F
        g = lambda r,c: 1 if c == col + r else 0 if c >= col else f(r,c)
        return Mat([lig,2*col],g)

    def extrait_carre_droite(self):
        """
        Extrait le carré de droite d'un tableau de GJ

        """
        r,f = self.D[0],self.F
        return Mat([r,r], lambda i,j:f(i,j + r) )

    def swap(self,i,j):
        """
        Li <-> Lj
        """
        [lig, col], f = self.D, self.F
        g = lambda r,c: f(j,c) if r == i else f(i,c) if r == j else f(r,c)
        return Mat([lig,col],g)

    def decoupe(self):
        """
        Fonction interne à triangle qui  retire la 1ère ligne et la 1ère colonne

        """
        [lig, col], f = self.D, self.F
        return Mat([lig-1,col-1],lambda r,c : f(r+1,c+1))

    def decoupe_bas(self):
        """
        Fonction interne à diago_triangle qui retire la dernière ligne et la
        colonne de même numéro de S

        """
        [lig, col], f = self.D, self.F
        #g = lambda r,c: f(lig-1,c) if r == lig else f(i,c) if r == lig-1 else f(r,c)
        g = lambda r,c: f(r,c) if c < lig - 1 else f(r,c+1)
        return Mat([lig-1,col-1],lambda r,c : g(r,c))

    def remplace_ligned(self,i,g):
        """
        Fonction interne à triangle qui remplace dans la ligne i
        les coefficients à partir de la colonne i par ceux du tableau S
        """
        [lig, col], f = self.D, self.F
        h = lambda r,c: g(r-i,c-i) if r == i and c >= i else  f(r,c)
        return Mat([lig,col],h)

    def remplace_ligneg(self,i,g):
        """
        Fonction interne à diago_triangle qui remplace dans la ligne i
        les coefficients à partir de la colonne i par ceux du tableau S
        """
        [lig, col], f = self.D, self.F
        h = lambda r,c: g(r,c - (lig - 1) + i) if r == i and c >= i else  f(r,c)
        return Mat([lig,col],h)

    def triangle(self):
        """ renvoie la triangulation d'une matrice de haut en bas """
        [r,c] = self.D
        m     = min(r,c)
        S     = self
        T     = zeros(r,c)
        while m > 0:
            NoLigne = 0
            while S[NoLigne, 0] == 0 and (NoLigne < m - 1):
                    NoLigne += 1
            S = S.swap(NoLigne,0)
            if S[0, 0] != 0:
                pivot = S[0,0]
                for k in range(1,m):
                    if S[k,0] != 0:
                        S = S.comb_lignes(pivot, -S[k,0],k,0)
                        #print("pivot = "+str(pivot))
                        #print("S dans for :")
                        #print(S)
            T = T.remplace_ligned(r - m,S.F)
            #print("Évolution de T :")
            #print(T)
            S = S.decoupe()
            m -= 1
        return T

    def diago_triangle(self,inv):
        """ renvoie la triangulation d'un tableau de GJ d'une matrice
        inversible de bas en haut """
        [r,c] = self.D
        assert c == 2*r, "Le tableau doit être un rectangle L x (2L)"
        m     = r - 1
        S     = self
        T     = zeros(r,c)
        while m >= 0:
            pivot = S[m,m]
            assert pivot !=0, "matrice non inversible"
            for k in range(m-1,-1,-1):
                if S[k,m] != 0:
                    S = S.comb_lignes(pivot, -S[k,m],k,m)
            T = T.remplace_ligneg(m,S.F)
            S = S.decoupe_bas()
            m -= 1
        for k in range(r):
            T = T.mult_ligne(inv(T[k,r-1]),k)
        return T



    def rang(self):
        r,c = self.D
        T = self.triangle()
        return len([T[i,i] for i in range(r) if T[i,i] != 0])

    def det(self,div):
        """ renvoie le déterminant de self par Gauss-Jordan """
        [r,c] = self.D
        assert r == c, "Matrice non carrée"
        S,i,d = self,1,1
        while r > 0:
            NoLigne = 0
            while S[NoLigne, 0] == 0 and (NoLigne < r - 1):
                    NoLigne += 1
            if S[NoLigne, 0] == 0:
                return 0
            pivot = S[NoLigne,0]
            S = S.swap(0,NoLigne)
            i *= (-1) ** (NoLigne != 0)
            for k in range(1,r):
                if S[k,0] != 0:
                    S = S.comb_lignes(pivot, -S[k,0],k,0)
                    i *=  pivot
            S = S.decoupe()
            r -= 1
            d *= pivot
        return (div(d,i))


    def inverse(self,inv):
        return self.cat_carre_droite().triangle().diago_triangle(inv).extrait_carre_droite()


# In [340]: A = list2mat([[0,1,0,0],[2,-1,9,1],[2,7,4,-12],[2,0,-1,-1]])


def next_pow_2(x):
    return 2**(ceil(log(x)/log(2)))

def all(it):
    for i in it:
        if not i:
            return False
    return True

def randmat(r,c,min = 0,max = 9):
    return Mat([r,c],lambda  i,j : randint(min,max))

def list2mat(mat):
    r,c = len(mat),len(mat[0])
    return Mat([r,c], lambda i,j : mat[i][j])


def prod_scal(it1,it2):
    return sum(map(mul,it1,it2))

def unite(n):
    return Mat([n,n], lambda i,j: 1 if i == j else 0)


def zeros(r,c):
    return Mat([r,c], lambda i,j: 0)





#######################################
#
#        Chiffrement de Hill
#
#######################################

def ascii(chaine):
    return [ord(c)-ord((' ')) for c in chaine]

def deascii(chaine):
    return ''.join(chr(x + ord((' '))) for x in chaine)

def to_Hill(m,p):
    cs = ascii(m)
    ls = len(cs)
    reste = ls % p
    cs = cs + ([] if reste == 0 else [0 for k in range(p - (ls % p))])
    g = lambda i,j: cs[(i % p) + p*j]
    return Mat([p,len(cs) // p], g)


cle = list2mat([[1,23,29],[0,31,1],[47,3,1]])

def bezout(a,b) :
    la  = np.array([1, 0, a])
    lb  = np.array([0, 1, b])
    while lb[2] != 0 :
        q      = la[2] // lb[2]
        la, lb = lb, la - q*lb
    return la

def inv_mod(p,n):
    B = bezout(p,n)
    assert B[2] == 1, str(p) + ' non iversible modulo ' + str(n)
    return B[0]%n


inv_cle = cle.inverse(lambda x: inv_mod(x, 95)).map(lambda n : n % 95)

clair = to_Hill("Arghh !! Ce 1000 pattes aurait 314 pattes ??",3)

crypte = deascii(iter((cle * clair).map(lambda n : n % 95)))


decrypte = deascii(iter((inv_cle * (to_Hill(crypte,3))).map(lambda n : n % 95)))



####
#
# Markov
#
########


P = list2mat([[0.8,0.3,0.2],[0.1,0.2,0.6],[0.1,0.5,0.2]])

X0 = Mat([3,1],lambda i,j : 1 if i == 0 else 0)


Xs = P**30 * X0

D = P*Xs - Xs



###############
#
#  Lena
#
#################"

def rvb_to_gray(m):
    r,c = len(m), len(m[0])
    return(np.array([[sum(m[i,j]) / 3 for j in range(c)] for i in range(r)]))

def array2mat(tab):
    """ convertit un array de numpy en objet de type Mat"""
    dim = list(tab.shape)
    return Mat(dim,  lambda i,j : tab[i,j])

def mat2array(mat):
    """ convertir un objet de type Mat en array de numpy """
    return np.fromfunction(np.vectorize(mat.F),tuple(mat.D),dtype = int)

lena_face_couleur = plt.imread('../figures/lenaFace.jpeg')


lena_face_array = rvb_to_gray(lena_face_couleur)

lena_face = array2mat(lena_face_array)

matlena = array2mat(misc.lena())

def montre(mat):
    """ permet de visualiser les images dans un terminal """
    return imshow(mat2array(mat), cmap = cm.gray)


def retourne(m):
    [r,c], f = m.D, m.F
    return Mat([r,c],lambda i,j: f(r - 1 - i, j))

def miroir(m):
    [r,c], f = m.D, m.F
    return Mat([r,c],lambda i,j: f(i,c - 1 - j))

def resolution(k,mat):
    [r,c],f = mat.D,mat.F
    return Mat([r//k,c//k], lambda i,j : f(k*i,k*j))



def ber(p):
    return 1 if random() < p else 0

def rand_image(dim,p):
    return Mat(dim, lambda i,j : randint(0,255)*ber(p))

def bruit(mat,p):
     return (mat + rand_image(mat.D,p))

def moyenne(mat,k):
    [li,co],f = mat.D, mat.F
    return Mat([li - k,co - k],
               lambda i,j : np.mean([f(r, c)
                                     for r in range(i - k, i + k + 1)
                                     for c in range(j - k, j + k + 1)]))


def mediane(mat,k):
    [li,co],f = mat.D, mat.F
    return Mat([li - k,co - k],
               lambda i,j : np.median([f(r, c)
                                       for r in range(i - k, i + k + 1)
                                       for c in range(j - k, j + k + 1)]))

def contour(m):
    [li,co] = m.D
    return Mat([li - 2, co - 2],
               lambda i,j : floor(sqrt((m[i,j-1]-m[i,j+1])**2 + (m[i-1,j]-m[i+1,j])**2))
    )



def comp_svd(mat,k):
    [r,c] = mat.D
    U,s,tV = linalg.svd(mat2array(mat))
    U,s,tV = array2mat(U),list(s),array2mat(tV)
    fu,ftv = U.F, tV.F
    C = zeros(r,c)
    for p in range(k):
        C += (Mat([r,1],lambda i,j: fu(i,p)) * Mat([1,c], lambda i,j: ftv(p,j))) * s[p]
    return C.map(lambda c: floor(c) % 256)


def c_svd(mat,k):
    U,s,tV = linalg.svd(mat)
    d = mat.shape
    C = np.zeros(d)
    for p in range(k):
        C += s[p]*(np.dot(U[:,p].reshape((d[0], 1)),tV[p,:].reshape((1,d[1]))))
    return C


#    U,s,tV = linalg.svd(mat)
#    x = np.arange(len(s))
#    plot(x,s)

def anim(n):
    plt.clf()
    for k in range(n):
        plt.imsave("lena_face_svd" + str(1000 + k) + '.jpg', c_svd(lena_face_array,k), cmap = cm.pink)

anim(150)

os.system("mencoder 'mf://lena_face_svd*.jpg' -mf type=jpg:fps=10 -ovc lavc  -o lena_animee.mpg")

os.system("rm lena_face_svd*.jpg")
