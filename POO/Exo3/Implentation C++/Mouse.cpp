#include <iostream>
#include "Mouse.hpp"
#include "ListEntity.hpp"

using namespace std;

Mouse::Mouse(int Id,string Sex,int Health,string TypeEntity,int Position,int LifeTime)
	{
		Id=Id;
		Sex=Sex;
		Health=Health;
		HealthMax=15;
		nbMaizeEaten=0;
	}
	string Mouse::getSex()
	{
		return Sex;
	}
	int Mouse::getHealth()
	{
		return Health;
	}
	void Mouse::HealthUp()
	{
		if(Health<HealthMax)
			Health++;
	}
	void Mouse::HealthDown(ListEntity liste)
	{
		if(Health>1)
		{
			Health--;
		}
		else
		{
			Health--;
			moveEntity(0);
			if(liste.nbMouse>0)
				liste.nbMouse--;
		}
	}
	 void Mouse::reproduce(ListEntity liste)
	{
		if(listCat.nb<5)
		{
			int pos1=1+(int)(Math.random() * 25);
			int pos2=1+(int)(Math.random() * 25);
			Mouse mouse= new mouse(liste.nbMouse,"Male",5,"Mouse",pos1,15);
			liste.AddMouse(mouse);
			mouse= new mouse(liste.nbMouse,"Female",5,"Mouse",pos1,15);
			liste.AddMouse(mouse);
	    }
    }	