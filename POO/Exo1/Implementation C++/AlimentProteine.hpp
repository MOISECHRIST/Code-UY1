#ifndef ALIMENTPROTEINE_H_INCLUDED
#define ALIMENTPROTEINE_H_INCLUDED
#include <string>
 class AlimentProteine{
   public:
     AlimentProteine();
     AlimentProteine(std::string NomProteine, int QteProteine,std::string MethodeCuissonProteine,std::string TypeProteine);//Constructors
     //Methods
      std::string AfficherNomProteine();
      int AfficherQteProteine();
      std::string AfficherTypeProteine();
      std::string AfficherMethodeCuissonProteine();
  //Atributes
   private:
     std::string mNomProteine;
	 int mQteProteine;
     std::string mMethodeCuissonProteine;
	 std::string mTypeProteine;  
};
#endif