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
class Pile:
	#Fonction d'initialisation
	def __init__(self):
		self.tete=None
	#Fonction pour stocker un Repas dans la pile
	def save(self,elt):
		node=Noeud()
		node.data=elt
		if (self.tete is None):
			self.tete=node
		else:
			tmp=self.tete
			while(tmp.next):
				tmp=tmp.next
			tmp.next=node
	def read(self):
		x=["Masculin","Feminin"]
		y=["Maison","Ecole","Resto"]
		z=["Okok","Pate saute","Eru","Poisson","Poulet"]
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
	#Fonction pour stocker les serie de repat contenu dans le fichier foodData_to_be_structured.csv
	def read_file(self):
		elt=Repas()
		with open("foodData_to_be_structured.csv","r") as f:
			for line in f:
				x=line.split(";")
				y=x[2].split("/")
				date=Date(int(y[0]),int(y[1]),int(y[2]))
				elt.unite=x[5]
				if x[6]=="":
					nbpers=0	
				else:
					nbpers=int(x[6])		
				elt.lieu=x[7]
				elt=Repas(x[0],int(x[1]),date,x[3],x[4],x[5],x[6],nbpers)
				self.save(elt)
	#Fonction qui retourne le nombre d'element dans la pile
	def nbelt(self):
		nb=1
		dernier=self.tete
		while(dernier.next):
			dernier=dernier.next
			nb+=1
		return nb
	#Fonction qui supprime un element de la pile a partir de son age
	def supp_elt(self,age):
		if self.tete is None:
			print("La self n'a aucun element")
		else :
			dernier=self.tete
			prec=self.tete
			i=0
			elt=dernier.data
			while (dernier.next)and(elt.age!=age):
				prec=dernier
				dernier=dernier.next
				elt=dernier.data
				i+=1
			if (elt.age==age)and(i>0):
				prec.next=dernier.next
			elif (elt.age==age)and(i==0):
				self.tete=dernier.next
	#Fonction qui retourne le Repas consommé par le plus jeune
	def minimum(self):
		if self.tete is None:
			print("La self n'a aucun element")
			return None
		else:
			cour=self.tete
			mini=cour.data
			while(cour):
				elt=cour.data
				if(mini.age>elt.age):
					mini=elt
				cour=cour.next
			return mini
	#Fonction qui trie la self suivant l'age
	def sort_list(self):
		new=Pile()
		while(self.tete):
			mini=self.minimum()
			self.supp_elt(mini.age)
			new.save(mini)
		return new
	#Fonction pour rechercher un element dans la pile a partir de l'age
	def search_elt(self,r):
		trouve=False
		tmp=self.tete
		elt=tmp.data
		while(tmp.next)and(elt.repas!=r):
			tmp=tmp.next
			elt=tmp.data
		if (elt.repas==r):
			trouve=True
		return trouve
	def print_list(self):
		if self.tete is None:
			print("self Vide...")
		else :
			tmp=self.tete
			while (tmp is not None):
				elt=tmp.data
				print("{}\t{}".format(elt.repas,elt.age))
				tmp=tmp.next
