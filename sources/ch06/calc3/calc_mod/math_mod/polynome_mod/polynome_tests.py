#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
# (C) Alexandre Casamayou-Boucau, Pascal Chauvin, Guillaume Connan     #
#                                                                      #
# Complément de l'ouvrage :                                            #
# Programmation en Python pour les mathématiques                       #
# Editeur : Dunod                   -        Collection : Sciences Sup #
# ISBN-13: 978-2100738311           -                  Licence : GPLv2 #
########################################################################

#
# fichier: polynome_tests.py
# version: 0.5.0
#  auteur: Pascal CHAUVIN
#    date: 2014/10/28
#
# (tous les symboles non internationaux sont volontairement omis)
#

import sys
sys.path.append('../monome_mod')
sys.path.append('../rationnel_mod')

import polynome as po

import monome as mo
import rationnel as ra

def test_unitaire_0(visible =False):
	print("*** polynome: test_unitaire_0 ***")
	
	a = po.polynome()
	if visible: print(a)
	
	ok = (a.nombre_monomes() == 1)
	return ok
	
	
	
def test_unitaire_1(visible =False):
	print("*** polynome: test_unitaire_1 ***")
		
	a = po.polynome(mo.monome(ra.rationnel(12), "x"))
	if visible: 
		print(a)
		print(repr(a))
		print(a.lire_monome())
		print(a.plat())

	ok = a.contient(mo.monome(ra.rationnel(1), "x"))
	return ok
	
	
	
def test_unitaire_2(visible =False):
	print("*** polynome: test_unitaire_2 ***")
	
	a = po.polynome(mo.monome(ra.rationnel(12), "x"))
	if visible: print(a.plat())
		
	a.inserer(mo.monome(ra.rationnel(1), "y"))
	if visible: print(a.plat())
		
	a.inserer(mo.monome(ra.rationnel(1), "a"))
	if visible: print(a.plat())
	
	if visible: print("---")
	
	b = po.polynome()
	for t in a.iterateur():
		b.inserer(t)
	
	if visible: print(b.plat())
	
	ok = (a.fin().lire_monome().lire_indet() == "y")
	return ok



def test_unitaire_3(visible =False):
	print("*** polynome: test_unitaire_3 ***")
	
	a = po.polynome()
	if visible: print(a.plat())
	
	a.inserer(mo.monome(ra.rationnel(12), "x"))
	if visible: print(a.plat())
		
	a.inserer(mo.monome(ra.rationnel(1), "y"))
	if visible: print(a.plat())
		
	a.inserer(mo.monome(ra.rationnel(1), "a"))
	if visible: print(a.plat())
	
	if visible: print("---")
	
	b = po.polynome()
	for t in a.iterateur():
		b.inserer(t)
	
	if visible: print(b.plat())

	ok = (a.nombre_monomes() == 3)
	return ok



def test_unitaire_4(visible =False):
	print("*** polynome: test_unitaire_4 ***")
				
	a = po.polynome()
	if visible: print(a.plat())
	
	a.inserer(mo.monome(ra.rationnel(12), "x"))
	if visible: print(a.plat())
		
	a.inserer(mo.monome(ra.rationnel(1), "y"))
	if visible: print(a.plat())
		
	a.inserer(mo.monome(ra.rationnel(1), "a"))
	if visible: print(a.plat())

	a = a.joindre(mo.monome(ra.rationnel(100), "t"))
	if visible: print(a.plat())
	
	ok = (a.debut().lire_monome().lire_coeff() == ra.rationnel(1)) and \
		(a.nombre_monomes() == 4)
	return ok



def test_unitaire_5(visible =False):
	print("*** polynome: test_unitaire_5 ***")
	
	a = po.polynome()
	if visible: print(a.plat())
	
	a = a.joindre(mo.monome(ra.rationnel(12), "x"))
	if visible: print(a.plat())
		
	a = a.joindre(mo.monome(ra.rationnel(1), "y"))
	if visible: print(a.plat())
	
	a = a.joindre(mo.monome(ra.rationnel(-12), "x"))
	if visible: print(a.plat())

	a = a.joindre(mo.monome(ra.rationnel(100), "t"))
	if visible: print(a.plat())
	
#	ok = (a.debut().lire_monome().lire_coeff().est_un())
#		(a.nombre_monomes() == 2)
	ok = (a.nombre_monomes() == 2) and \
		(a.debut().lire_monome().lire_coeff().lire_num().lire_valeur() == 100)
	return ok



def test_unitaire_6(visible =False):
	print("*** polynome: test_unitaire_6 ***")
	
	a = po.polynome()
	if visible: print(a.plat())
	
	a = a.joindre(mo.monome(ra.rationnel(12), "x"))
	if visible: print(a.plat())
		
	a = a.joindre(mo.monome(ra.rationnel(1), "y"))
	if visible: print(a.plat())
	
	a = a.joindre(mo.monome(ra.rationnel(), "y"))
	if visible: print(a.plat())

	a = a.joindre(mo.monome(ra.rationnel(-1), "y"))
	if visible: print(a.plat())

	a = a.joindre(mo.monome(ra.rationnel(100), "t"))
	if visible: print(a.plat())
	
	ok = (a.nombre_monomes() == 2) and \
		(a.debut().lire_monome().lire_coeff().lire_num().lire_valeur() == 100)
	return ok



def test_unitaire_7(visible =False):
	print("*** polynome: test_unitaire_7 ***")
	
	a = po.polynome()
	if visible: print(a.plat())
	
	a = a.joindre(mo.monome(ra.rationnel(12), "x"))
	if visible: print(a.plat())
		
	a = a.joindre(mo.monome(ra.rationnel(1), "y"))
	if visible: print(a.plat())
	
	a = a.joindre(mo.monome(ra.rationnel(5), "x"))
	if visible: print(a.plat())

	a = a.joindre(mo.monome(ra.rationnel(100), "t"))
	if visible: print(a.plat())
	
	ok = a.contient(mo.monome(ra.rationnel(1), "x"))
	return ok



def test_unitaire_8(visible =False):
	print("*** polynome: test_unitaire_8 ***")
	
	a = po.polynome()
	if visible: print(a.plat())
	
	a = a.joindre(mo.monome(ra.rationnel(12), "x"))
	if visible: print(a.plat())
		
	a = a.joindre(mo.monome(ra.rationnel(1), "y"))
	if visible: print(a.plat())
	
	a = a.joindre(mo.monome(ra.rationnel(5), "x"))
	if visible: print(a.plat())

	a = a.joindre(mo.monome(ra.rationnel(100), "t"))
	if visible: print(a.plat())
	
	a = a.joindre(mo.monome(ra.rationnel(-12), "x"))
	if visible: print(a.plat())
		
	a = a.joindre(mo.monome(ra.rationnel(-1), "y"))
	if visible: print(a.plat())
	
	a = a.joindre(mo.monome(ra.rationnel(-5), "x"))
	if visible: print(a.plat())

	a = a.joindre(mo.monome(ra.rationnel(-100), "t"))
	if visible: print(a.plat())
	
	a = a.joindre(mo.monome(ra.rationnel(0), "t"))
	if visible: print(a.plat())
	
	a = a.joindre(mo.monome(ra.rationnel(3, -30), "xx"))
	if visible: print(a.plat())
	
	ok = (a.nombre_monomes() == 1) and \
		(a.debut().lire_monome().lire_coeff() == ra.rationnel(-1, 10))
	return ok



def test_unitaire_9(visible =False):
	print("*** polynome: test_unitaire_9 ***")
	
	p = po.polynome()
	if visible: print(p)
	
	p = p.joindre(mo.monome(ra.rationnel(2), "x"))
	if visible: print(p)
	
	p = p.joindre(mo.monome(ra.rationnel(-2,3), "x"))
	if visible: print(p)
	
	ok = (p.nombre_monomes() == 1) and \
		(p.lire_monome().lire_coeff() == ra.rationnel(4, 3)) and \
		(p.lire_monome().lire_indet() == "x")
	return ok



def test_unitaire_10(visible =False):
	print("*** polynome: test_unitaire_10 ***")
	
	p = po.polynome()
	p = p.joindre(mo.monome(ra.rationnel(2), "x"))
	p = p.joindre(mo.monome(ra.rationnel(1), "y"))
	p = p.joindre(mo.monome(ra.rationnel(2), "x"))
	p = p.joindre(mo.monome(ra.rationnel(-3), "y"))
	
	if visible: print(p)
	
	v1 = p.fin().lire_monome().lire_coeff().lire_num().lire_valeur()
	v2 = p.debut().lire_monome().lire_coeff().lire_num().lire_valeur()
	
	ok = (v1 == -2) and (v2 == 4)
	return ok



def test_unitaire_11(visible =False):
	print("*** polynome: test_unitaire_11 ***")
	
	p = po.polynome()
	p = p.joindre(mo.monome(ra.rationnel(2), "x"))
	p = p.joindre(mo.monome(ra.rationnel(1), "y"))

	if visible: print(p)

	q = po.polynome()
	q = q.joindre(mo.monome(ra.rationnel(-5), "a"))
	q = q.joindre(mo.monome(ra.rationnel(10), "y"))
	
	if visible: print(q)
	
	r = p + q
	
	if visible: print(r)
	
	ok = (r.valuation().lire_num().lire_valeur() == 11)
	return ok



def test_unitaire_12(visible =False):
	print("*** polynome: test_unitaire_12 ***")
	
	p = po.polynome()
	p = p.joindre(mo.monome(ra.rationnel(2), "x"))
	p = p.joindre(mo.monome(ra.rationnel(1), "y"))

	if visible:
		print(p)
		print(-p)
		
	q = po.polynome()
	q = q.joindre(mo.monome(ra.rationnel(-5), "a"))
	q = q.joindre(mo.monome(ra.rationnel(10), "y"))
	
	if visible: print(q)
	
	r = p - q
	
	if visible: print(r)

	ok = (r.valuation().lire_num().lire_valeur() == -9)
	return ok



def test_unitaire_13(visible =False):
	print("*** polynome: test_unitaire_13 ***")
	
	p = po.polynome(mo.monome(ra.rationnel(20, -30), "xax"))
	if visible: print(p)

	p = p.joindre(mo.monome(ra.rationnel(1), "x"))
	if visible: print(p)
	
	p = p.joindre(mo.monome(ra.rationnel(1), "a"))
	if visible: print(p)
	
	p = p.joindre(mo.monome(ra.rationnel(-1), "x"))
	if visible: print(p)

	ok = (p.degre() == 3) and (p.valuation() == ra.rationnel(1))
	return ok



def test_unitaire_14(visible =False):
	print("*** polynome: test_unitaire_14 ***")
	
	p = po.polynome_nul()
	if visible: print("Polynome nul:", p)

	ok1 = p.valuation().est_zero()
	
	p = po.polynome_un()
	if visible: print("Polynome unite:", p)
	ok2 = p.valuation().est_un()

	p = po.polynome_err()
	if visible: print("Polynome erreur:", p)
	ok3 = not p.est_valide()
	
	ok = ok1 and ok2 and ok3
	return ok



def test_unitaire_15(visible =False):
	print("*** polynome: test_unitaire_15 ***")
	
	p = po.polynome()
	p = p.joindre(mo.monome(ra.rationnel(2), "x"))
	p = p.joindre(mo.monome(ra.rationnel(1), "y"))

	if visible: print(p)

	q = po.polynome()
	q = q.joindre(mo.monome(ra.rationnel(-5), "a"))
	q = q.joindre(mo.monome(ra.rationnel(10), "y"))
	
	if visible: print(q)
	
	r = p * q
	
	if visible: print(r)
	
	ok = (r.valuation() == ra.rationnel(10))
	return ok



def test_unitaire_16(visible =False):
	print("*** polynome: test_unitaire_16 ***")
	
	p = po.polynome(mo.monome(ra.rationnel(-5, 2), "a"))
	if visible: print(p)

	p = p.joindre(mo.monome(ra.rationnel(15, 4)))
	if visible: print(p)

	p = p.joindre(mo.monome(ra.rationnel(5), "x"))
	if visible: print(p)
	
	if visible: print(p.valuation())
	
	ok = (p.valuation() == ra.rationnel(15, 4))
	return ok



def test_unitaire_17(visible =False):
	print("*** polynome: test_unitaire_17 ***")
	
	p = po.polynome()
	p = p.joindre(mo.monome(ra.rationnel(2, 3), "a"))
	p = p.joindre(mo.monome(ra.rationnel(1), "b"))

	if visible: print(p)

	q = po.polynome()
	q = q.joindre(mo.monome(ra.rationnel(2, 3), "a"))
	q = q.joindre(mo.monome(ra.rationnel(1), "b"))
	
	if visible: print(q)
	
	r = p * q
	
	if visible: print(r)
	
	if visible: print(r.valuation())

	ok = (r.valuation() == ra.rationnel(1))
	return ok



def test_unitaire_18(visible =False):
	print("*** polynome: test_unitaire_18 ***")
	
	p = po.polynome()
	p = p.joindre(mo.monome(ra.rationnel(2), "x"))
	p = p.joindre(mo.monome(ra.rationnel(-1)))

	if visible: print(p)

	q = po.polynome()
	q = q.joindre(mo.monome(ra.rationnel(2), "x"))
	q = q.joindre(mo.monome(ra.rationnel(1)))
	
	if visible: print(q)
	
	r = p * q
	
	if visible: print(r)
	
	if visible: print(r.valuation())

	ok = (r.valuation() == ra.rationnel(-1))
	return ok



def test_unitaire_19(visible =False):
	print("*** polynome: test_unitaire_19 ***")
	
	p = po.polynome()
	
	p = p.joindre(mo.monome(ra.rationnel(5, 7)))
	
	if visible:
		print(p)
		print(p.degre())
		print(p.valuation())
	
	ok = (p.degre() == 0) and (p.valuation() == ra.rationnel(5, 7))
	return ok



def test_unitaire_20(visible =False):
	print("*** polynome: test_unitaire_20 ***")
	
	p = po.polynome()
	
	p = p.joindre(mo.monome(ra.rationnel(2, 3), "xxxx"))
	p = p.joindre(mo.monome(ra.rationnel(1), "xxxyyy"))
	p = p.joindre(mo.monome(ra.rationnel(5, 3)))
	p = p.joindre(mo.monome(ra.rationnel(-5, 2), "a"))
	
	if visible:
		print(p)
		print(p.degre())
		print(p.valuation())
	
	ok = (p.degre() == 6) and (p.valuation() == ra.rationnel(5, 3))
	return ok



def test_unitaire_21(visible =False):
	print("*** polynome: test_unitaire_21 ***")
	
	a = po.polynome(mo.monome(ra.rationnel(1), "x"))
	a = a.joindre(mo.monome(ra.rationnel(1), ""))
	if visible: print(a)
	
	b = po.polynome(mo.monome(ra.rationnel(1), "x"))
	b = b.joindre(mo.monome(ra.rationnel(3)))
	if visible: print(b)
	
	ok = (b.valuation() == ra.rationnel(3))
	return ok



def test_unitaire_22(visible =False):
	print("*** polynome: test_unitaire_22 ***")
	
	a = po.polynome(mo.monome(ra.rationnel(1), "x"))
	a = a.joindre(mo.monome(ra.rationnel(1)))
	if visible: print(a)
	
	b = po.polynome(mo.monome(ra.rationnel(1), "x"))
	b = b.joindre(mo.monome(ra.rationnel(3)))
	if visible: print(b)
	
	c = po.polynome(mo.monome(ra.rationnel(-1), "xx"))
	if visible: print(c)
	
	d = po.polynome(mo.monome(ra.rationnel(1)))
	if visible: print(d)
	
	r = (a*d)
	if visible: print(r)
	
	r = (b*c)
	if visible: print(r)

	r = (a*d + b*c)
	if visible: print(r)
	
	r = (b * d)
	if visible: print(r)
	
	ok = (r.valuation() == ra.rationnel(3))
	return ok



def test_unitaire_23(visible =False):
	print("*** polynome: test_unitaire_23 ***")
	
	p = po.polynome()
	p = p.joindre(mo.monome(ra.rationnel(1), "x"))
	p = p.joindre(mo.monome(ra.rationnel(1)))

	if visible: print(p)

	q = po.polynome()
	q = q.joindre(mo.monome(ra.rationnel(1), "x"))
	q = q.joindre(mo.monome(ra.rationnel(3)))
	
	if visible: print(q)
	
	r = p * q
	
	if visible:
		print(r)
		print(repr(r))
	
	ok = (r.degre() == 2)
	return ok



def test_unitaire_24(visible =False):
	print("*** polynome: test_unitaire_24 ***")
	
	p = po.polynome()
	ok1 = p.est_polynome_nul()	
	
	p = p.joindre(mo.monome(ra.rationnel(8, -2)))
	ok2 = p.est_degre_nul()
	
	ok = ok1 and ok2
	return ok



def test_unitaire_25(visible =False):
	print("*** polynome: test_unitaire_25 ***")
	
	a = po.polynome(mo.monome(ra.rationnel(1), "a"))
	a = a.joindre(mo.monome(ra.rationnel(1), "b"))
	if visible: print(a)
	
	b = po.polynome(mo.monome(ra.rationnel(7)))
	if visible: print(b)
		
	r = a ** b
	if visible: print(r)
	
	ok = (r.valuation() == ra.rationnel(1))
	return ok



def test_unitaire_26(visible =False):
	print("*** polynome: test_unitaire_26 ***")
	
	a = po.polynome(mo.monome(ra.rationnel(1), "a"))
	a = a.joindre(mo.monome(ra.rationnel(1), "b"))
	if visible: print(a)
			
	r = a ** 3
	if visible: print(r)
	
	ok = (r.valuation() == ra.rationnel(1))
	
	return ok



def test_unitaire_27(visible =False):
	print("*** polynome: test_unitaire_27 ***")
	
	a = po.polynome(mo.monome(ra.rationnel(1), "a"))
	a = a.joindre(mo.monome(ra.rationnel(1), "b"))
	a = a.joindre(mo.monome(ra.rationnel(-2, 3)))
	if visible: print(a)
	
	b = po.polynome(mo.monome(ra.rationnel(7)))
	if visible: print(b)
		
	r = a ** b
	
	t = r.liste_decroissante_monomes()
	c = t[-1].lire_coeff()
	
	if visible:
		print(r)
		
		print(t)
		print(c)
		
		print(r.pgcd_numerateurs())
		print(r.ppcm_denominateurs())
		
	ok = (c == ra.rationnel(-128, 2187))
	return ok



def test_unitaire_28(visible =False):
	print("*** polynome: test_unitaire_28 ***")
	
	a = po.polynome(mo.monome(ra.rationnel(1), "x"))
	a = a.joindre(mo.monome(ra.rationnel(-2, 3)))
#	if visible: print(a)
	
	b = po.polynome(mo.monome(ra.rationnel(4)))
#	if visible: print(b)
		
	r = a ** b
	
	pgcd = r.pgcd_numerateurs()
	ppcm = r.ppcm_denominateurs()
	
	if visible:
		print(r)
		
		print(pgcd)
		print(ppcm)
		
	ok = (pgcd == 1) and (ppcm == 19683)
	return ok



def test_unitaire_29(visible =False):
	print("*** polynome: test_unitaire_29 ***")
	
	a = po.polynome(mo.monome(ra.rationnel(1), "a"))
	a = a.joindre(mo.monome(ra.rationnel(1), "b"))
	if visible: print(a)
			
	r = a ** 3
	if visible: print(r.joli())
	
	ok = (r.valuation() == ra.rationnel(1))
	return ok



def test_unitaire_30(visible =False):
	print("*** polynome: test_unitaire_30 ***")
	
	ok = True
	return ok



def test_unitaire_31(visible =False):
	print("*** polynome: test_unitaire_31 ***")
	
	ok = True
	return ok



def test_unitaire_32(visible =False):
	print("*** polynome: test_unitaire_32 ***")
	
	ok = True
	return ok



def test_unitaire_33(visible =False):
	print("*** polynome: test_unitaire_33 ***")
	
	ok = True
	return ok



def test_unitaire_34(visible =False):
	print("*** polynome: test_unitaire_34 ***")
	
	ok = True
	return ok



def test_unitaire_35(visible =False):
	print("*** polynome: test_unitaire_35 ***")
	
	ok = True
	return ok



def test_unitaire_(visible =False):
	print("*** polynome: test_unitaire_ ***")
	
	ok = True
	return ok



def tests_unitaires():
	return (
		test_unitaire_0() and \
		test_unitaire_1() and \
		test_unitaire_2() and \
		test_unitaire_3() and \
		test_unitaire_4() and \
		test_unitaire_5() and \
		test_unitaire_6() and \
		test_unitaire_7() and \
		test_unitaire_8() and \
		test_unitaire_9() and \
		
		test_unitaire_10() and \
		test_unitaire_11() and \
		test_unitaire_12() and \
		test_unitaire_13() and \
		test_unitaire_14() and \
		test_unitaire_15() and \
		test_unitaire_16() and \
		test_unitaire_17() and \
		test_unitaire_18() and \
		test_unitaire_19() and \
		
		test_unitaire_20() and \
		test_unitaire_21() and \
		test_unitaire_22() and \
		test_unitaire_23() and \
		test_unitaire_24() and \
		test_unitaire_25() and \
		test_unitaire_26() and \
		test_unitaire_27() and \
		test_unitaire_28() and \
		test_unitaire_29(True) and \
		
		test_unitaire_30() and \
		test_unitaire_31() and \
		test_unitaire_32() and \
		test_unitaire_33() and \
		test_unitaire_34() and \
		test_unitaire_35
	)
	
	
	
if __name__ == "__main__":
	ok = tests_unitaires()
	if ok:
		print("*** polynome: tests unitaires OK ***")

