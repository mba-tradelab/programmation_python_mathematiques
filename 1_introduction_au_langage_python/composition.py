#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

# On peut munir une fonction d'une documentation appelée en anglais "docstring"
# Elle doit être placée à la ligne qui suit le mot-clef def
# Elle doit être saisie entre triples guillemets anglais
# La première phrase se doit d'expliquer de manière concise à quoi sert la fonction
# Pour une fonction un peu développée, on peut même inclure après une ligne blanche
# des exemples d'utilisation qui peuvent ensuite servir de tests unitaires

def composition(f, g):
    """Renvoie la composée de deux fonctions f et g.
    >>> from math import sin, cos
    >>> f = composition(cos, sin)
    >>> g = composition(sin, cos)
    >>> [f(x) - g(x) for x in range(0, 3)]
    [0.1585290151921035, 0.15197148686933137, 1.018539435968748]
    """

    return lambda x: f(g(x))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Pour accéder à la documentation de la fonction, on utilise help
# Pour lancer les tests, on exécute le script avec l'option -v
# $python3 composition.py -v
