
#ifndef EPICES_H_INCLUDED
#define EPICES_H_INCLUDED
#include <string>

class Epices{
  public:
    Epices();
    Epices(std::string NomEpice);//Constructor
    //Methods
    std::string AfficherEpice();
 //Atributs
 private:
  std::string mNomEpice;   
};
#endif