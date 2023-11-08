 #include <iostream>
 #include "Plat.hpp"
 #include "AlimentPrincipal.hpp"
#include "AlimentProteine.hpp"
#include "Complement.hpp"
#include "Epices.hpp"

using namespace std;

      Plat::Plat(string IdPlat,string NomPlat,string DescriptionPlat,string TypePlat,string ListeIngredient,string SourcePlat,string RecettePlat)
{
		mIdPlat=IdPlat;
		mNomPlat=NomPlat;
		mDescriptionPlat=DescriptionPlat;
		mTypePlat=TypePlat;
		mListeIngredient=ListeIngredient;
		mSourcePlat=SourcePlat;
		mRecettePlat=RecettePlat;
	}
void Plat::setNomPlat(string NomPlat){
		mNomPlat=NomPlat;
}
void Plat::setTypePlat(string TypePlat){
		mTypePlat=TypePlat;
	}
string Plat::getNomPlat(){
		return mNomPlat;
	}
string Plat::getTypePlat(){
		return mTypePlat;
	}
void Plat::ajouterAlPrin(AlimentPrincipal AlPrin){
		tabAlPrin[nbAlPrin]=AlPrin;
		nbAlPrin++;
	}
void Plat::ajouterAlProt(AlimentProteine AlProt){
		tabAlProt[nbAlProt]=AlProt;
		nbAlProt++;
	}
void Plat::ajouterCompl(Complement Compl){
		tabCompl[nbCompl]=Compl;
		nbCompl++;
	}
void Plat::ajouterEpices(Epices epices){
		tabEpices[nbEpices]=epices;
		nbEpices++;
	}