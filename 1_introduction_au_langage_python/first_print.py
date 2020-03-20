#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

x, y = 3, 1000000000
z = 3.1416
print(x, y, z, sep='')
print(x, y, z, sep='; ')
print(x, y, z, sep='\n')
print('x=', x, sep='', end='; ')
print('y=', y, sep='', end='; ')
print('z=', z, sep='')

print('*******')

print('-> Ici on peut employer des "guillemets" !')
print("-> Ici on peut employer des 'apostrophes' !")
print(""" -> Voici un saut...
    de ligne.""")
print("-> On peut aussi\n passer à la ligne ainsi.")

print('\n ******** \n')

print(' -> Comment couper une ligne '
      'trop longue dans le fichier source ?')
