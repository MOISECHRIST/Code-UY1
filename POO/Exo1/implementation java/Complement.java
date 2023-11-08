public class Complement{
	private String mNomComplement;
	private int mQteComplement;
	private String mCouleurComplement;
	public Complement(String NomComplement,int QteComplement,String CouleurComplement)
	{
		this.mNomComplement=NomComplement;
		this.mQteComplement=QteComplement;
		this.mCouleurComplement=CouleurComplement;
	}
	public String AfficherNomComplement()
	{
		return this.mNomComplement;
	}
	public int AfficherQteComplement()
	{
		return this.mQteComplement;
	}
	public String AfficherCouleurComplement()
	{
		return this.mCouleurComplement;
	}
}
