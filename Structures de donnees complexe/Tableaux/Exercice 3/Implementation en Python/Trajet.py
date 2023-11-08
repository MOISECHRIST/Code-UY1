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
class Pile:
	def __init__(self):
		self.data=None
		self.nbelt=0
	def save(self,elt):
		if self.nbelt==0:
			self.data=[elt]
			self.nbelt+=1
		else:
			self.data=[elt]+self.data
			self.nbelt+=1
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
	def print_list(self):
		if self.nbelt==0:
			print("self Vide...")
		else :
			for i in range(self.nbelt):
				elt=self.data[i]
				print("{}\t{}\t{}\t{}".format(elt.depart,elt.arrivee,elt.prix,elt.duree))
	def sort_list(self):
		for i in range(self.nbelt-1):
			mini=i
			for j in range(i+1,self.nbelt):
				if self.data[j].prix<self.data[mini].prix:
					mini=j
			self.data[i],self.data[mini]=self.data[mini],self.data[i]
	def seqSearch(self,elt):
		trouve=False
		i=0
		while(self.data[i].depart!=elt)and(i<self.nbelt):
			i+=1
		if self.data[i].depart==elt:
			trouve=True
		return trouve
pile=Pile()
pile.read()
pile.print_list()
print("\n\n")
pile.sort_list()
pile.print_list()
