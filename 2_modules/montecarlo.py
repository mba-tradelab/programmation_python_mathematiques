#/usr/bin/python3
#-*- coding: Utf-8 -*-

import random, math

def montecarlo(f, a, b, n):
    s = 0
    for i in range(n):
        x = random.uniform(a, b)
        s += f(x)
    return s * (b-a) / n

def f(x):
    return math.sqrt(1-x**2)

print('-'*63)
print('{0:>10s} | {1:^12s} | {2:^14s} | {3:^15s} |'
      .format('n', 'approximation', 'erreur absolue', 'erreur relative'))
print('-'*63)
for i in range(0, 10, 2):
    n = 10**i
    approx = 4*montecarlo(f, 0, 1, n)
    erreur = math.pi - approx
    print('{0:10d} | {1: 12.10f} | {2: 14.10f} | {3: 15.10f} |'
          .format(n, approx, erreur, abs(erreur/math.pi)))
print('-'*63)
