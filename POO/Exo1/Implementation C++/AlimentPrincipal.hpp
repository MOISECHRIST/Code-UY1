#ifndef ALIMENTPRINCIPAL_H_INCLUDED
#define ALIMENTPRINCIPAL_H_INCLUDED
#include <string>

//constructor
class AlimentPrincipal{
  public:
     AlimentPrincipal();
     AlimentPrincipal(std::string NomAliment,std::string TextureAliment,std::string CouleurAliment);//constructor
	  std::string AfficherNomAliment();
     void ModifierNomAliment(std::string NomAliment);
     std::string AfficherTextureAliment();
	  std::string AfficherCouleurAliment();
  //Attributes
  private:
     std::string mNomAliment;
	  std::string mTextureAliment;
	  std::string mCouleurAliment;
};
#endif