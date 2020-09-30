class Polynome(object):
	def __init__(self, coefficients):
		self.coeffs = coefficients

	#methode renvoyant le degre du polynome
	def deg(self):
		n = len(self.coeffs)
		for i, c in enumerate(reversed(self.coeffs)):
			if c != 0:
				return n-1-i
		return -1

	#methode basee sur la methode par defaut __add__()
	#permettant d'additioner deux polynomes
	#on surcharge la methode __add__() par defaut
	def __add__(self, other):
		if self.deg() < other.deg():
			self, other = other, self
		tmp = other.coeffs + [0]*(self.deg() - other.deg())
		return Polynome([x+y for x, y in zip(self.coeffs, tmp)])

	#on souhaite changer le mode d'affichage des resultats d'operations
	#surcharge de la methode __str__() par defaut
	def str_monome(self, i, c):
		coeffs = '{}'.format(c) if c >= 0 else '({})'.format(c)
		indet = ('.X^{}'.format(i) if i > 1
				 else ('.X' if i == 1 else ''))
		return ''.join([coeffs, indet])

	def __str__(self):
		chaine = ' + '.join(self.str_monome(i, c)
				for i, c in enumerate(self.coeffs) if c != 0)
		chaine = chaine.replace(' 1.', ' ')
		return chaine if chaine != '' else '0'

	#evaluation d'un polynome en un point
	#methode de HORNER
	def __call__(self, x):
		somme = 0
		for c in reversed(self.coeffs):
			somme = c + x*somme
		return somme

	#produit de polynomes
	#commencons par definir au prealable une fonction qui calcule le produit d'un polynome
	#par un monome de la forme cX^i
	def mul_monome(self, i, c):
		return Polynome([0]*i + [c * x for x in self.coeffs])

	def __mul__(self, other):
		tmp = Polynome([0])
		for i, c in enumerate(other.coeffs):
			tmp += self.mul_monome(i, c)
		return tmp

#definition d'une classe derivee de la classe polynome
#cette classe beneficiera des methodes programmees lors de la construction de la classe parente
class FracRationnelle(Polynome):
	def __init__(self, numerateur, denominateur):
		self.numer = numerateur
		self.denom = denominateur

	def deg(self):
		return self.numer.deg() - self.denom.deg()

	def __call__(self, x):
		return self.numer.__call__(x) / self.denom.__call__(x)

	def __str__(self):
		return('({}) / ({})'.format(self.numer, self.denom))

	def __add__(self, other):
		numer = self.numer * other.denom + self.denom * other.numer
		denom = self.denom * other.denom
		return FracRationnelle(numer, denom)

	def __mul__(self, other):
		numer = self.numer * other.numer
		denom = self.denom * other.denom
		return FracRationnelle(numer, denom)

#amelioration de la classe des fractions rationnelles par heritage multiple
#cette classe herite de la classe des polynomes et d'une nouvelle classe de rationnels definie ci-apres
class Rationnel(object):
	def __init__(self, num, den):
		self.numer = num
		self.denom = den

	def __str__(self):
		return('({}) / ({})'.format(self.numer, self.denom))

	def __add__(self, other):
		denom = self.denom * other.denom
		numer = self.numer * other.denom + other.numer * self.denom
		return Rationnel(numer, denom)

	def __mul__(self, other):
		numer = self.numer * other.numer
		denom = self.denom * other.denom
		return Rationnel(numer, denom)

class FracRationnelle(Rationnel, Polynome):
	def __init__(self, numerateur, denominateur):
		self.numer = numerateur
		self.denom = denominateur

	def deg(self):
		return self.numer.deg() - self.denom.deg()

	def __call__(self, x):
		return self.numer.__call__(x) / self.denom.__call__(x)

	def __add__(self, other):
		tmp = (Rationnel(self.numer, self.denom)
			    + Rationnel(other.numer, other.denom))
		return FracRationnelle(tmp.numer, tmp.denom)

	def __mul__(self, other):
		tmp = (Rationnel(self.numer, self.denom)
			    * Rationnel(other.numer, other.denom))
		return FracRationnelle(tmp.numer, tmp.denom)






