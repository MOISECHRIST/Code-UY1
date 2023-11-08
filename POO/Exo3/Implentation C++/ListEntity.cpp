#include <iostream>
#include "ListEntity.hpp"
#include "Cat.hpp"
#include "Mouse.hpp"
#include "Maize.hpp"


using namespace std;

ListEntity:ListEntity()
	{
		nbMaize=0;
		nbMouse=0;
		nbCat=0;
	}
	void ListEntity::AddCat(Cat elt)
	{
		nbCat++;
		listCat[nbCat]=elt;
	}
	void ListEntity::AddMouse(Mouse elt)
	{
		nbMouse++;
		listMouse[nbMouse]=elt;
	}
	void ListEntity::AddMaize(Maize elt)
	{
		nbMaize++;
		listMaize[nbMaize]=elt;
	}
	void ListEntity::rmCat()
	{
		nbCat--;
	}
	void ListEntity::rmMouse()
	{
		nbMouse++;
	}
	void ListEntity::rmMaize()
	{
		nbMaize--;
	}