#ifndef LISTENTITY_H_INCLUDED
#define LISTENTITY_H_INCLUDED
#include <string>

class ListEntity{
   public:
      ListEntity();//Constructor
  //Methods
      void AddCat(Cat elt); 
      void AddMouse(Mouse elt);
	  void AddMaize(Maize elt);
	  void rmCat();
	  void rmMouse();
	  void rmMaize();

 //Attributs  
  public:
     int nbCat;
     int nbMouse;
     int nbMaize;
     Cat listCat[5];
	 Mouse listMouse[10];;
	 Maize listMaize[8];;
};
#endif