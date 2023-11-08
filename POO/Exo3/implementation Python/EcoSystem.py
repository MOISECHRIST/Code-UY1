from random import randrange
class Entity:
	def __init__(self,TypeEntity,Position,LifeTime):
		self._TypeEntity=TypeEntity
		self.Position=Position
		self._LifeTime=LifeTime
		self._Age=1
		self.isDead=False
	def getAge(self):
		return self._Age
	def AgeUp(self,listCat):
		if(self._Age<self._LifeTime):
			self._Age+=1
		else:
			self.isDead=True
			self.moveEntity(0)
			if(listCat.nb>0):
				listCat.nb-=1
	def getType(self):
		return self._TypeEntity
	def moveEntity(self,Position):
		self.Position=Position
class ListEntity:
	def __init__(self):
		self.tab=[]
		self.nb=0
	def AddEntity(self,elt):
		self.tab+=[elt]
		self.nb+=1
class Cat(Entity):
	def __init__(self,Id,Sex,Health,TypeEntity,Position,LifeTime):
		self.Id=Id
		self.__Sex=Sex
		self.__Health=Health
		self.HealthMax=15
		Entity.__init__(self,TypeEntity,Position,LifeTime)
		self.MouseEaten=[]
		self.nbMouseEaten=0
	def getSex(self):
		return self.__Sex
	def getHealth(self):
		return self.__Health
	def HealthUp(self):
		if(self.__Health<self.HealthMax):
			self.__Health+=1
	def HealthDown(self,listCat):
		if(self.__Health>1):
			self.__Health-=1
		else:
			self.__Health-=1
			self.moveEntity(0)
			if(listCat.nb>0):
				listCat.nb-=1
	def reproduce(self,listCat):
		if(listCat.nb<5):
			pos1=randrange(25)+1
			pos2=randrange(25)+1
			cat=Cat(listCat.nb,"Male",10,"Cat",pos1,20)
			listCat.nb+=1
			listCat.tab+=[cat]
			cat=Cat(listCat.nb,"Female",10,"Cat",pos2,20)
			listCat.nb+=1
			listCat.tab+=[cat]
	def EatMouse(self,mouse):
		self.nbMouseEaten+=1
		self.MouseEaten+=[mouse]
		self.HealthUp()
	def killMouse(self,mouse):
		mouse.isDead=True
		mouse.moveEntity(0)
		if(self.__Health<self.HealthMax):
			self.EatMouse(mouse)
class Mouse(Entity):
	def __init__(self,Id,Sex,Health,TypeEntity,Position,LifeTime):
		self.Id=Id
		self.__Sex=Sex
		self.__Health=Health
		self.HealthMax=10
		Entity.__init__(self,TypeEntity,Position,LifeTime)
		self.MaizeEaten=[]
		self.nbMaizeEaten=0
	def getSex(self):
		return self.__Sex
	def getHealth(self):
		return self.__Health
	def HealthUp(self):
		if(self.__Health<self.HealthMax):
			self.__Health+=1
	def HealthDown(self,listMouse):
		if(self.__Health>1):
			self.__Health-=1
		else:
			self.__Health-=1
			self.moveEntity(0)
			if(listMouse.nb>0):
				listMouse.nb-=1
	def reproduce(self,listMouse):
		if(listMouse.nb<10):
			pos1=randrange(25)+1
			pos2=randrange(25)+1
			mouse=Mouse(listMouse.nb,"Male",5,"Mouse",pos1,15)
			listMouse.nb+=1
			listMouse.tab+=[mouse]
			mouse=Mouse(listMouse.nb,"Female",5,"Mouse",pos2,15)
			listMouse.nb+=1
			listMouse.tab+=[mouse]
	def EatMaize(self,maize):
		maize.isDead=True
		maize.moveEntity(0)
		self.MaizeEaten+=[maize]
		self.HealthUp()
		self.nbMaizeEaten+=1
class Maize(Entity):
	def __init__(self,Id,TypeEntity,Position,LifeTime):
		self.Id=Id
		self.__Qty=7
		Entity.__init__(self,TypeEntity,Position,LifeTime)
	def getQty(self):
		return self.__Qty
	def QtyDown(self,listMaize):
		if(self.__Qty>0):
			self.__Qty-=1
		else:
			self.moveEntity(0)
			if(listMaize.nb>0):
				listMaize.nb-=1
	def appear(self,listMaize):
		if(listMaize.nb<8):
			pos=randrange(25)+1
			maize=Maize(listMaize.nb,"Maize",pos,10)
			listMaize.tab+=[maize]
			listMaize.nb+=1
