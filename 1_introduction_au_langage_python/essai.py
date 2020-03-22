#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

def essai(N):
    n = 0
    while 2**n <= N:
        n += 1
    return n
