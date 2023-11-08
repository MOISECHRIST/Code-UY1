#include <iostream>
#include "Entity.hpp"
#include "ListEntity.hpp"

using namespace std;

Entity::Entity(string TypeEntity,int Position,int LifeTime)
	{
		TypeEntity=TypeEntity;
		Position=Position;
		LifeTime=LifeTime;
		Age=1;
		isDead=0;
	}
	int Entity::getAge()
	{
		return Age;
	}
	void Entity::AgeUp(ListEntity liste)
	{
		if(Age<LifeTime)
		{
			Age+=1;
		}
		else{
			isDead=1;
			moveEntity(0);
			if(TypeEntity=="Cat")
			{
				if(liste.nbCat>0)
					liste.rmCat();
			}
			if(TypeEntity=="Mouse")
			{
				if(liste.nbMouse>0)
					liste.rmMouse();
			}
			if(TypeEntity=="Maize")
			{
				if(liste.nbMaize>0)
					liste.rmMaize();
			}
		}
	}
	 string Entity::getType()
	{
		return TypeEntity;
	}
	void Entity::moveEntity(int Position)
	{
		Position=Position;
	}