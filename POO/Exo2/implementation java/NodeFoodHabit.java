public class NodeFoodHabit
{
	public FoodHabit data= new FoodHabit();
	public NodeFoodHabit NextFoodHabit = new NodeFoodHabit();
	public NodeHealthPB Problem = new NodeHealthPB();
	public AddFoodHabit(FoodHabit elt)
	{
		this.data.copyFoodHabit(elt);
	}
	public void AddHealthProblem(NodeHealthPB elt)
	{
		this.Problem=elt;
	}
	public int compare(NodeFoodHabit elt)
	{
		return this.data.getFoodEaten()!=elt.getFoodEaten();
	}
}
