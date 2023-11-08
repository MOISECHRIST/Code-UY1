#include <iostream>
#include "Epices.hpp"

using namespace std;

Epices::Epices(string NomEpice)
	{
		mNomEpice=NomEpice;
	}
string Epices::AfficherEpice()
	{
		return mNomEpice;
	}