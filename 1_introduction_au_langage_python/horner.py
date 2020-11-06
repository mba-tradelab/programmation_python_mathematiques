#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

# Méthode de Horner pour évaluer efficacement un polynôme en une valeur donnée
# p(x) = a0 + a1 * x + a2 * x^2 + a3 * x^3 + ... + an * x^n
# En x0, on remarque que
#       p(x0) = ((...((an*x0 + an-1)*x0+an-2)*x0+...)*x0+a1)*x0 + a0
# Il n'y a alors que n multiplications à effectuer
# Pour programmer cet algorithme, il suffit de calculer les valeurs de bn :
#       bn = an
#       ∀ k ∈ [0,n-1], bk = ak + bk+1*x0

def horner_rec(p, x):
    if len(p) = 1: return p[0]
    p[-2] += x * p[-1]
    return horner_rec(p[:-1], x)
