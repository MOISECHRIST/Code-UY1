public class AlimentProteine{
	private String mNomProteine;
	private int mQteProteine;
	private String mMethodeCuissonProteine;
	private String mTypeProteine;
	public AlimentProteine(String NomProteine, int QteProteine, String MethodeCuissonProteine, String TypeProteine)
	{
		this.mNomProteine=NomProteine;
		this.mQteProteine=QteProteine;
		this.mMethodeCuissonProteine=MethodeCuissonProteine;
		this.mTypeProteine=TypeProteine;
	}
	public String AfficherNomProteine()
	{
		return this.mNomProteine;
	}
	public int AfficherQteProteine()
	{
		return this.mQteProteine;
	}
	public String AfficherTypeProteine()
	{
		return this.mTypeProteine;
	}
	public String AfficherMethodeCuissonProteine()
	{
		return this.mMethodeCuissonProteine;
	}
}
