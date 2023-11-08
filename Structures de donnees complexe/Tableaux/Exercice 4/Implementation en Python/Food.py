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
	def print_list(self):
		if self.nbelt==0:
			print("self Vide...")
		else :
			for i in range(self.nbelt):
				elt=self.data[i]
				print("{}\t{}\t{}\t{}\t{}".format(elt.heure,elt.repas,elt.lieu,elt.age,elt.nbpers))
	def sort_list(self):
		for i in range(self.nbelt-1):
			mini=i
			for j in range(i+1,self.nbelt):
				if self.data[j].age<self.data[mini].age:
					mini=j
			self.data[i],self.data[mini]=self.data[mini],self.data[i]
	def seqSearch(self,elt):
		trouve=False
		i=0
		while(self.data[i].repas!=elt)and(i<self.nbelt):
			i+=1
		if self.data[i].repas==elt:
			trouve=True
		return trouve
pile=Pile()
pile.read()
pile.print_list()
print("\n\n")
pile.sort_list()
pile.print_list()
