#ifndef COMPLEMENT_H_INCLUDED
#define COMPLEMENT_H_INCLUDED
#include <string>

class Complement{
   public:
     Complement();
      Complement(std::string NomComplement,int QteComplement,std::string CouleurComplement);//Constructor
     //Methods
      std::string AfficherNomComplement();
      int AfficherQteComplement();
      std::string AfficherCouleurComplement();
   //Attributes
  private:
    std::string mNomComplement;
	int mQteComplement;
	std::string mCouleurComplement;
};
#endif    