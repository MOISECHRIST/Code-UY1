#include <iostream>
#include "AlimentProteine.hpp"

using namespace std;
AlimentProteine::AlimentProteine(string NomProteine,int QteProteine,string MethodeCuissonProteine,string TypeProteine)
	{
		this.mNomProteine=NomProteine;
		this.mQteProteine=QteProteine;
		this.mMethodeCuissonProteine=MethodeCuissonProteine;
		this.mTypeProteine=TypeProteine;
	}
	 string AlimentProteine::AfficherNomProteine(){
		return this.mNomProteine;
	}
	int AlimentProteine::AfficherQteProteine(){
		return this.mQteProteine;
	}
	string AlimentProteine::AfficherTypeProteine(){
		return this.mTypeProteine;
	}
	string AlimentProteine::AfficherMethodeCuissonProteine(){
		return this.mMethodeCuissonProteine;
	}