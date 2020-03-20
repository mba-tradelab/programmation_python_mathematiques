#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

x = eval(input('Entrez une valeur pour la variable x : '))
print('{}^2 = {}'.format(x, x**2))

print('\n ******** \n')

from math import *
x = eval(input('x = ?'))
fonction = input('f = ?')
code = ('def f(x):'
        '    return {}'.format(fonction))
exec(code)
print('{:.6f}'.format(f(x)))
