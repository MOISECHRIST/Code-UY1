#include <iostream>
#include "AlimentPrincipal.hpp"

using namespace std;

AlimentPrincipal::AlimentPrincipal(string NomAliment,string TextureAliment,string CouleurAliment)	{
		mNomAliment=NomAliment;
		mTextureAliment=TextureAliment;
		mCouleurAliment=CouleurAliment;
	}
string AlimentPrincipal::AfficherNomAliment(){
		return mNomAliment;
	}
void AlimentPrincipal::ModifierNomAliment(string NomAliment){
		mNomAliment=NomAliment;
	}
string AlimentPrincipal::AfficherTextureAliment(){
		return mTextureAliment;
	}
string AlimentPrincipal::AfficherCouleurAliment(){
		return mCouleurAliment;
	}