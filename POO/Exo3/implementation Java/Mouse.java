public class Mouse extends Entity
{
    private int Id, Health;
	private String Sex;
	public int HealthMax,nbMaizeEaten;
	public Maize MaizeEaten[]= new Maize[25];

    public Mouse(int Id, String Sex, int Health, String TypeEntity, int Position, int LifeTime)
    {
        super(TypeEntity,Position,LifeTime);
		this.Id=Id;
		this.Sex=Sex;
		this.Health=Health;
		this.HealthMax=15;
		this.nbMaizeEaten=0;
    }

    	public String getSex()
	{
		return this.Sex;
	}
	public int getHealth()
	{
		return this.Health;
	}
	public void HealthUp()
	{
		if(this.Health<this.HealthMax)
			this.Health++;
	}
	public void HealthDown(ListEntity liste)
	{
		if(this.Health>1)
		{
			this.Health--;
		}
		else
		{
			this.Health--;
			this.moveEntity(0);
			if(liste.nbMouse>0)
				liste.nbMouse--;
		}
	}
	public void EatMaize(Maize maize)
	{
		maize.moveEntity(0);
		this.MaizeEaten[nbMaizeEaten]=maize;
		nbMaizeEaten++;
		if(maize.getQty()==0)
		{
			this.HealthDown();	
		}
		else
		{
			this.HealthUp();
		}
		
	}
	public void Reproduce(ListEntity liste)
	{
		if(liste.nbCat<5)
		{
			int pos1=1+(int)(Math.random() * 25);
			int pos2=1+(int)(Math.random() * 25);
			Mouse mouse= new Mouse(liste.nbMouse,"Male",5,"Mouse",pos1,15);
			liste.AddMouse(mouse);
			mouse= new Mouse(liste.nbMouse,"Female",5,"Mouse",pos2,15);
			liste.AddMouse(mouse);
		}
	}
}