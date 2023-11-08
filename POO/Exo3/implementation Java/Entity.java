public class Entity
{
    protected String TypeEntity;
    protected int Age, LifeTime;
    public int isDead, Position;

    public Entity(String TypeEntity, int Position, int LifeTime)
    {
        this.TypeEntity=TypeEntity;
        this.Position=Position;
        this.LifeTime=LifeTime;
        this.Age=1;
        this.isDead=0;
    }

    public int getAge()
    {
        return this.Age;
    }
    public String getType()
	{
		return this.TypeEntity;
	}
	public void moveEntity(int Position)
	{
		this.Position=Position;
	}
    public void AgeUp(ListEntity liste)
    {
        if(this.Age < this.LifeTime)
        {
			this.Age+=1;
		}
		else{
			this.isDead=1;
			this.moveEntity(0);
			if(this.TypeEntity=="Cat")
			{
				if(liste.nbCat>0)
					liste.rmCat();
			}
			if(this.TypeEntity=="Mouse")
			{
				if(liste.nbMouse>0)
					liste.rmMouse();
			}
			if(this.TypeEntity=="Maize")
			{
				if(liste.nbMaize>0)
					liste.rmMaize();
			}
		}
    }
}