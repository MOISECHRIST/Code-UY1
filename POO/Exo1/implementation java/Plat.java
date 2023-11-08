public class Plat{
	private String mIdPlat, mNomPlat, mTypePlat, mSourcePlat;
	public String mDescriptionPlat, mListeIngredient, mRecettePlat;
	public AlimentPrincipal tabAlPrin[] = new AlimentPrincipal[5];
	public AlimentProteine tabAlProt[] = new AlimentProteine[5];
	public Complement tabCompl[] = new Complement[5];
	public Epices tabEpices[] = new Epices[5];
	public int nbAlPrin=0;
	public int nbAlProt=0;
	public int nbCompl=0;
	public int nbEpices=0;
	public Plat(String IdPlat,String NomPlat,String DescriptionPlat,String TypePlat,String ListeIngredient,String SourcePlat,String RecettePlat)
	{
		this.mIdPlat=IdPlat;
		this.mNomPlat=NomPlat;
		this.mDescriptionPlat=DescriptionPlat;
		this.mTypePlat=TypePlat;
		this.mListeIngredient=ListeIngredient;
		this.mSourcePlat=SourcePlat;
		this.mRecettePlat=RecettePlat;
	}
	public void setNomPlat(String NomPlat)
	{
		this.mNomPlat=NomPlat;
	}
	public void setTypePlat(String TypePlat)
	{
		this.mTypePlat=TypePlat;
	}
	public String getNomPlat()
	{
		return this.mNomPlat;
	}
	public String getTypePlat()
	{
		return this.mTypePlat;
	}
	public void ajouterAlPrin(AlimentPrincipal AlPrin)
	{
		this.tabAlPrin[nbAlPrin]=AlPrin;
		this.nbAlPrin++;
	}
	public void ajouterAlProt(AlimentProteine AlProt)
	{
		this.tabAlProt[nbAlProt]=AlProt;
		this.nbAlProt++;
	}
	public void ajouterCompl(Complement Compl)
	{
		this.tabCompl[nbCompl]=Compl;
		this.nbCompl++;
	}
	public void ajouterEpices(Epices epices)
	{
		this.tabEpices[nbEpices]=epices;
		this.nbEpices++;
	}
}
