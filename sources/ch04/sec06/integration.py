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


from math import *

class Integration(object):
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n
        self.poids_pivots = self.quadrature()

    def quadrature(self):
        raise NotImplementedError

    def integrale(self, f):
        return sum(w * f(x) for w, x in self.poids_pivots)

class Rectangles(Integration):
    def quadrature(self):
        a, b, n = self.a, self.b, self.n
        h = (b-a) / n
        return [(h, a + i*h) for i in range(n)]

class Trapezes(Integration):
    def quadrature(self):
        a, b, n = self.a, self.b, self.n
        h = (b-a) / n
        return [(h, a + (i+0.5)*h) for i in range(n)]

class Simpson(Integration):
    def coeff(self, i, N):
        if i == 0 or i == N:
            return 1
        elif i % 2 == 1:
            return 4
        else:
            return 2

    def quadrature(self):
        a, b, n = self.a, self.b, self.n
        if n % 2 != 1:
            n += 1
        h = (b-a) * 0.5 / n
        return [(h/3*self.coeff(i, 2*n), a + i*h) for i in range(2*n+1)]


class GaussLegendre(Integration):
    def gaussPivots(self, m, tol=1e-14):
        def legendre(t, m):
            p0, p1 = 1, t
            for k in range(1, m):
                p = ((2*k+1)*t*p1 - k*p0) / (1+k)
                p0, p1 = p1, p
            dp = m*(p0 - t*p1) / (1 - t**2)
            return p, dp

        w = [0 for i in range(m)] # poids
        x = [0 for i in range(m)] # pivots
        nRoots = (m + 1)//2          # nbre de recines positives
        for i in range(nRoots):
            t = cos(pi*(i + 0.75)/(m + 0.5))  # racine approchée
            for j in range(30):
                p, dp = legendre(t, m)          # méthode
                dt = -p / dp; t = t + dt        # de Newton
                if abs(dt) < tol:
                    x[i] = t; x[m-i-1] = -t
                    w[i] = 2 / (1 - t**2) / (dp**2)
                    w[m-i-1] = w[i]
                    break
        return zip(w, x)

    def quadrature(self):
        a, b, n = self.a, self.b, self.n
        return [((b-a)*w*0.5, (a+b)*0.5 + (a-b)*0.5*x)
                for w, x in self.gaussPivots(n)]

class Romberg(object):
    def __init__(self, a, b, m):
        self.a, self.b, self.m = a, b, m

    def integrale(self, f):
        a, b, m = self.a, self.b, self.m
        A = [[(b-a) * (f(a)+f(b)) * 0.5]]
        for k in range(1, m+1):
            h = (b-a) / 2**k
            Ap = h * sum([f(a + j*h)
                    for j in range(1, 2**k, 2)])
            A.append([0.5 * A[k-1][0] + Ap])
        for t in range(1, m+1):
            for k in range(t, m+1):
                A[k].append((4**t * A[k][t-1] - A[k-1][t-1])
                        / (4**t-1))
        return A[m][m]


def simpson(f, a, b):
    c = (a+b) * 0.5
    return (f(a) + 4*f(c) + f(b)) * abs(b-a) / 6

def simpson_adaptative(f, a, b, eps):
    c = (a+b) * 0.5
    reunion = simpson(f, a, b)
    gauche = simpson(f, a, c)
    droite = simpson(f, c, b)
    if abs(gauche + droite - reunion) <= 15 * eps:
        return gauche + droite + (gauche + droite - reunion)/15
    else:
        return (simpson_adaptative(f, a, c, eps/2)
                + simpson_adaptative(f, c, b, eps/2))

if __name__ == '__main__':

    from math import *
    import sys
    sys.path.append('../../modules')
    from PostScript import plot, nrange

    ########################
    ### Spirale de Cornu ###
    ########################

    def z(t):
        s = Simpson(0, t, 1000)
        x = lambda u:cos(u**2)
        y = lambda u:sin(u**2)
        return (s.integrale(x), s.integrale(y))

    numpoints, a, b, zoom = 1000, -10 , 10, 100
    boite = [-1, -1, 1, 1] # xmin, ymin, xmax, ymax

    liste = (z(x) for x in nrange(a, b, numpoints))
    plot("cornu", boite, zoom, [[liste, (0, 0, 1)]], axes=False)

    #################################################
    ### Conjecture sur la convergence d'une suite ###
    #################################################

    print("Conjecture sur la convergence d'une suite")
    m = Romberg(0, 1, 16)

    def u(n):
        return m.integrale(lambda x:log(1+x**n))

    def v(n):
        return n * (u(n+1)/u(n) - 1)

    n, liste = 2**8, [1, 0]

    while n <= 10**4 and abs(liste[0] - liste[1]) > 1e-10:
        liste = [v(n), v(n+1)]
        print("n={:4d} | v(n)={: .10f}".format(n, liste[0]))
        n *= 2
    print("n*u(n)={:f}".format(n*u(n)))
    print(pi**2/12)

    ######################################
    ### Tracé de polynômes de Legendre ###
    ######################################

    def legendre(t, m):
        if m == 0:
            return 1
        elif m==1:
            return t
        else:
            p0, p1 = 1, t
            for k in range(1, m):
                p = ((2*k+1)*t*p1 - k*p0) / (1+k)
                p0, p1 = p1, p
            return p

    numpoints, a, b, fichier, zoom = 1000, -1 , 1, "legendre", 120
    boite = [-1.1, -1.1, 1.1, 1.1] # xmin, ymin, xmax, ymax

    liste = ((((x, legendre(x, n))
            for x in nrange(a, b, numpoints)), (n/10, 0.32, 1 - n/16))
            for n in range(1, 11))

    plot(fichier, boite, zoom, liste, gradH=.03, ratioY=.4)

    #############################################
    ### Comparatif des méthodes d'intégration ###
    #############################################

    print("Comparatif des méthodes d'intégration")

    print("{:>3} | {:^10} | {:^10} | {:^9} | {:^9} | {:^9}".format("n",
          "rectangles", "trapèzes", "Simpson", "Romberg", "Gauss"))
    for i in range(1, 8):
        r = Rectangles(0, 0.5, 2**i)
        t = Trapezes(0, 0.5, 2**i)
        s = Simpson(0, 0.5, 2**i)
        ro = Romberg(0, 0.5, i)
        g = GaussLegendre(0, 0.5, 2**i)
        comp = [eval(m).integrale(lambda x:sqrt(1-x**2))
                for m in ['r', 't', 's', 'ro', 'g']]
        comp = [pi - 12*(c - sqrt (3)/8) for c in comp]
        print("{0:>3d} |  {1[0]: .2e} |  {1[1]: .2e} | {1[2]: .2e} "
              "| {1[3]: .2e} | {1[4]: .2e}".format(2**i, comp))

    #####################################
    ### Méthode de Simpson adaptative ###
    #####################################

    print('Méthode de Simpson adaptative')

    s = 4 * simpson_adaptative(lambda x:sqrt(1-x**2), 0, 1, 1e-9)

    print("{:20} ---> {: .15f}".format("pi", pi))
    print("{:20} ---> {: .15f} => erreur = {: .2e}"
            .format("Simpson adaptative", s, pi-s))

