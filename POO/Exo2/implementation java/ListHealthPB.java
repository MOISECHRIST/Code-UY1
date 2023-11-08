class ListHealthPB
{
	public NodeHealthPB head = new NodeHealthPB();
	public NodeHealthPB end = new NodeHealthPB();
	public int isEmpty=0;
	public void SaveHealthPB(NodeHealthPB elt)
	{
		if(this.isEmpty==0)
		{
			this.head=elt;
			this.isEmpty=1;
		}
		else
		{
			NodeHealthPB cur = new NodeHealthPB();
			cur=this.head;
			while((this.end.compare(cur.NextProblem))&&(cur.getHealthPB() != elt.getHealthPB()))
			{
				cur=cur.NextProblem;
			}
			if(cur.getHealthPB() != elt.getHealthPB())
				cur.NextProblem=elt;
		}
	}
}
