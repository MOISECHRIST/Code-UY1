from Manipulation.graphe import *
#Read data file
def ReadFile(DataSet):
	graph=Graph()
	listHPB=ListHealthPB()
	with open(DataSet,"r") as f:
		for line in f:
			x=line.split(",")
			if x[2]=="":
				x[2]=0
			if x[3]=="":
				x[3]=0
			if x[4]=="":
				x[4]=0
			if x[6]=="":
				x[6]=0
			elt1=FoodHabit(x[0],x[1],int(x[2]),float(x[3]),float(x[4]),x[5],int(x[6]),x[7])
			node=NodeFoodHabit(elt1)
			elt2=NodeHealthPB(x[8])
			listHPB.SaveHealthPB(elt2)
			cur=listHPB.head
			while(cur.getHealthPB() != elt2.getHealthPB()):
				cur=cur.NextProblem
			node.AddHealthProblem(cur)
			graph.Save(node)
	return graph
#Graph Tranversal Program
def GraphTransversal(graph):
	cur = graph.head
	while (cur):
		print("{}: {}---->{}".format(cur.data.day,cur.data.getFoodEaten(),cur.Problem.getHealthPB()))
		cur=cur.NextFoodHabit
#Read graph for prediction
def ReadGraph(graph):
	cur = graph.head
	table=[]
	for i in range(7):
		table+=[{}]
	while (cur):
		if cur.data.day=="lundi":
			i=0
		elif cur.data.day=="mardi":
			i=1
		elif cur.data.day=="mercredi":
			i=2
		elif cur.data.day=="jeudi":
			i=3
		elif cur.data.day=="vendredi":
			i=4
		elif cur.data.day=="samedi":
			i=5
		elif cur.data.day=="dimanche":
			i=6
		if(cur.data.getFoodEaten() in table[i].keys()):
			table[i][cur.data.getFoodEaten()]+=1
		else:
			table[i][cur.data.getFoodEaten()]=1
		cur=cur.NextFoodHabit
	return table
#algorithm that can be used to predict the food that you’ll eat
def predictProgram(graph):
	total=0
	day=input("Entrer votre jour \n[0=Lundi, 1=Mardi, 2=Mercredi, 3=Jeudi, 4=Vendredi, 5=Samedi et 6=Dimanche] :")
	try :
		day=int(day)
	except ValueError:
		print("Erreur de saisie")
		day=input("Entrer votre jour \n[0=Lundi, 1=Mardi, 2=Mercredi, 3=Jeudi, 4=Vendredi, 5=Samedi et 6=Dimanche] :")
		day=int(day)
	while((day<0)and(day>6)):
		print("Erreur de saisie")
		day=input("Entrer votre jour \n[0=Lundi, 1=Mardi, 2=Mercredi, 3=Jeudi, 4=Vendredi, 5=Samedi et 6=Dimanche] :")
		try :
			day=int(day)
		except :
			print("Erreur de saisie")
			day=input("Entrer votre jour \n[0=Lundi, 1=Mardi, 2=Mercredi, 3=Jeudi, 4=Vendredi, 5=Samedi et 6=Dimanche] :")
			day=int(day)
	if day==0:
		i="lundi"
	elif day==1:
		i="mardi"
	elif day==2:
		i="mercredi"
	elif day==3:
		i="jeudi"
	elif day==4:
		i="vendredi"
	elif day==5:
		i="samedi"
	elif day==6:
		i="dimanche"
	table=ReadGraph(graph)
	for Key in table[day].keys():
		if table[day][Key]==max(table[day].values()):
			maxKey=Key
		total+=table[day][Key]
	proba=table[day][maxKey]*100/total
	print("Vous avez {}% de chance de manger le plat {} le {}".format(round(proba,2),maxKey,i))
#Fill Max Bag program
def FillMaxBag(graph,food):
	maxFoodEaten=5
	cur = graph.head
	nb=0
	while (cur):
		if(cur.data.getFoodEaten()==food):
			nb+=1
		cur=cur.NextFoodHabit
	if(nb<maxFoodEaten-2):
		print("Quantite consomme : {}/{}\nVous pouvez encore consommer ce produit sans probleme".format(nb,maxFoodEaten))
	elif(nb in range(maxFoodEaten-3,maxFoodEaten)):
		print("Quantite consomme : {}/{}\nAttention !! Vous etes proche de la limite requise".format(nb,maxFoodEaten))
	else:
		print("Quantite consomme : {}/{}\nVous avez depasse la limite requise !!!\nVous ne devez plus consommer ce produit.".format(nb,maxFoodEaten))
DataSet="data_food.csv"
graph=ReadFile(DataSet)
print("Habitudes Alimentaire :\n")
GraphTransversal(graph)
print("Prediction :\n")
predictProgram(graph)
print("Fill Max Bag :\n")
food=input("Que voulez-vous consommer ? ")
FillMaxBag(graph,food)
