public class ListEntity
{
    public Cat listCat[]= new Cat[5];
    public Mouse listMouse[]= new Mouse[10];
    public Maize listMaize[]= new Maize[8];
    public int nbCat, nbMouse, nbMaize;

    public ListEntity()
    {
        this.nbCat=0;
        this.nbMouse=0;
        this.nbMaize=0;
    }

    public void AddCat(Cat elt)
	{
		this.nbCat++;
		this.listCat[nbCat]=elt;
	}
	public void AddMouse(Mouse elt)
	{
		this.nbMouse++;
		this.listMouse[nbMouse]=elt;
	}
	public void AddMaize(Maize elt)
	{
		this.nbMaize++;
		this.listMaize[nbMaize]=elt;
	}
	public void rmCat()
	{
		this.nbCat--;
	}
	public void rmMouse()
	{
		this.nbMouse++;
	}
	public void rmMaize()
	{
		this.nbMaize--;
	}
}