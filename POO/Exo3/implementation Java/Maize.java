public class Maize extends Entity
{
	private int Id, Qty;

	public Maize(int Id,String TypeEntity,int Position,int LifeTime)
	{
        super(TypeEntity,Position,LifeTime);
		this.Id=Id;
		this.Qty=7;
    }

	public int getQty()
	{
		return this.Qty;
	}
	public void QtyDown(ListEntity liste)
	{
		if(this.Qty>0)
		{
			this.Qty-=1;
		}
		else
		{
			this.moveEntity(0);
			if(liste.nbMaize>0)
				liste.rmMaize();
		}
	}
	public void appear(ListEntity liste)
	{
		if(liste.nbMaize<8)
		{
			int pos=(int)(Math.random()*25)+1;
			Maize maize= new Maize(liste.nbMaize,"Maize",pos,10);
			liste.AddMaize(maize);
			liste.nbMaize+=1;
		}
	}
}