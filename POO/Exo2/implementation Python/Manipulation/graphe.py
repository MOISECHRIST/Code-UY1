#Definition du noeud Habitudes alimentaires
class FoodHabit:#Classe utilisee pour stocker les données sur les habitudes alimentaires
	def __init__(self,date,foodEaten,nbFoodEaten,QtyWater,OtherLiquid,FruitEaten,nbBowel,day):
		self.__date=date
		self.__foodEaten=foodEaten
		self.__nbFoodEaten=nbFoodEaten
		self.__QtyWater=QtyWater
		self.__OtherLiquid=OtherLiquid
		self.__FruitEaten=FruitEaten
		self.__nbBowel=nbBowel
		self.day=day
	def getFoodEaten(self):
		return self.__foodEaten
class NodeFoodHabit:#Class utilisee pour creer les noeuds d'habitudes alimentaires
	def __init__(self,elt=None):
		self.data=elt
		self.NextFoodHabit=None
		self.Problem=None
	def AddHealthProblem(self,elt):
		self.Problem=elt
class Graph:
	def __init__(self):
		self.head=None
	def Save(self,elt):
		if self.head is None:
			self.head=elt
		else:
			cur=self.head
			while(cur.NextFoodHabit):
				cur=cur.NextFoodHabit
			cur.NextFoodHabit=elt
#Definition du noeud probleme de sante
class NodeHealthPB:
	def __init__(self,HealthPB):
		self.__HealthPB=HealthPB
		self.NextProblem=None
	def getHealthPB(self):
		return self.__HealthPB
class ListHealthPB:
	def __init__(self):
		self.head=None
	def SaveHealthPB(self,elt):
		if self.head is None:
			self.head=elt
		else:
			cur=self.head
			while((cur.NextProblem)and(cur.getHealthPB() != elt.getHealthPB())):
				cur=cur.NextProblem
			if(cur.getHealthPB() != elt.getHealthPB()):
				cur.NextProblem=elt
#Classes Manipulées par l'algorithme de prediction
class lineTCD:
	def __init__(self):
		self.FoodEaten=""
		self.nbEaten=0
		self.nbHPB=0
		self.maxEaten=10
class TCD:
	def __init__(self):
		self.head=[]
		self.nb=0
