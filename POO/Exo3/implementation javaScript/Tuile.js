//definition de la classe Entity
class Entity{
    #TypeEntity;
    Position;
    #LifeTime;
    #Age;
    isDead;
    constructor(TypeEntity,Position,LifeTime){
        this.#TypeEntity=TypeEntity;
        this.Position=Position;
        this.LifeTime=LifeTime;
        this.#Age=1;
        this.isDead=false;
    }
    //fonction pour avoir l'age
    getAge(){
        return this.#Age;
    }
    AgeUp(){
        if(this.#Age<this.#LifeTime){
            this.#Age+=1;
        }else{
            this.isDead=true;
            this.moveEntity(0);
            if(listCat.nb>0){
                listCat.nb-=1;
            }
        }
    }
    //fonction permettant de recuperer la position d'une entity
    getPosition(){
        return this.Position;
    }
    //recuperation du type de l'entity
    getType(){
        return this.#TypeEntity;
    }
    //fonction qui permet de retirer une entity dans la tuile
    moveEntity(position){
        this.Position=position;
    }
}
//definition de la classe de la vie de l'Entity
class ListEntity{
    constructor(){
        this.tab= new Array();//l'utilisation de nex array nous permet d'avoir un tableau dynamique donc l'isertion a l'interieur se fait en utilisant la fonction push()
        this.nb=0;
    }
    AddEntity(elt){
        this.tab[this.nb]=elt;
        this.nb=this.nb+1;
    }
}
//definition de la class Cat
class Cat extends Entity{
    #Sex;
    constructor(Id,Sex,Health,TypeEntity,Position,LifeTime){
        super(TypeEntity,Position,LifeTime);
        this.Id=Id;
        this.#Sex=Sex;
        this.HealthMax=25;
        this.Health=Health;
        this.MouseEaten=new Array();
        this.nbMouseEaten=0;
    }
    getSex(){
        return this.#Sex;
    }
    getHealth(){
        return this.Health;
    }
    HealthUp(){
        return this.Health+=1;
    }
    HealthDown(listCat){
        if(this.Health>1){
            this.Health-=1;
        }else{
            this.Health-=1;
            this.moveEntity(0);
            listCat.nb-=1;
        }
    }
    reproduction(listCat){
        if(listCat.nb<5){
            var pos1=1+((Math.random()*25)%(25-1));

            var pos2=1+((Math.random()*25)%(25-1));
            
            var cat1=new Cat(listCat.nb,"Male",10,pos1,20);
            
            listCat.nb+=1;
            listCat.tab.push(cat1);

            var cat2=new Cat(listCat.nb,"Female",10,pos2,20);
            
            listCat.nb+=1;
            listCat.tab.push(cat2);
        }
    }
    EatMouse(mouse){
        mouse.moveEntity(0);
        this.nbMouseEaten+=1;
        this.MouseEaten.push(mouse);
        this.HealthUp();
    }
    KillMouse(mouse){
        mouse.isDead=true;
        if(this.Health<this.HealthMax){
            this.EatMouse(mouse);
        }
    }
}
//definition de la classe Mouse pour le projet
class Mouse extends Entity{
    constructor(Id,Sex,Health,TypeEntity,Position,LifeTime){
        super(TypeEntity,Position,LifeTime);
        this.Id=Id;
        this.Sex=Sex;
        this.Health=Health;
        this.HealthMax=5;
        this.MaizeEaten=[];
        this.nbMaizeEaten=0;
    }
    getSex(){
        return this.Sex;
    }
    getHealth(){
        return this.Health;
    }
    Healthup(){
        if(this.Health<this.HealthMax){
            this.Health+=1;
        }
    }
    HealthDown(listMouse){
        if(this.Health>1){
            this.Health-=1;
        }else{
            this.Health-=1;
            this.moveEntity(0);
            listMouse.nb-=1;
        }
    }
    reproduce(listMouse){
        if(listMouse.nb<10){
            //a = (Math.random() * nbplats)% (nbplats - 1)
            var pos1=1+((Math.random()*25)%(25-1));

			var pos2=1+((Math.random()*25)%(25-1));
			
            var mouse1=new Mouse(listMouse.nb,"Male",5,"Mouse",pos1,15);
            
            listMouse.nb+=1;
			listMouse.tab.push(mouse1);

            var mouse2=new Mouse(listMouse.nb,"Female",5,"Mouse",pos2,15);
            
            listMouse.nb+=1;
			listMouse.tab.push(mouse2);
        }  
    }
    EatMaize(maize){
        maize.isDead=true;
		maize.moveEntity(0);
            this.MaizeEaten.push(maize);
		this.nbMaizeEaten+=1;
        this.Healthup();
    }
}
//definition de la class maize poue les exercices
class Maize extends Entity{
    constructor(Id,TypeEntity,Position,LifeTime,){
        super(TypeEntity,Position,LifeTime);
        this.Id=Id;
        this.Qty=3;
    }
    getQty(){
        return this.Qty;
    }
    //definition de la fonction qui fait diminuer
    dowQty(listMaize){
        if(this.Qty>0){
            this.Qty=this.Qty-1;
        }else{
            this.moveEntity(0);
            listMaize.nb=listMaize.nb-1;
        }
    }
    appear(listMaize){
        if(listMaize.nb<8){
            var pos=1+((Math.random()*25)%(25-1));

            var maize=new Maize(listMaize.nb,"Maize",pos,10);
			
            listMaize.tab.push(maize);
			listMaize.nb+=1;
        }
    }
}
//creation de la classe Main
var listCat=new ListEntity();
var listMouse=new ListEntity();
var listMaize=new ListEntity();
//Cat1
var cat=new Cat(listCat.nb+1,"Male",10,"Cat",1,20);
listCat.AddEntity(cat);
//Cat2
cat=new Cat(listCat.nb+1,"Female",10,"Cat",8,20)
listCat.AddEntity(cat);
//Cat3
cat=new Cat(listCat.nb+1,"Female",10,"Cat",15,20)
listCat.AddEntity(cat);

//Mouse1
var mouse=new Mouse(listMouse.nb+1,"Mal",5,"Mouse",5,15);
listMouse.AddEntity(mouse);
//Mouse2
mouse=new Mouse(listMouse.nb+1,"Mal",5,"Mouse",6,15);
listMouse.AddEntity(mouse);
//Mouse3
mouse=new Mouse(listMouse.nb+1,"Mal",5,"Mouse",19,15);
listMouse.AddEntity(mouse);
//Mouse4
mouse=new Mouse(listMouse.nb+1,"Mal",5,"Mouse",21,15);
listMouse.AddEntity(mouse);
//Mouse5
mouse=new Mouse(listMouse.nb+1,"Mal",5,"Mouse",25,15);
listMouse.AddEntity(mouse);

//Maize1
var maize=new Maize(listMaize.nb+1,"Maize",10,10);
listMaize.AddEntity(maize);
//Maize2
maize=new Maize(listMaize.nb+1,"Maize",13,10);
listMaize.AddEntity(maize);
//Maize3
maize=new Maize(listMaize.nb+1,"Maize",23,10);
listMaize.AddEntity(maize);
//Maize4
maize=new Maize(listMaize.nb+1,"Maize",14,10);
listMaize.AddEntity(maize);
//Maize5
maize=new Maize(listMaize.nb+1,"Maize",18,10);
listMaize.AddEntity(maize);
var temps=0;
var size=5;

var i,j,m,n,tmp,p,k;

function mainProgram()
{
    var tile="";
    while(listCat.nb >= 0 && listMouse.nb >= 0){
        console.log("time", temps+1);
        console.log("*********************************************************************");
        for(i=0;i<size*size;i++){
            tmp=" ";
            if(i%size==0){
                for(j=0;j<listCat.nb;j++){
                    if(listCat.tab[j].getPosition()==i){
                        tmp=" "+listCat.tab[j].getType()+"("+listCat.tab[j].getSex()+")\n\n\n";
                    }else{
                        for(k=0;k<listMouse.nb;k++){
                            if(listMouse.tab[k].getPosition()==i){
                                tmp=" "+listMouse.tab[k].getType()+"("+listMouse.tab[k].getSex()+")\n\n\n";
                            }else{
                                for(n=0;n<listMaize.nb;n++){
                                    if(listMaize.tab[n].getPosition()==i){
                                        tmp=" "+listMaize.tab[n].getType()+"\n\n\n";
                                    }
                                }
                            }
                        }
                    }
                }
                if(tmp==" "){
                    tile+="   \n\n\n";
                }else{
                    tile+=tmp;
                }
            }else{
                for(j=0;j<listCat.nb;j++){
                    if(listCat.tab[j].position==i){
                        tmp=" "+listCat.tab[j].getType()+"("+listCat.tab[j].getSex()+")";
                    }else{
                        for(k=0;k<listMouse.nb;k++){
                            if(listMouse.tab[k].getPosition()==i){
                                tmp=" "+listMouse.tab[k].getType()+"("+listMouse.tab[k].getSex()+")";
                            }else{
                                for(n=0;n<listMaize.nb;n++){
                                    if(listMaize.tab[n].getPosition()==i){
                                        tmp=" "+listMaize.tab[n].getType();
                                    }
                                }
                            }
                        }
                    }
                }
                if(tmp==""){
                    tile+=" ";
                }else{
                    tile+=tmp;
                }
            }
        }
        console.log(tile);
        console.log("Total Cat : ",listCat.nb,"\nTotal Mouse : ",listMouse.nb,"\nTotal Maize : ",listMaize.nb);
        //operation permettant de faire une pause de 1 seconde
        //setTimeout(console.log,1000);
        /*time.sleep(1000);
        system("clear");*/
        
        for(i=0;i<listCat.nb;i++){
            k=0;
            listCat.tab[i].AgeUp();
            for(m=i+1;m<listCat.nb;m++){
                if(listCat.tab[m].getPosition()==listCat.tab[i].Position){
                    if(listCat.tab[m].getSex!=listCat.tab[i].getSex){
                        listCat.tab[m].reproduce(listCat);
                    }else{
                        p=1+((Math.random()*25)%(25-1));
                        listCat.tab[m].moveEntity(p);
                    }
                }
            }
            for(m=i+1;m<listMouse.nb;m++){
                if(listMouse.tab[m].getPosition()==listCat.tab[i].getPosition()){
                    listCat.tab[i].killMouse(listMouse.tab[m]);
                    k+=1;
                }
            }
            if(k==0){
                listCat.tab[i].HealthDown(listCat);
                p=1+((Math.random()*25)%(25-1));
                listCat.tab[i].moveEntity(p);
            }   
        }
        for(k=i+1;k<listMouse.nb;k++){
            i=0;
            listMouse.tab[k].AgeUp();
            for(m=i+1;m<listMouse.nb;m++){
                if(listMouse.tab[m].Position==listMouse.tab[k].Position){
                    if(listMouse.tab[k].getSex!=listMouse.tab[m].getSex){
                        listMouse.tab[m].reproduce(listMouse);
                    }else{
                        p=1+((Math.random()*25)%(25-1));
                        listMouse.tab[m].moveEntity(p);
                    }
                }
            }
            for(m=0;m<listMaize.nb;m++){
                if(listMouse.tab[k].Position==listMaize.tab[m].Position){
                    listMouse.tab[k].EatMaize(listMaize.tab[m]);
                    i+=1;
                }
            }
            if(i==0){
                listMouse.tab[k].HealthDown(listMouse);
                p=1+((Math.random()*25)%(25-1));
                listMouse.tab[k].moveEntity(p);
            }
        }
        for(let f=0;f<listMaize.nb;f++){
            listMaize.tab[f].dowQty(listMaize)
            
            if(temps%4==0){
                listMaize.tab[f].appear(listMaize)
            }
        }
        temps+=1;
        
        setTimeout(() => {
            mainProgram();
        }, 1000);
        break;
    }
}
mainProgram();