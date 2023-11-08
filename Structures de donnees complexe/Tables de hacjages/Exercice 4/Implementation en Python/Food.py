from random import randrange
#Classe pour definir la structure de la date
class Date:
	#Fonction d'initialisation
	def __init__(self,jourval=None,moisval=None,anneeval=None):
		self.jour=jourval
		self.mois=moisval
		self.annee=anneeval
#Classe pour definir la structure d'un Repas 
class Repas:
	#Fonction d'initialisation
	def __init__(self,sexeval=None,ageval=None,date=None,heureval=None,repasval=None,uniteval=None,lieuval=None,nbpersval=None):
		self.sexe=sexeval
		self.age=ageval
		self.date=date
		self.heure=heureval
		self.repas=repasval
		self.unite=uniteval
		self.lieu=lieuval
		self.nbpers=nbpersval
#Classe pour definir la structure d'un noeud de la pile
class Noeud:
	#Fonction d'initialisation
	def __init__(self,elt=None):
		self.data=elt
		self.next=None
#Classe pour definir la structure de la pile
class File:
	#Fonction d'initialisation
	def __init__(self):
		self.tete=None
	#Fonction pour stocker un Food dans la pile
	def save_file(self,elt):
		node=Noeud()
		node.data=elt
		if (self.tete is None):
			self.tete=node
		else:
			tmp=self.tete
			while(tmp.next):
				tmp=tmp.next
			tmp.next=node
	#Fonction qui retourne le nombre d'element dans la pile
	def nbre(self):
		nb=1
		dernier=self.tete
		while(dernier.next):
			dernier=dernier.next
			nb+=1
		return nb
	#Fonction qui supprime un element de la pile a partir de son point de repas
	def supp_elt(self,repas):
		if self.tete is None:
			print("La self n'a aucun element")
		else :
			dernier=self.tete
			prec=self.tete
			i=0
			elt=dernier.data
			while (dernier.next)and(elt.repas!=repas):
				prec=dernier
				dernier=dernier.next
				elt=dernier.data
				i+=1
			if (elt.repas==repas)and(i>0):
				prec.next=dernier.next
			elif (elt.repas==repas)and(i==0):
				self.tete=dernier.next
	#Fonction qui retourne le Food de prix minimal dans la self
	def minimum(self):
		if self.tete is None:
			print("La self n'a aucun element")
			return None
		else:
			cour=self.tete
			mini=cour.data
			while(cour):
				elt=cour.data
				if(mini.prix>elt.prix):
					mini=elt
				cour=cour.next
			return mini
	#Fonction qui trie la self suivant les couts des Foods
	def sort_list(self):
		new=File()
		while(self.tete):
			mini=self.minimum()
			self.supp_elt(mini.repas)
			new.save_file(mini)
		return new
	#Fonction pour rechercher un element dans la pile
	def search_elt(self,repas):
		trouve=False
		tmp=self.tete
		elt=tmp.data
		while(tmp.next)and(elt.repas!=repas):
			tmp=tmp.next
			elt=tmp.data
		if (elt.repas==repas):
			trouve=True
		return trouve
	def print_list(self):
		if self.tete is None:
			print("self Vide...")
		else :
			tmp=self.tete
			i=1
			while (tmp is not None):
				elt=tmp.data
				print("{}\t{}\t{}\t{}\t{}".format(elt.heure,elt.repas,elt.lieu,elt.age,elt.nbpers))
				i+=1
				tmp=tmp.next
#Classe de la tabble de hachage
class TableHash :
	def __init__(self):
		self.tab=[]
		self.nbelt=4
		for i in range(self.nbelt):
			elt=File()
			self.tab+=[elt]
	def HashFunct(self,repas):
		return len(repas)%self.nbelt
	def save(self,elt):
		n=self.HashFunct(elt.repas)
		if self.tab[n] is None:
			liste=File()
			liste.save_file(elt)
			self.tab[n]=[liste]
		else :
			self.tab[n].save_file(elt)
	def read(self):
		x=["Masculin","Feminin"]
		y=["Maison","Ecole","Resto"]
		z=["Okok","Pate saute","Eru","Poisson","Poulet","Ndole","Nhui","Sauce tomate avec le riz"]
		w=["08h-12h","12h-16h","16h-18h"]
		#1
		date=Date(randrange(1,28),randrange(1,7),2022)
		elt=Repas(x[randrange(2)],randrange(15,25),date,w[randrange(3)],z[randrange(5)],"plat",y[randrange(3)],randrange(10))
		self.save(elt)
		#2
		date=Date(randrange(1,28),randrange(1,7),2022)
		elt=Repas(x[randrange(2)],randrange(15,25),date,w[randrange(3)],z[randrange(5)],"plat",y[randrange(3)],randrange(10))
		self.save(elt)
		#3
		date=Date(randrange(1,28),randrange(1,7),2022)
		elt=Repas(x[randrange(2)],randrange(15,25),date,w[randrange(3)],z[randrange(5)],"plat",y[randrange(3)],randrange(10))
		self.save(elt)
		#4
		date=Date(randrange(1,28),randrange(1,7),2022)
		elt=Repas(x[randrange(2)],randrange(15,25),date,w[randrange(3)],z[randrange(5)],"plat",y[randrange(3)],randrange(10))
		self.save(elt)
		#5
		date=Date(randrange(1,28),randrange(1,7),2022)
		elt=Repas(x[randrange(2)],randrange(15,25),date,w[randrange(3)],z[randrange(5)],"plat",y[randrange(3)],randrange(10))
		self.save(elt)
		#6
		date=Date(randrange(1,28),randrange(1,7),2022)
		elt=Repas(x[randrange(2)],randrange(15,25),date,w[randrange(3)],z[randrange(5)],"plat",y[randrange(3)],randrange(10))
		self.save(elt)
		#7
		date=Date(randrange(1,28),randrange(1,7),2022)
		elt=Repas(x[randrange(2)],randrange(15,25),date,w[randrange(3)],z[randrange(5)],"plat",y[randrange(3)],randrange(10))
		self.save(elt)
		#8
		date=Date(randrange(1,28),randrange(1,7),2022)
		elt=Repas(x[randrange(2)],randrange(15,25),date,w[randrange(3)],z[randrange(5)],"plat",y[randrange(3)],randrange(10))
		self.save(elt)
		#9
		date=Date(randrange(1,28),randrange(1,7),2022)
		elt=Repas(x[randrange(2)],randrange(15,25),date,w[randrange(3)],z[randrange(5)],"plat",y[randrange(3)],randrange(10))
		self.save(elt)
		#10
		date=Date(randrange(1,28),randrange(1,7),2022)
		elt=Repas(x[randrange(2)],randrange(15,25),date,w[randrange(3)],z[randrange(5)],"plat",y[randrange(3)],randrange(10))
		self.save(elt)
#Programme principal
table=TableHash()
table.read()
for i in range(table.nbelt):
	print("{} :".format(i+1))
	if table.tab[i].tete is not None :
		table.tab[i].print_list()
print("\n(C) 2022 By MMCJ/INF-L1")
