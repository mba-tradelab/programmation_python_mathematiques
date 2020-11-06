#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

def max2(x, y):
    # fonction qui renvoie le plus grand des deux nombres x et y
    return x if x >= y else y

def max3(a, b, c):
    # fonction qui calcule le maximum de 3 nombres
    return max2(a, max2(b, c))
