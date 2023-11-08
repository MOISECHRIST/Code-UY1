#ifndef CAT_H_INCLUDED
#define CAT_H_INCLUDED
#include "Entity.hpp"
#include <string>

class Cat: public Entity{
  public:
    Cat(int Id,std::string Sex,int Health,std::string TypeEntity,int Position,LifeTime);//Constructor
    //Methods
    std::string getSex();
     int getHealth();
	 void HealthUp();
	 void HealthDown(ListEntity liste);
     void EatMouse(Mouse mouse);
	 void killMouse(Mouse mouse);
    //Attributs 
  private:
    int Id, Health;
	 std::string Sex;
  public:
    int HealthMax,nbMouseEaten;
	 Mouse MouseEaten[25];
};
#endif