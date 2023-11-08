#include <iostream>
#include "Maize.hpp"

using namespace std;

Maize::Maize(int Id,String TypeEntity,int Position,int LifeTime)
	{
		this.Id=Id;
		this.Qty=7;
		super(TypeEntity,Position,LifeTime);
	}
	void Maize::getQty(self)
	{
		return this.Qty;
	}
	void Maize::QtyDown(ListEntity liste)
	{
		if(this.Qty>0)
		{
			this.Qty-=1;
		}
		else
		{
			this.moveEntity(0);
			if(liste.nbMaize>0)
				liste.rmMaize();
		}
	}
	void Maize::appear(self,listMaize)
	{
		if(liste.nbMaize<8)
		{
			pos=randrange(25)+1
			maize=Maize(listMaize.nb,"Maize",pos,10)
			listMaize.tab+=[maize]
			listMaize.nb+=1
		}
	}