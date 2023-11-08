public class Cat extends Entity
{
    private int Id, Health;
    private String Sex;
	public int HealthMax, nbMouseEaten;
	public Mouse MouseEaten[]= new Mouse[25];

    public Cat(int Id, String Sex, int Health, String TypeEntity, int Position, int LifeTime)
    {
        super(TypeEntity,Position,LifeTime);
        this.Id=Id;
        this.Sex=Sex;
        this.Health=Health;
        this.HealthMax=15;
        this.nbMouseEaten=0;
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
			if(liste.nbCat>0)
				liste.nbCat--;
		}
	}
	public void Reproduce(ListEntity liste)
	{
		if(liste.nbCat<5)
		{
			int pos1=1+(int)(Math.random() * 25);
			int pos2=1+(int)(Math.random() * 25);
			Cat cat= new Cat(liste.nbCat,"Male",10,"Cat",pos1,20);
			liste.AddCat(cat);
			cat= new Cat(liste.nbCat,"Female",10,"Cat",pos2,20);
			liste.AddCat(cat);
		}
	}
	public void EatMouse(Mouse mouse)
	{
		this.MouseEaten[this.nbMouseEaten]=mouse;
		this.nbMouseEaten++;
	}
	public void killMouse(Mouse mouse)
	{
		mouse.isDead=1;
		mouse.moveEntity(0);
		if(this.Health<this.HealthMax)
			this.EatMouse(mouse);
	}
}