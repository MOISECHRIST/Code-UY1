from random import randrange;
#Classe pour definir la structure de la date
class Date:
	#Fonction d'initialisation
	def __init__(self,jourval=None,moisval=None,anneeval=None):
		self.jour=jourval
		self.mois=moisval
		self.annee=anneeval
#Classe pour definir la structure d'un trajet 
class Trajet:
	#Fonction d'initialisation
	def __init__(self,departval=None,arriveeval=None,date=None,prixval=None,dureeval=None):
		self.depart=departval
		self.arrivee=arriveeval
		self.date=date
		self.prix=prixval
		self.duree=dureeval
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
	#Fonction pour stocker un trajet dans la pile
	def save(self,elt):
		tmp=Noeud()
		tmp.data=elt
		tmp.next=self.tete
		self.tete=tmp
	#Fonction pour stocker les serie de trajet
	def read(self):
		#1
		date=Date(randrange(1,28),randrange(1,7),2022)
		elt=Trajet("Odza","Mvan",date,300,25)
		self.save(elt)
		#2
		date=Date(randrange(1,28),randrange(1,7),2022)
		elt=Trajet("Beatitude","Ngoa Ekele",date,400,50)
		self.save(elt)
		#3
		date=Date(randrange(1,28),randrange(1,7),2022)
		elt=Trajet("Mvan","Ngoa Ekele",date,350,20)
		self.save(elt)
		#4
		date=Date(randrange(1,28),randrange(1,7),2022)
		elt=Trajet("Ekounou","Mokolo",date,250,50)
		self.save(elt)
		#5
		date=Date(randrange(1,28),randrange(1,7),2022)
		elt=Trajet("Poste","Camer",date,100,5)
		self.save(elt)
		#6
		date=Date(randrange(1,28),randrange(1,7),2022)
		elt=Trajet("Bastos","Education",date,300,50)
		self.save(elt)
	#Fonction qui retourne le nombre d'element dans la pile
	def nbelt(self):
		nb=1
		dernier=self.tete
		while(dernier.next):
			dernier=dernier.next
			nb+=1
		return nb
	#Fonction qui supprime un element de la pile a partir de son point de depart
	def supp_elt(self,depart):
		if self.tete is None:
			print("La self n'a aucun element")
		else :
			dernier=self.tete
			prec=self.tete
			i=0
			elt=dernier.data
			while (dernier.next)and(elt.depart!=depart):
				prec=dernier
				dernier=dernier.next
				elt=dernier.data
				i+=1
			if (elt.depart==depart)and(i>0):
				prec.next=dernier.next
			elif (elt.depart==depart)and(i==0):
				self.tete=dernier.next
	#Fonction qui retourne le trajet de prix minimal dans la self
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
	#Fonction qui trie la self suivant les couts des trajets
	def sort_list(self):
		new=Pile()
		while(self.tete):
			mini=self.minimum()
			self.supp_elt(mini.depart)
			new.save(mini)
		return new
	#Fonction pour rechercher un element dans la pile
	def search_elt(self,depart):
		trouve=False
		tmp=self.tete
		elt=tmp.data
		while(tmp.next)and(elt.depart!=depart):
			tmp=tmp.next
			elt=tmp.data
		if (elt.depart==depart):
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
				print("{}\t{}\t{}\t{}".format(elt.depart,elt.arrivee,elt.prix,elt.duree))
				i+=1
				tmp=tmp.next
