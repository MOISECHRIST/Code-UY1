#ifndef ENTITY_H_INCLUDED
#define ENTITY_H_INCLUDED
#include "ListEntity.hpp"

#include <string>

class Entity{
  public:
    Entity(std::string TypeEntity,int Position,int LifeTime);//Constructor
  //Methods
    int getAge();
    void AgeUp(ListEntity liste);
    std::string getType();
    void moveEntity(int Position);
  //Attributs  
  protected:
    std::string TypeEntity,LifeTime;
     int Age;
  public:   
	int isDead,Position;
};
#endif