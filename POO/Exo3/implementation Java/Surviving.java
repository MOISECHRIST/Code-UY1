public class Surviving
{
    public static void main(String[] agrs)
    {
        ListEntity listEntity;
        //Cat1
        Cat cat = new Cat(listEntity.nbCat+1,"Male",10,"Cat",1,20);
        listEntity.AddCat(cat);
        //Cat2
        cat= new Cat(listEntity.nbCat+1,"Female",10,"Cat",8,20);
        listEntity.AddCat(cat);
        //Cat3
        cat= new Cat(listEntity.nbCat+1,"Female",10,"Cat",15,20);
        listEntity.AddCat(cat);

        //Mouse1
        Mouse mouse= new Mouse(listEntity.nbMouse+1,"Mal",5,"Mouse",5,15);
        listEntity.AddMouse(mouse);
        //Mouse2
        mouse= new Mouse(listEntity.nbMouse+1,"Mal",5,"Mouse",6,15);
        listEntity.AddMouse(mouse);
        //Mouse3
        mouse= new Mouse(listEntity.nbMouse+1,"Mal",5,"Mouse",19,15);
        listEntity.AddMouse(mouse);
        //Mouse4
        mouse= new Mouse(listEntity.nbMouse+1,"Mal",5,"Mouse",21,15);
        listEntity.AddMouse(mouse);
        //Mouse5
        mouse= new Mouse(listEntity.nbMouse+1,"Mal",5,"Mouse",25,15);
        listEntity.AddMouse(mouse);

        //Maize1
        Maize maize=new Maize(listEntity.nbMaize+1,"Maize",10,10);
        listEntity.AddMaize(maize);
        //Maize2
        maize=new Maize(listEntity.nbMaize+1,"Maize",13,10);
        listEntity.AddMaize(maize);
        //Maize3
        maize=new Maize(listEntity.nbMaize+1,"Maize",23,10);
        listEntity.AddMaize(maize);
        //Maize4
        maize= new Maize(listEntity.nbMaize+1,"Maize",14,10);
        listEntity.AddMaize(maize);
        //Maize5
        maize=new Maize(listEntity.nbMaize+1,"Maize",18,10);
        listEntity.AddMaize(maize);
        //PrintTile(listCat,listMouse,listMaize)
        System.out.println("**********************************************************************************************************************");
            int i,j,k,l,m,size = 5;
            String title=" ", tmp=" ";
            for(i=1;i<(size*size);i++)
            {
                tmp=" ";
                if(i%size==0)
                {
                    for(j=0;j<listEntity.nbCat;j++)
                    {
                        if(listEntity.listCat[j].Position==i)
                        {
                            tmp="      "+listEntity.listCat[j].getType()+"("+listEntity.listCat[j].getSex()+")\n\n\n";
                        }
                        else
                        {
                            for(k=0;k<listEntity.nbMouse;k++)
                            {
                                if(listEntity.listMouse[k].Position==i)
                                {
                                    tmp="      "+listEntity.listMouse[k].getType()+"("+listEntity.listMouse[k].getSex()+")\n\n\n";
                                }
                                else
                                {
                                    for(l=0;l<listEntity.nbMaize;l++)
                                    {
                                        if(listEntity.listMaize[l].Position==i)
                                        {
                                            tmp="      "+listEntity.listMaize[l].getType()+"\n\n\n";
                                        }
                                    }
                                }
                            }
                        }
                    }
                    if(tmp==" ")
                    {
                        title+="   \n\n";
                    }
                    else
                    {
                        title+=tmp;
                    }
                }
                else
                {
                    for(j=0;j<listEntity.nbCat;j++)
                    {
                        if(listEntity.listCat[j].Position==i)
                        {
                            tmp="    "+listEntity.listCat[j].getType()+"("+listEntity.listCat[j].getSex()+")";
                        }
                        else
                        {
                            for(k=0;k<listEntity.nbMouse;k++)
                            {
                                if(listEntity.listMouse[k].Position==i)
                                {
                                    tmp="      "+listEntity.listMouse[k].getType()+"("+listEntity.listMouse[k].getSex()+")";
                                }
                                else
                                {
                                    for(l=0;l<listEntity.nbMaize;l++)
                                    {
                                        if(listEntity.listMaize[l].Position==i)
                                        {
                                            tmp="      "+listEntity.listMaize[l].getType()+")";
                                        }
                                    }
                                }
                            }
                        }
                    }
                    if(tmp=="")
                    {
                        title+="      ";
                    }
                    else
                    {
                        title+=tmp;
                    }
                }
            }
        System.out.println("title");
        System.out.println("Total Cat : "+listEntity.nbCat+"\nTotal Mouse : "+listEntity.nbMouse+"\nTotal Maize : "+listEntity.nbMaize);

        //pour faire bune pause de 1 second pour le terminal
        Thread.sleep(1000);
			   String command = "cls";
			   Runtime runtime = Runtime.getRuntime();
			   Process process = null;
        try
				   {
					process = runtime.exec(command);
				   } catch(Exception err) {;}
        for(i=0;i<listEntity.nbCat;i++)
        {
            k=0;
            for(m=i+1;m<listEntity.nbCat;m++)
            {
                if(listEntity.listCat[m].Position==listEntity.listCat[i].Position)
                {
                    if(listEntity.listCat[m].getSex()!=listEntity.listCat[i].getSex())
                    {
                        cat.Reproduce(listEntity);
                    }
                    else
                    {
                        listEntity.listCat[m].moveEntity(1+(int)(Math.random() * 25));
                    }
                }
            }
            for(m=0;m<listEntity.nbMouse;m++)
            {
                if(listEntity.listMouse[m].Position==listEntity.listCat[i].Position)
                {
                    listEntity.listCat[i].killMouse(listEntity.listMouse[m]);
                    k++;
                }
            }
            if(k==0)
			   	{
			   		listEntity.listCat[i].HealthDown(listEntity);
			   	}
			   	listEntity.listCat[i].moveEntity(1+(int)(Math.random() * 25));
			}
            for(k=0;k<listEntity.nbMouse;k++)
			{
			   	i=0;
			   	for(m=k+1;m<listEntity.nbMouse;m++)
			   	{
			   		if(listEntity.listMouse[m].Position==listEntity.listMouse[k].Position)
			   		{
			   			if(listEntity.listMouse[m].getSex()!= listEntity.listMouse[k].getSex())
			   				mouse.Reproduction(listEntity);
			   			else
			   				listEntity.listMouse[m].moveEntity(1+(int)(Math.random() * 25));
			   		}			
			   	}
			   	for(m=0;m<listEntity.nbMaize;m++)
			   	{
			   		if(listEntity.listMouse[k].Position==listEntity.listMaize[m].Position)
			   		{
			   			listEntity.listMouse[k].EatMaize(listEntity.listMaize[m]);
			   			i++;
			   		}
			   	}
			   	if(k==0)
			   	{
			   		listEntity.listMouse[k].HealthDown(listEntity);
			   	}
			   	listEntity.listMouse[k].moveEntity(1+(int)(Math.random() * 25));
			   }
            }
        }
    }
}