class Plat:
	def __init__(self,IdPlat,NomPlat,DescriptionPlat,TypePlat,ListeIngredient,SourcePlat,RecettePlat):
		self.__mIdPlat=IdPlat
		self.__mNomPlat=NomPlat
		self.mDescriptionPlat=DescriptionPlat
		self.__mTypePlat=TypePlat
		self.mListeIngredient=ListeIngredient
		self.mSourcePlat=SourcePlat
		self.mRecettePlat=RecettePlat
		self.tabAlPrin=[]
		self.nbAlPrin=0
		self.tabAlProt=[]
		self.nbAlProt=0
		self.tabCompl=[]
		self.nbCompl=0
		self.tabEpices=[]
		self.nbEpices=0
		
	def setNomPlat(self,NomPlat):
		self.__mNomPlat=NomPlat
	def setTypePlat(self,TypePlat):
		self.__mTypePlat=TypePlat
	def getNomPlat(self):
		return self.__mNomPlat
	def getTypePlat(self):
		return self.__mTypePlat
	def ajouterAlPrin(self,AlPrin):
		self.tabAlPrin+=[AlPrin]
		self.nbAlPrin+=1
	def ajouterAlProt(self,AlProt):
		self.tabAlProt+=[AlProt]
		self.nbAlProt+=1
	def ajouterCompl(self,Compl):
		self.tabCompl+=[Compl]
		self.nbCompl+=1
	def ajouterEpices(self,epices):
		self.tabEpices+=[epices]
		self.nbEpices+=1

class Epices:
	def __init__(self,NomEpice):
		self.__mNomEpice=NomEpice
	def AfficherEpice(self):
		return self.__mNomEpice

class Complement:
	def __init__(self, NomComplement, QteComplement, CouleurComplement):
		self.__mNomComplement=NomComplement
		self.__mQteComplement=QteComplement
		self.__mCouleurComplement=CouleurComplement
	def AfficherNomComplement(self):
		return self.__mNomComplement
	def AfficherQteComplement(self):
		return self.__mQteComplement
	def AfficherCouleurComplement(self):
		return self.__mCouleurComplement

class AlimentProteine:
	def __init__(self,NomProteine, QteProteine, MethodeCuissonProteine, TypeProteine):
		self.__mNomProteine=NomProteine;
		self.__mQteProteine=QteProteine;
		self.__mMethodeCuissonProteine=MethodeCuissonProteine;
		self.__mTypeProteine=TypeProteine;
	def AfficherNomProteine(self):
		return self.__mNomProteine
	def AfficherQteProteine(self):
		return self.__mQteProteine
	def AfficherTypeProteine(self):
		return self.__mTypeProteine
	def AfficherMethodeCuissonProteine(self):
		return self.mMethodeCuissonProteine

class AlimentPrincipal:
	def __init__(self,NomAliment,TextureAliment,CouleurAliment):
		self.__mNomAliment=NomAliment
		self.__mTextureAliment=TextureAliment
		self.__mCouleurAliment=CouleurAliment
	def AfficherNomAliment(self):
		return self.__mNomAliment
	def ModifierNomAliment(self,NomAliment):
		self.__mNomAliment=NomAliment
	def AfficherTextureAliment(self):
		return self.__mTextureAliment
	def AfficherCouleurAliment(self):
		return self.__mCouleurAliment
