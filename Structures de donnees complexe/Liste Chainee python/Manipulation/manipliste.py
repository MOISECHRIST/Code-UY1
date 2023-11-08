#Classe Node pour definir un noeud de la liste chainée
class Node:
	#Fonction d'initialisation d'un noeud de liste chainée
	def __init__(liste,data):
		liste.data=data
		liste.suivant=None
#Classe listechainee pour definir la liste chainée	
class Listechainee:
	#Fonction d'initralisation de la liste
	def __init__(liste):
		liste.teteval=None
	#Fonction pour afficher la liste
	def affiche(liste):
		printval=liste.teteval
		while printval is not None:
			print(printval.data)
			printval=printval.suivant
	#Fonction pour ajouter un element en tete de liste
	def ajoutdebut(liste,dataval):
		new=Node(dataval)
		new.suivant=liste.teteval
		liste.teteval=new
	#Fonction pour ajouter un element en fin de liste
	def ajoutfin(liste,dataval):
		new=Node(dataval)
		if liste.teteval is None:
			liste.teteval=new
		else:
			dernier=liste.teteval
			while (dernier.suivant):
				dernier=dernier.suivant
			dernier.suivant=new
	#Fonction pour rechercher un element dans la liste
	def recherche(liste,depart):
		trouve=False
		if liste.teteval is None:
			print("La liste n'a aucun element")
		else :
			dernier=liste.teteval
			while (dernier.suivant)and(dernier.data!=depart):
				dernier=dernier.suivant
			if (dernier.data==depart):
				trouve=True
		return trouve
	#Fonction pour supprimer un element de la liste
	def suppelt(liste,depart):
		if liste.teteval is None:
			print("La liste n'a aucun element")
		else :
			dernier=liste.teteval
			prec=liste.teteval
			i=0
			while (dernier.suivant)and(dernier.data!=depart):
				prec=dernier
				dernier=dernier.suivant
				i+=1
			if (dernier.data==depart)and(i>0):
				prec.suivant=dernier.suivant
			elif (dernier.data==depart)and(i==0):
				liste.teteval=dernier.suivant
	#Fonction pour compter le nombre d'element dans une liste
	def nbelt(liste):
		i=1
		dernier=liste.teteval
		while(dernier.suivant):
			dernier=dernier.suivant
			i+=1
		return i
	#Fonction pour tester si la liste est vide
	def Sivide(liste):
		return liste.teteval==None
	#Fonction pour trier dans l'ordre croissant les données
	def TriCrois(liste):
		if liste.teteval is None:
			print("La liste est vide")
		else :
			new=Listechainee()
			n=liste.nbelt()
			while(n>0):
				cour=liste.teteval
				mini=cour.data
				while(cour.suivant):
					if(mini>cour.data):
						mini=cour.data
					cour=cour.suivant
				if (mini>cour.data):
					mini=cour.data
				liste.suppelt(mini)
				new.ajoutfin(mini)
				n-=1
			return new
	#Fonction pour trier dans l'ordre croissant les données
	def TriDecrois(liste):
		if liste.teteval is None:
			print("La liste est vide")
		else :
			new=Listechainee()
			n=liste.nbelt()
			while(n>0):
				cour=liste.teteval
				mini=cour.data
				while(cour.suivant):
					if(mini>cour.data):
						mini=cour.data
					cour=cour.suivant
				if (mini>cour.data):
					mini=cour.data
				liste.suppelt(mini)
				new.ajoutdebut(mini)
				n-=1
			return new
	#Fonction pour inverser les elements d'un tableau	
	def InversList(liste):
		new=Listechainee()
		cour=liste.teteval
		while (cour.suivant):
			val=cour.data
			new.ajoutdebut(val)
			cour=cour.suivant
		val=cour.data
		new.ajoutdebut(val)
		return new
