#ifndef ENTITY_H_INCLUDED
#define ENTITY_H_INCLUDED
#include "Entity.hpp"
#include <string>

class Mouse:public Entity{
   public:
      Mouse(int Id,std::string Sex,int Health,std::string TypeEntity,int Position,int LifeTime);//Constructor
  //Methods
      std::string getSex();
      int getHealth();
      void HealthUp();
      void HealthDown(ListEntity liste);
      void reproduce(ListEntity liste);
  //Attributs  
  private:
     int Id, Health;
	 std::string Sex;
  public:   
	 Maize MaizeEaten[25];
     int HealthMax,nbMaizeEaten;
  
};
#endif