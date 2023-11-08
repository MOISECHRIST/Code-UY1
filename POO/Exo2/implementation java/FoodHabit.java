public class FoodHabit
{
	private String date,foodEaten,nbFoodEaten,FruitEaten;
	private int QtyWater,OtherLiquid,nbBowel;
	public FoodHabit(String date, String foodEaten, String nbFoodEaten, int QtyWater, int OtherLiquid, int nbBowel)
	{
		this.date=date;
		this.foodEaten=foodEaten;
		this.nbFoodEaten=nbFoodEaten;
		this.QtyWater=QtyWater;
		this.OtherLiquid=OtherLiquid;
		this.nbBowel=nbBowel;
	}
	public FoodHabit()
	{
		this.date="";
		this.foodEaten="";
		this.nbFoodEaten=0;
		this.QtyWater=0;
		this.OtherLiquid="";
		this.nbBowel=0;
	}
	public void CopyFoodHabit(FoodHabit elt)
	{
		this.date=elt.date;
		this.foodEaten=elt.foodEaten;
		this.nbFoodEaten=elt.nbFoodEaten;
		this.QtyWater=elt.QtyWater;
		this.OtherLiquid=elt.OtherLiquid;
		this.nbBowel=elt.nbBowel;
	} 
	public String getFoodEaten()
	{
		return this.foodEaten;
	}
}
