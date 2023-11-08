//definition du noeud habitudes alimentaire
class FoodHabit{
    //classe utilisée pour stockerles données sur les habitudes alimentaires
    constructor(date,foodEaten,nbFoodEaten,QtyWater,otherLiquid,FruitEaten,nbBowel){
        this.date=date;
        this.foodEaten=foodEaten;
        this.nbFoodEaten=foodEaten;
        this.QtyWater=QtyWater;
        this.otherLiquid=otherLiquid;
        this.FruitEaten=FruitEaten;
        this.nbBowel=nbBowel;
    }
    getFoodEaten(){
        return this.foodEaten;
    }
}
class NodeFoodHabit{
    //class utilisée pour creer les noeuds d'habitudes alimentaires
    constructor(elt=null){
        this.date=elt;
        this.NexFoodHabit=null;
        this.problem=null;
    }
    AddHealthProblem(elt){
        this.Problem=elt;
    }
}
class Graph{
    constructor(){
        this.head=null;
    }
    save(elt){
        if(this.head==null){
            this.head=elt;
        }else{
          var cur=this.head;
            while(cur.NextFoodHabit==null){
                cur=cur.NexFoodHabit;
            }
            cur.NextFoodHabit=elt;
        }
    }
}
//definition du noeud probleme de santé
class NodeHealthPB{
    constructor(HealthPB){
        this.HealthPB=HealthPB;
        this.NextProblem=null;
    }
    getHealthPB(){
        return this.HealthPB;
    }
}
//definition de la classe pour la liste des pobleme de santé
class ListHealthPB{
    constructor(){
        this.head=null;
    }
    SaveHealthPB(elt){
        if(this.head=null){
            this.head=elt;
        }else{
            var cur =this.head;
            while((cur.NextProblem==null)&&(cur.getHealthPB()!=elt.getHealthPB()))
            {
                cur=cur.NextProblem;
                if(cur.getHealthPB() != elt.getHealthPB()){
                    cur.NextProblem=elt;
                }
            }
        }
    }
}
//ecriture de la fonction main pour le programme js..
/*comment acceder a un fichier en utilisant le javaScript */
function ReadFile(DataSet){
    var graph= Graph();
    var listHPB= ListHealthPB();
    
    var fs.ReadFile(data_food.csv,"r")
 }
