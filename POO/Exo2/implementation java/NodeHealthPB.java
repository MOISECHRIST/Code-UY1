public class NodeHealthPB
{
	public String HealthPB;
	public NodeHealthPB NextProblem = new NodeHealthPB();
	public NodeHealthPB(String HealthPB)
	{
		this.HealthPB=HealthPB;
	}
	public NodeHealthPB()
	{
		this.HealthPB="";
	}
	public String getHealthPB()
	{
		return this.HealthPB;
	}
	public int compare(NodeHealthPB elt)
	{
		return this.HealthPB!=elt.HealthPB;
	}
}
