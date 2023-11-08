public class AlimentPrincipal{
	private String mNomAliment;
	private String mTextureAliment;
	private String mCouleurAliment;
	public AlimentPrincipal(String NomAliment, String TextureAliment, String CouleurAliment)
	{
		this.mNomAliment=NomAliment;
		this.mTextureAliment=TextureAliment;
		this.mCouleurAliment=CouleurAliment;
	}
	public String AfficherNomAliment()
	{
		return this.mNomAliment;
	}
	public void ModifierNomAliment(String NomAliment)
	{
		this.mNomAliment=NomAliment;
	}
	public String AfficherTextureAliment()
	{
		return this.mTextureAliment;
	}
	public String AfficherCouleurAliment()
	{
		return this.mCouleurAliment;
	}
}
