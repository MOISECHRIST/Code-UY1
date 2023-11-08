from random import randrange
from EcoSystem import *	
import time
from os import *	
listCat=ListEntity()
listMouse=ListEntity()
listMaize=ListEntity()
#Cat1
cat=Cat(listCat.nb+1,"Male",10,"Cat",1,20)
listCat.AddEntity(cat)
#Cat2
cat=Cat(listCat.nb+1,"Female",10,"Cat",8,20)
listCat.AddEntity(cat)
#Cat3
cat=Cat(listCat.nb+1,"Female",10,"Cat",15,20)
listCat.AddEntity(cat)
#Mouse1
mouse=Mouse(listMouse.nb+1,"Mal",5,"Mouse",5,15)
listMouse.AddEntity(mouse)
#Mouse2
mouse=Mouse(listMouse.nb+1,"Mal",5,"Mouse",6,15)
listMouse.AddEntity(mouse)
#Mouse3
mouse=Mouse(listMouse.nb+1,"Mal",5,"Mouse",19,15)
listMouse.AddEntity(mouse)
#Mouse4
mouse=Mouse(listMouse.nb+1,"Mal",5,"Mouse",21,15)
listMouse.AddEntity(mouse)
#Mouse5
mouse=Mouse(listMouse.nb+1,"Mal",5,"Mouse",25,15)
listMouse.AddEntity(mouse)
#Maize1
maize=Maize(listMaize.nb+1,"Maize",10,10)
listMaize.AddEntity(maize)
#Maize2
maize=Maize(listMaize.nb+1,"Maize",13,10)
listMaize.AddEntity(maize)
#Maize3
maize=Maize(listMaize.nb+1,"Maize",23,10)
listMaize.AddEntity(maize)
#Maize4
maize=Maize(listMaize.nb+1,"Maize",14,10)
listMaize.AddEntity(maize)
#Maize5
maize=Maize(listMaize.nb+1,"Maize",18,10)
listMaize.AddEntity(maize)
#PrintTile(listCat,listMouse,listMaize)
temps=0
while(listCat.nb+listMouse.nb+listMaize.nb>0):
	print("Time :",temps+1)
	print("*********************************************************************")
	size=5
	tile=""
	for i in range(1,size*size +1):
		tmp=""
		if(i%size==0):
		
			for j in range(listCat.nb):
				if(listCat.tab[j].Position==i):
					tmp="      "+listCat.tab[j].getType()+"("+listCat.tab[j].getSex()+")\n\n\n"
				else:
					for k in range(listMouse.nb):						
						if(listMouse.tab[k].Position==i):
							tmp="      "+listMouse.tab[k].getType()+"("+listMouse.tab[k].getSex()+")\n\n\n"
						else:
							for n in range(listMaize.nb):
								if(listMaize.tab[n].Position==i):
									tmp="      "+listMaize.tab[n].getType()+"\n\n\n"
			if(tmp==""):
				tile+="      \n\n\n"
			else:
				tile+=tmp
		else:
			for j in range(listCat.nb):
				if(listCat.tab[j].Position==i):
					tmp="      "+listCat.tab[j].getType()+"("+listCat.tab[j].getSex()+")"
				else:
					for k in range(listMouse.nb):						
						if(listMouse.tab[k].Position==i):
							tmp="      "+listMouse.tab[k].getType()+"("+listMouse.tab[k].getSex()+")"
						else:
							for n in range(listMaize.nb):
								if(listMaize.tab[n].Position==i):
									tmp="      "+listMaize.tab[n].getType()
			if(tmp==""):
				tile+="      "
			else:
				tile+=tmp
	print(tile)
	print("Total Cat : ",listCat.nb,"\nTotal Mouse : ",listMouse.nb,"\nTotal Maize : ",listMaize.nb)
	#faire une pause de 1 seconds
	time.sleep(1)
	system("clear")
	for i in range(listCat.nb):
		k=0
		listCat.tab[i].AgeUp(listCat)
		for m in range(i+1,listCat.nb):
			if(listCat.tab[m].Position==listCat.tab[i].Position):	
				if(listCat.tab[m].getSex!=listCat.tab[i].getSex):
			   		listCat.tab[m].reproduce(listCat)
				else:
			   		p=1+randrange(25)
			   		listCat.tab[m].moveEntity(p)
		for m in range(listMouse.nb):
			if(listMouse.tab[m].Position==listCat.tab[i].Position):
				listCat.tab[i].killMouse(listMouse.tab[m])
				k+=1
		if(k==0):
			listCat.tab[i].HealthDown(listCat)
			p=1+randrange(25)
			listCat.tab[i].moveEntity(p)
	for k in range(listMouse.nb):
		i=0
		listMouse.tab[k].AgeUp(listMouse)
		for m in range(k+1,listMouse.nb):
			if(listMouse.tab[m].Position==listMouse.tab[k].Position):
				if(listMouse.tab[k].getSex!=listMouse.tab[m].getSex):
					listMouse.tab[m].reproduce(listMouse)
				else:
					p=1+randrange(25)
					listMouse.tab[m].moveEntity(p)
		for m in range(listMaize.nb):
			if(listMouse.tab[k].Position==listMaize.tab[m].Position):
				listMouse.tab[k].EatMaize(listMaize.tab[m])
				i+=1
		if(i==0):
			listMouse.tab[k].HealthDown(listMouse)
			p=1+randrange(25)
			listMouse.tab[k].moveEntity(p)
	for m in range(listMaize.nb):
		listMaize.tab[m].QtyDown(listMaize)
		listMaize.tab[m].AgeUp(listMaize)
		if(temps%4==0):
			listMaize.tab[m].appear(listMaize)
	'''for i in range(len(listCat.tab)):
		if(listCat.tab[i].Position==0):
			listCat.tab.pop(i)
	for j in range(len(listMouse.tab)):
		if(listMouse.tab[j].Position==0):
			listMouse.tab.pop(j)
	for k in range(len(listMaize.tab)):
		if(listMaize.tab[k].Position==0):
			listMaize.tab.pop(k)'''
	temps+=1
