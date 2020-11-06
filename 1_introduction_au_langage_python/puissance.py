#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

def puissance(x, n):
    if n == 0: return 1
    else:
        print('--'*n + '> appel de puissance({},{})'.format(x, n-1))
        y = x * puissance(x, n-1)
        print('--'*n + '> sortie de puissance({},{})'.format(x, n-1))
        return y
    
