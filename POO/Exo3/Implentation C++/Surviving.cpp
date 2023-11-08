#include <iostream>
#include "Entity.hpp"
#include "Cat.hpp"
#include "Mouse.hpp"
#include "Maize.hpp"
#include "ListEntity.hpp"

using namespace std;

int main(){
    listCat=ListEntity();
    listMouse=ListEntity();
    listMaize=ListEntity();
        //Cat1
    cat = new Cat(listCat.nb+1,"Male",10,"Cat",1,20);
    listCat.AddEntity(cat);
        //Cat2
    cat= new Cat(listCat.nb+1,"Female",10,"Cat",8,20);
        listCat.AddEntity(cat);
        //Cat3
    cat= new Cat(listCat.nb+1,"Female",10,"Cat",15,20);
    listCat.AddEntity(cat);

        //Mouse1
    mouse= new Mouse(listMouse.nb+1,"Mal",5,"Mouse",5,15);
        listMouse.AddEntity(mouse);
        //Mouse2
    mouse= new Mouse(listMouse.nb+1,"Mal",5,"Mouse",6,15);
    listMouse.AddEntity(mouse);
        //Mouse3
    mouse= new Mouse(listMouse.nb+1,"Mal",5,"Mouse",19,15);
        listMouse.AddEntity(mouse);
        //Mouse4
    mouse= new Mouse(listMouse.nb+1,"Mal",5,"Mouse",21,15);
        listMouse.AddEntity(mouse);
        //Mouse5
    mouse= new Mouse(listMouse.nb+1,"Mal",5,"Mouse",25,15);
        listMouse.AddEntity(mouse);

        //Maize1
    maize=new Maize(listMaize.nb+1,"Maize",10,10);
    listMaize.AddEntity(maize);
        //Maize2
    maize=new Maize(listMaize.nb+1,"Maize",13,10);
    listMaize.AddEntity(maize);
        //Maize3
    maize=new Maize(listMaize.nb+1,"Maize",23,10);
    listMaize.AddEntity(maize);
        //Maize4
    maize= new Maize(listMaize.nb+1,"Maize",14,10);
    listMaize.AddEntity(maize);
        //Maize5
    maize=new Maize(listMaize.nb+1,"Maize",18,10);
    listMaize.AddEntity(maize);
        //PrintTile(listCat,listMouse,listMaize)
    int temps=0;
    while(listCat.nb+listMaize.nb+listMaize.nb>0)
        {
            cout << "Time ;", temp+1;
            cout << "***********************************************************************************************";
            int i,j,k,size = 5;
            string title=" ", tmp=" ";
            for(i=1;i<(size*size);i++)
            {
                tmp=" ";
                if(i%size==0)
                {
                    for(j=0;j<listCat.nb;j++)
                    {
                        if(cat.listCat[j].Position==i)
                        {
                            tmp="      "+cat.listCat[j].getType()+"("+cat.listCat[j].getSex()+")\n\n\n";
                        }
                        else
                        {
                            for(k=0;k<listMouse.nb;k++)
                            {
                                if(mouse.listMouse[k].Position==i)
                                {
                                    tmp="      "+listMouse[n].getType()+"\n\n\n";
                                }
                            }
                        }
                    }
                }
            }
        }
    }
