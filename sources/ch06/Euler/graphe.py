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

import random



def arret(liste, s):
	"""  """
	for item in liste:
		if item[-1] is not s:
			return False
	return True



class graphe(object):

	def __init__(self, liste_adj =None):
		"""  """
		self.__liste_adj = liste_adj



	def __str__(self):
		"""  """
		return str(self.__liste_adj)



	def adjacents(self, a):
		"""  """
		if self.__liste_adj is not None:
			if a in self.__liste_adj.keys():
				return self.__liste_adj[a]
		return []



	def est_adjacent(self, a, b):
		"""  """
		return (b in self.adjacents(a))



	def liste_adjacence(self):
		"""  """
		return self.__liste_adj



	def sommets(self):
		"""  """
		if self.__liste_adj is None:
			return []
		else:
			t = list(self.__liste_adj.keys())
			t.sort()
			return t



	def nombre_sommets(self):
		"""  """
		return len(self.sommets())



	def degre(self):
		"""  """
		return len(self.__liste_adj)



	def composante_connexe(self, s):
		"""  """
		p = []
		if s in self.sommets():
			q = []
			q.append(s)
			visite = []
			visite.append(s)
			while len(q) > 0:
				x = q.pop(0)
				p.append(x)
				for t in self.adjacents(x):
					if t not in visite:
						q.append(t)
						visite.append(t)
		t=list(p)
		t.sort()
		return t



	def composantes(self):
		"""  """
		c = []
		for s in self.sommets():
			t = self.composante_connexe(s)
			u = list(t)
			u.sort()
			if u not in c:
				c.append(u)
		return c



	def liaison(self, a, b):
		"""  """
		return (b in self.composante_connexe(a))



	def chaines(self, a, b):
		"""  """
		ll = []
		ll.append([a])
		while not arret(ll, b):
			q = []
			for p in ll:
				u = p[-1]
				if u == b:
					q.append(p)
				else:
					s = self.adjacents(u)
					for t in s:
						if not (t in p):
							v = [i for i in p]
							v.append(t)
							q.append(v)
			ll = q
		return ll



	def recherche_chaines(self, a, b):
		"""  """
		p = []
		if a != b and self.liaison(a, b):
			p = self.chaines(a, b)
		return p



	def recherche_cycles(self, a):
		"""  """
		p = []

	# Pour chaque sommet s adjacent au sommet a (sauf a), rechercher les chaînes 
	# d'origine s et d'extrémité a. Pour chaque chaine trouvée, lui adjoindre 
	# a comme premier élément.

		c = self.adjacents(a)
		for s in c:
			t = self.recherche_chaines(s, a)
			for k in t:
				u = [a]
				for v in k:
					u.append(v)
				if len(u) > 3:
					p.append(u)
		return p



	def degre_sommet(self, a):
		"""  """
		deg = 0
		if self.__liste_adj is not None:
			if a in self.__liste_adj.keys():
				deg = len(self.__liste_adj[a])
		return deg



	def existence_chaine_Euler(self): # pour graphe connexe! (test à insérer)
		"""  """
		sommets_deg_impair = 0
		for s in self.sommets():
			if self.degre_sommet(s) % 2 == 1:
				sommets_deg_impair += 1
		return (sommets_deg_impair == 0 or sommets_deg_impair == 2)



	def existence_cycle_Euler(self): # pour graphe connexe! (idem)
		"""  """
		sommets_deg_impair = 0
		for s in self.sommets():
			if self.degre_sommet(s) % 2 == 1:
				sommets_deg_impair += 1
		return (sommets_deg_impair == 0)



	def nombre_aretes(self):
		"""  """
		n = 0
		for s in self.sommets():
			n += len(self.adjacents(s))
		return (n/2)



	def graphe_reduit(self, a, b):
		"""  """
		h = dict()
		for s in self.sommets():
			l = []
			for t in self.adjacents(s):
				if (s != a or t != b) and (s != b or t != a):
					l.append(t)
			if len(l) != 0:
				h[s] = l
		return graphe(h)



	def est_un_pont(self, a, b):
		"""  """
		if not (b in self.adjacents(a)):
			return False
		r = self.graphe_reduit(a, b)
		return (len(r.composantes()) != 1)



	def recherche_Euler(self):
		""" algorithme de Fleury """
		g = self
		fin = (g.nombre_aretes() == 1)
		if fin:
			return g.sommets()

		p = []

		choix = []
		for s in g.sommets():
			if g.degre_sommet(s) % 2 == 1:
				choix.append(s)
		if len(choix) == 0:
			choix = g.sommets()

		a = choix[random.randrange(0, len(choix))]

		while not fin:

			u = g.adjacents(a)
			v = []
			for s in u:
				if not g.est_un_pont(a, s):
					v.append(s)

			b = v[random.randrange(0, len(v))]

			p.append(a)
			g = g.graphe_reduit(a, b)
			a = b
			
			fin = (g.nombre_aretes() == 1)
				
		p.append(a)
		p.append(g.adjacents(a)[0])

		return p

