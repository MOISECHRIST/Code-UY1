public class Graph
{
	public NodeFoodHabit head = new NodeFoodHabit();
	public NodeFoodHabit end = new NodeFoodHabit();
	public int nb=0;
	public void Save(NodeFoodHabit elt)
	{
		if(this.nb==0)
		{
			self.head=elt;
			this.nb++;
		}
		else
		{	
			this.end.NextFoodHabit=elt;
			this.nb++;
		}
	}
}
