#ifndef PLAT_H_INCLUDED
#define PLAT_H_INCLUDED
#include "Plat.hpp"
 #include "AlimentPrincipal.hpp"
#include "AlimentProteine.hpp"
#include "Complement.hpp"
#include "Epices.hpp"
#include <string>

class Plat{
   public:
     Plat();
 Plat(std::string IdPlat,std::string NomPlat,std::string DescriptionPlat,std::string TypePlat,std::string ListeIngredient,std::string SourcePlat,std::string RecettePlat);
      //Methods
      void setNomPlat(std::string NomPlat);
      void setTypePlat(std::string TypePlat);
      std::string getNomPlat();
      std::string getTypePlat();
      void ajouterAlPrin(AlimentPrincipal AlPrin);
      void ajouterAlProt(AlimentProteine AlProt);
      void ajouterCompl(Complement Compl);
      void ajouterEpices(Epices epices);
  //Attributs
   private:
     std::string mIdPlat;
     std::string mNomPlat;
     std::string mTypePlat;
     std::string mSourcePlat;

   public:
      std::string mDescriptionPlat, mListeIngredient, mRecettePlat;
	  AlimentPrincipal tabAlPrin[5];
	  AlimentProteine tabAlProt[5];
	  Complement tabCompl[5];
	  Epices tabEpices[5];
	  int nbAlPrin=0,nbAlProt=0,nbCompl=0,nbEpices=0;  
};
#endif