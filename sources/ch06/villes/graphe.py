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
			if a in list(self.__liste_adj.keys()):
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
		p.sort()
		return p

	def composantes(self):
		"""  """
		c = []
		for s in self.sommets():
			t = self.composante_connexe(s)
			t.sort()
			if t not in c:
				c.append(t)
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

def arret(liste, s):
	"""  """
	for item in liste:
		if item[-1] is not s:
			return False
	return True

