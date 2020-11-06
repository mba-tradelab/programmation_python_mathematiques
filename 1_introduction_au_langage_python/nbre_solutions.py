#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

def nbre_solutions(a, b, c):
    if a == 0:
        print('L\'équation est du premier degré.')
    else:
        delta = b**2 - 4*a*c
        if delta > 0:
            print('L\'équation possède deux solutions réelles.')
        else:
            if delta == 0:
                print('L\'équation possède une solution réelle.')
            else:
                print('L\'équation ne possède pas de solution réelle.')

def nbre_solutions_(a, b, c):
    delta = b**2 - 4*a*c
    if a == 0:
        print('L\'équation est du premier degré.')
    elif delta > 0:
        print('L\'équation possède deux solutions réelles.')
    elif delta == 0:
        print('L\'équation possède une solution réelle.')
    else:
        print('L\'équation ne possède pas de solution réelle.')
