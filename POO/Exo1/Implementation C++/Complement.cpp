#include <iostream>
#include "Complement.hpp"

using namespace std;

Complement::Complement(string NomComplement,int QteComplement,string CouleurComplement)
	{
		mNomComplement=NomComplement;
		mQteComplement=QteComplement;
		mCouleurComplement=CouleurComplement;
	}
string Complement::AfficherNomComplement()
	{
		return mNomComplement;
	}
int Complement::AfficherQteComplement()
	{
		return mQteComplement;
	}
string Complement::AfficherCouleurComplement()
	{
		return mCouleurComplement;
	}