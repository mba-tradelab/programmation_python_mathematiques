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

"""Esquisses de classes pour polynômes, nombres rationnels et fractions rationnelles."""

class Polynome(object):
    """Classe de polynômes.

    >>> p1 = Polynome([1, 4, 6, 3, 0, 0])
    >>> p2 = Polynome([-4, 2, 7, 1, 2])
    >>> print(p1, p2, p1 + p2, sep=' ; ')
    1 + 4.X + 6.X^2 + 3.X^3 ; (-4) + 2.X + 7.X^2 + X^3 + 2.X^4 ; (-3) + 6.X + 13.X^2 + 4.X^3 + 2.X^4
    >>> print(p1 * p2)
    (-4) + (-14).X + (-9).X^2 + 29.X^3 + 54.X^4 + 35.X^5 + 15.X^6 + 6.X^7
    """

    def __init__(self, coefficients):
        self.coeffs = coefficients

    def deg(self):
        n = len(self.coeffs)
        for i, c in enumerate(reversed(self.coeffs)):
            if c != 0:
                return n-1-i
        return -1

    def __call__(self, x):
        somme = 0
        for c in reversed(self.coeffs):
            somme = c + x*somme
        return somme

    def str_monome(self, i, c):
        coeffs = '{}'.format(c) if c >= 0 else '({})'.format(c)
        indet = '.X^{}'.format(i) if i > 1 else ('.X' if i == 1 else '')
        return ''.join([coeffs, indet])

    def __str__(self):
        chaine = ' + '.join(self.str_monome(i, c)
                for i, c in enumerate(self.coeffs) if c !=0)
        chaine = chaine.replace(' 1.', ' ')
        return chaine if chaine != '' else '0'

    def __add__(self, other):
        if self.deg() < other.deg():
            self, other = other, self
        tmp = other.coeffs + [0]*(self.deg() - other.deg())
        return Polynome([x+y for x, y in zip(self.coeffs, tmp)])

    def mul_monome(self, i, c):
        return Polynome([0]*i + [c * x for x in self.coeffs])

    def __mul__(self, other):
        tmp = Polynome([0])
        for i, c in enumerate(other.coeffs):
            tmp += self.mul_monome(i, c)
        return tmp

class FracRationnelle(Polynome):
    """Première version d'une classe pour les fractions rationnelles.

    >>> p1, p2, p3 = Polynome([1]), Polynome([-1, 1]), Polynome([1, 1])
    >>> r1, r2 = FracRationnelle(p1, p2), FracRationnelle(p1, p3)
    >>> print(r1, r2, r1 + r2, r1 * r2, sep=' ; ')
    (1) / ((-1) + X) ; (1) / (1 + X) ; (2.X) / ((-1) + X^2) ; (1) / ((-1) + X^2)
    >>> print(r1(-1.3))
    -0.4347826086956522
    """

    def __init__(self, numerateur, denominateur):
        self.numer = numerateur
        self.denom = denominateur

    def deg(self):
        return self.numer.deg() - self.denom.deg()

    def __call__(self, x):
        return self.numer.__call__(x) / self.denom.__call__(x)

    def __str__(self):
        return ("({}) / ({})".format(self.numer, self.denom))

    def __add__(self, other):
        numer = (self.numer * other.denom
                + self.denom * other.numer)
        denom = self.denom * other.denom
        return FracRationnelle(numer, denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return FracRationnelle(numer, denom)

class Rationnel(object):
    """Classe pour les nombres rationnels.

    >>> q1, q2 = Rationnel(2, 3), Rationnel(5, 7)
    >>> print(q1, q2, q1 + q2, q1 * q2, sep=' ; ')
    (2) / (3) ; (5) / (7) ; (29) / (21) ; (10) / (21)
    """

    def __init__(self, num, den):
        self.numer = num
        self.denom = den

    def __str__(self):
        return ("({}) / ({})".format(self.numer, self.denom))

    def __add__(self, other):
        denom = self.denom * other.denom
        numer = (self.numer * other.denom
                 + other.numer * self.denom)
        return Rationnel(numer, denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rationnel(numer, denom)

class FracRationnelle2(Rationnel, Polynome):
    """Deuxième version d'une classe pour les fractions rationnelles
    (exemple d'héritage multiple).

    >>> p1, p2, p3 = Polynome([1]), Polynome([-1, 1]), Polynome([1, 1])
    >>> r1, r2 = FracRationnelle2(p1, p2), FracRationnelle2(p1, p3)
    >>> print(r1, r2, r1 + r2, r1 * r2, sep=' ; ')
    (1) / ((-1) + X) ; (1) / (1 + X) ; (2.X) / ((-1) + X^2) ; (1) / ((-1) + X^2)
    >>> print(r1(-1.3))
    -0.4347826086956522
    """

    def __init__(self, numerateur, denominateur):
        self.numer = numerateur
        self.denom = denominateur

    def deg(self):
        return self.numer.deg() - self.denom.deg()

    def __call__(self, x):
        return self.numer.__call__(x) / self.denom.__call__(x)

    def __add__(self, other):
        tmp = (Rationnel(self.numer, self.denom)
                + Rationnel(other.numer, other.denom))
        return FracRationnelle2(tmp.numer, tmp.denom)

    def __mul__(self, other):
        tmp = (Rationnel(self.numer, self.denom)
                * Rationnel(other.numer, other.denom))
        return FracRationnelle2(tmp.numer, tmp.denom)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

