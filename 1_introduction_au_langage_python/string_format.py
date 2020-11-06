#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

x = 1037.123456789

print('{:g}'.format(x), '# {:g} choisit le format le plus approprié')
print('{:.3f}'.format(x), '# {:.nf} fixe le nombre n de décimales')
print('{:.3e}'.format(x), '# {:.3e} notation scientifique')
print('{0:20.3f}'.format(x), '# {0:20.3f} précise la longueur de la chaîne' )
print('{0:>20.3f}'.format(x), '# {0:>20.3f} justifié à droite')
print('{0:<20.3f}'.format(x), '# {0:<20.3f} justifié à gauche')
print('{0:^20.3f}'.format(x), '# {0:^20.3f} centré')
print('{0:+.3f} ; {1:+.3f}'.format(x, -x), '# {0:+3f}, {1:+.3f} affiche toujours le signe')
print('{0: .3f} ; {1: .3f}'.format(x, -x), '# {0: .3f}, {1: .3f} affiche un espace si x > 0')

