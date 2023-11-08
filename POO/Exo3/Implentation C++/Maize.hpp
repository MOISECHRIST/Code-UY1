#ifndef ENTITY_H_INCLUDED
#define ENTITY_H_INCLUDED
#include "Entity.hpp"
#include <string>

class Mouse: public Entity{
   public:
      Maize(int Id,std::string TypeEntity,int Position,int LifeTime);//Constructor
  //Methods
      void getQty();
      void QtyDown(ListEntity liste);
      void appear(listMaize);
 //Attributs  
  private:
     int Id;
     int Qty;

};
#endif