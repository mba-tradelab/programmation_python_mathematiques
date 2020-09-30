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




class Bits(list):
    """
    Crée des objets pour représenter des chaînes de bits correspondant à des entiers signés à partir de listes de 0 et 1.
    Par exemple 13 sera Bits([0,1,1,0,1])
    """

    def __init__(self,bits = []):
        """ Une chaine de bits est construite à partir de la liste de ses bits"""
        self.bits = bits

    def __iter__(self):
        """ On itère sur la liste des bits"""
        return iter(self.bits)

    def __len__(self):
        """ Permet de donner le nombre de bits avec la méthode len"""
        return len(self.bits)

    def __getitem__(self,cle):
        """ Pour obtenir le bit en position cle avec b[cle] ou une
            séquence de bits avec b[deb..fin]"""
        return self.bits[cle]

    def __reversed__(self):
        """Pour renvoyer la chaîne de bits inversée"""
        return Bits(self.bits[::-1])

    def norm(self):
        """Normalise l'écriture d'une chaîne de bits en supprimant les
        bits non significatifs à gauche"""
        if len(self) == 0:
            return self
        if len(self) == 1:
            return Bits(self.bits + self.bits)
        tete = self[0]
        qs   = self[1:]
        if qs[0] == tete:
            return Bits(qs).norm()
        return self

    def __str__(self):
        """On utilise la fonction str pour afficher la liste des bits"""
        return str(self.bits)

    def __repr__(self):
        """Une belle représentation dans l'interpréteur
           Bits([0,1,1,0,1]) est affiché 0:1101"""
        n = self.norm()
        return str(n[0]) + ':' + ''.join(str(b) for b in n.bits[1:])

    def map(self,fonc):
        """Applique une fonction aux bits d'une chaîne"""
        return Bits(list(map(fonc,self.bits)))

    def comp1(self):
        """Renvoie le complément à 1 d'une chaîne"""
        return self.map(lambda x : 0 if x  else 1)


    def __add__(self, other):
        """
        Additionne deux entiers en base 2 sous forme de la liste de leurs bits
        """
        # Formate les listes pour qu'elles soient de même longueur
        long = max(len(self), len(other)) + 1
        s1,s2 = self.signe(), other.signe()
        op1 = Bits([s1 for i in range(len(self), long)] + self.bits)
        op2 = Bits([s2 for i in range(len(other), long)] + other.bits)
        # stocke la retenue de la précédente somme de 2 bits
        retenue = 0
        # On stocke la somme intermédiaire
        res = [];
        # on itère dans l'ordre inverse de la liste des bits des opérandes
        for i in range(1, long):
            b1,b2 = op1[-i], op2[-i]
            # unité comme xor des deux bits et de la retenue
            res = [b1 ^ b2 ^ retenue] + res
            # retenue : vaut 1 si au moins 2 bits sont à 1
            retenue = (retenue & (b1 | b2)) | (b1 & b2)
        # on ajoute l'éventuelle dernière retenue à droite
        if s1 != s2:
            res = [retenue ^ s1 ^ s2] + res
        else:
            if retenue != 0:
                res = [s1, retenue] + res
            else:
                res = [s1] + res
        # on remet la liste dans le bon sens
        return Bits(res).norm()


    def __neg__(self):
        """Opposé d'une chaîne en utilisant le symbole -"""
        bs = self.bits
        signe = bs[0]
        if signe == 1:
            return (self + Bits([1 for k in range(len(bs))])).comp1()
        return self.comp1() + Bits([0,1])

    def __sub__(self,other):
        """Différence de deux chaînes avec -"""
        return self + (-other)

    def __abs__(self):
        """Valeur absolue d'une chaîne"""
        return -self if self.signe() == 1 else self

    def mantisse(self):
        """La liste des bits sans le bit de signe"""
        return self.norm()[1:]


    def __eq__(self,other):
        """Permet de tester l'égalité de deux chaînes à partir de leur forme normalisée"""
        return self.norm().bits == other.norm().bits

    def signe(self):
        """Renvoie le bit de signe"""
        return self[0]

    def to_dec(self):
        """Renvoie l'écriture décimale de la chaîne de bits"""
        ab = abs(self)
        cs = ab.mantisse()[::-1]
        if cs == []:
            return 0
        n   = 0
        dec = 0
        for c in cs:
            n += int(c) << dec
            dec += 1
        return n if self.signe() == 0 else -n

    def pair(self):
        """Teste la parité d'une chaîne"""
        return self[-1] == 0


    def mul_primaire(self,other):
        """Multiplication avec l'algo appris à l'école primaire"""
        s1,s2 = self.signe(),other.signe()
        sig = s1 ^ s2
        op1, op2 = abs(self)[1:], abs(other)[1:]
        m = Bits([0,0])
        dec = len(op1) - 1
        for n1 in op1:
            m1 = []
            for n2 in op2:
                m1.append(n2 * n1)
            m = m + Bits([0] + m1 + [0 for k in range(dec)])
            dec -= 1
        if sig == 1:
            return -m
        return m


    def mul_russe(self,other):
        """Algo de la multiplication du paysan russe"""
        op1,op2 = self.norm(),other.norm()
        if op1[0] == 1:
            return -((-op1).mul_russe(op2))
        if op2[0] == 1:
            return -(op1.mul_russe(-op2))
        def aux(acc,x,y):
            if x == Bits([0,0]):
                return acc
            return aux(acc + (Bits([0,0]) if x.pair() else y), Bits(x[:-1]), Bits(y.bits + [0]))
        return aux(Bits([0,0]),op1,op2)


    def mul_divis(self, other):
        """Algo dichotomique naïf de multiplication"""
        op1,op2 = self.norm(),other.norm()
        if op1.signe() == 1:
            return -((-op1).mul_divis(op2))
        if op2.signe() == 1:
            return -(op1.mul_divis(-op2))
        long = max(len(op1), len(op2))
        op1 = Bits([0 for i in range(len(op1), long)] + op1.bits)
        op2 = Bits([0 for i in range(len(op2), long)] + op2.bits)

        if long <= 2:
            return Bits([0, op1[1] & op2[1]])

        m0 = (long + 1) >> 1 # ie // 2
        m1 = long >> 1

        x0 = Bits([0] + op1[  : m0]).norm()
        x1 = Bits([0] + op1[m0 :  ]).norm()
        y0 = Bits([0] + op2[  : m0]).norm()
        y1 = Bits([0] + op2[m0 :  ]).norm()

        p0 = x0.mul_divis(y0)
        p1 = x1.mul_divis(y0)
        p2 = x0.mul_divis(y1)
        p3 = x1.mul_divis(y1)

        z0prod = Bits(p0.bits + [0 for i in range(0,  m1 << 1)])
        z1prod = Bits((p1 + p2).bits + [0 for i in range(0, m1)])
        z2prod = p3

        return z0prod + z1prod + z2prod


    def mul_karat(self, other):
        """Algo de Karatsouba"""
        op1,op2 = self.norm(),other.norm()
        if op1.signe() == 1:
            return -((-op1).mul_karat(op2))
        if op2.signe() == 1:
            return -(op1.mul_karat(-op2))
        long = max(len(op1), len(op2))
        op1 = Bits([0 for i in range(len(op1), long)] + op1.bits)
        op2 = Bits([0 for i in range(len(op2), long)] + op2.bits)

        if long <= 2:
            return Bits([0, op1[1] & op2[1]])

        m0 = (long + 1) >> 1
        m1 = long >> 1

        x0 = Bits([0] + op1[  : m0]).norm()
        x1 = Bits([0] + op1[m0 :  ]).norm()
        y0 = Bits([0] + op2[  : m0]).norm()
        y1 = Bits([0] + op2[m0 :  ]).norm()

        p0 = x0.mul_karat(y0)
        p1 = (x0 - x1).mul_divis(y0 - y1)
        p2 = x1.mul_divis(y1)

        z0 = Bits(p0.bits + [0 for i in range(0, m1 << 1)])
        z1 = Bits((p0 + p2 - p1).bits + [0 for i in range(0, m1)])
        z2 = p2

        return z0 + z1 + z2



    def __mul__(self,other):
        """Définit la multplication de deux chaîne avec l'un des algos proposés"""
        return self.mul_russe(other)


# mul_russe
# In [48]: %timeit (n * n)
# 1000 loops, best of 3: 525 µs per loop

# mul_karat
# In [51]: %timeit (n * n)
# 100 loops, best of 3: 3.14 ms per loop

# mul_divis
# In [54]: %timeit (n * n)
# 100 loops, best of 3: 7.08 ms per loop

# mul_primaire
# In [57]: %timeit (n * n)
# 1000 loops, best of 3: 576 µs per loop







def dec2bits(n):
    if n == 0:
        return [0]
    s = []
    i = abs(n)
    while i:
        if i & 1 == 1:
            s = [1] + s
        else:
            s = [0] + s
        i >>= 1
    s = [0] + s
    if n < 0:
        return -Bits(s)
    return Bits(s)





## ieee754

from math import floor

def petits2bits(x,nmax):
    dec = abs(x)
    bin = ""
    k = 0
    while dec != 0 and k < nmax:
        a = floor(2*dec)
        bin += str(a)
        dec = 2*dec - a
        k += 1
    return '0:' + bin




