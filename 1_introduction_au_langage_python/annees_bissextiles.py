#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

# Années bissextiles
# On rappelle que les années bissextiles reviennent tous les 4 ans, sauf les
# années séculaires, si celles-ci ne sont pas multiples de 400

def bissextile_(n):
    if n % 4 != 0:
        return False
    elif n % 100 != 0:
        return True
    elif n % 400 != 0:
        return False
    else:
        return True

def bissextile(n):
    # fonction booléenne qui permet de tester si une année est bissextile
    return ((n % 4 == 0) and (n % 100 != 0)) or (n % 400 == 0)        
