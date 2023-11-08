#include <iostream>
#include "Cat.hpp"
#include "Mouse.hpp"

using namespace std;

Cat::Cat(int Id,string Sex,int Health,string TypeEntity,int Position,int LifeTime)
	{
		
		Id=Id;
		Sex=Sex;
		Health=Health;
		HealthMax=15;
		nbMouseEaten=0;
	}
	string Cat::getSex()
	{
		return Sex;
	}
	 int Cat::getHealth()
	{
		return Health;
	}
	 void Cat::HealthUp()
	{
		if(Health<HealthMax)
			Health++;
	}
	void Cat::HealthDown(ListEntity liste)
	{
		if(Health>1)
		{
			Health--;
		}
		else
		{
			Health--;
			moveEntity(0);
			if(listCat.nbMouse>0)
				liste.nbCat--;
		}
	}
	void Cat::reproduce(ListEntity liste)
	{
		if(listCat.nb<5)
		{
			int pos1=1+(int)(Math.random() * 25);
			int pos2=1+(int)(Math.random() * 25);
			Cat cat= new Cat(liste.nbCat,"Male",10,"Cat",pos1,20);
			liste.AddCat(cat);
			cat= new Cat(liste.nbCat,"Female",10,"Cat",pos1,20);
			liste.AddCat(cat);
		}
	}
	void Cat::EatMouse(Mouse mouse)
	{
		MouseEaten[nbMouseEaten]=mouse;
		nbMouseEaten++;
	}
	 void Cat::killMouse(Mouse mouse)
	{
		mouse.isDead=1;
		mouse.moveEntity(0);
		if(Health<HealthMax)
			EatMouse(mouse);
	}