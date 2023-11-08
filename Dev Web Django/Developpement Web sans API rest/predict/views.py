from django.contrib.auth import get_user_model, login,logout, authenticate
from django.shortcuts import render,get_object_or_404,redirect
from predict.models import *
from django.urls import reverse

User=get_user_model()


# Create your views here.
def home_view(request):
    return render(request,'index.html')

def index_view(request, username):
    user=get_object_or_404(Personne,username=username)
    return render(request,'predict/index.html', context={'user': user})

def login_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        try:
            user1=authenticate(username=username,password=password)
            login(request,user1)
        except:
            user2=User.objects.get(username=username,password=password)
            login(request,user2) 
        return redirect(reverse("predict",kwargs={"username": username}))           
    return render(request,'predict/login.html')

def newuser_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        sex=request.POST.get("sex")
        date_of_birth=request.POST.get("date_of_birth")
        first_name=request.POST.get("first_name")
        image=request.POST.get("image")
        last_name=request.POST.get("last_name")
        user=User.objects.create_user(username=username,
                                      password=password,
                                      first_name=first_name,
                                      last_name=last_name,
                                      sex=sex,
                                      date_of_birth=date_of_birth,
                                      image=image)
        login(request,user)
        return redirect(reverse("predict",kwargs={"username": username}))
    return render(request,'predict/new_user.html')

def logout_user(request):
    logout(request)
    return redirect('accueil')

def enreg_conso_view(request,username):
    foods=Food.objects.all()
    hpbs=Health_Problem.objects.all()
    user=get_object_or_404(Personne,username=username)
    if request.method=="POST":
        date=request.POST.get("date")
        day_of_week=request.POST.get("day_of_week")
        hpb_name=request.POST.get("hpb_name")
        food_name=request.POST.get("food_name")
        food =Food.objects.get(name=food_name)
        hpb =Health_Problem.objects.get(name=hpb_name)
        nut=Nutritional_Diary.objects.create(date=date,
                                         day_of_week=day_of_week,
                                         personne=user,
                                         food=food,
                                         health_pb=hpb,
                                         )
        slog=str(nut.personne.first_name)+"_"+user.username
        nut.slog=slog
        nut.save()
        return redirect(reverse("predict",kwargs={"username": username}))
    return render(request, 'predict/enreg_conso.html', context={"foods":foods, "hpbs":hpbs, 'user': user })

def enreg_food_view(request,username):
    user=get_object_or_404(Personne,username=username)
    if request.method=="POST":
        name=request.POST.get("name")
        image=request.POST.get("image")
        description=request.POST.get("description")
        Food.objects.create(
            name=name,
            image=image,
            description=description
        )
        return redirect(reverse("predict",kwargs={"username": username}))
    return render(request, 'predict/enreg_food.html', context={'user': user})

def enreg_hpb_view(request,username):
    user=get_object_or_404(Personne,username=username)
    if request.method=="POST":
        name=request.POST.get("name")
        description=request.POST.get("description")
        Health_Problem.objects.create(
            name=name,
            description=description
        )
        return redirect(reverse("predict",kwargs={"username": username}))
    return render(request, 'predict/enreg_hpb.html', context={'user': user})

def visualise_view(request,username):
    user=get_object_or_404(Personne,username=username)
    nutritions=Nutritional_Diary.objects.filter(personne=user)
    return render(request, 'predict/visualise.html', context={'user': user, 'nutritions': nutritions})

def modif_conso_view(request, slog):
    foods=Food.objects.all()
    hpbs=Health_Problem.objects.all()
    conso=get_object_or_404(Nutritional_Diary, slog=slog)
    user=request.user
    if request.method=="POST":
        date=request.POST.get("date")
        day_of_week=request.POST.get("day_of_week")
        hpb_name=request.POST.get("hpb_name")
        food_name=request.POST.get("food_name")
        food =Food.objects.get(name=food_name)
        hpb =Health_Problem.objects.get(name=hpb_name)
        conso.date=date
        conso.day_of_week=day_of_week
        conso.food=food
        conso.health_pb=hpb
        conso.save()
        nutritions=Nutritional_Diary.objects.filter(personne=user)
        return redirect(reverse("visualise",kwargs={'username': user.username}))
    return render(request, "predict/modif_conso.html",context={"foods":foods, "hpbs":hpbs, "conso": conso})

def supp_conso_view(request, slog):
    conso=get_object_or_404(Nutritional_Diary, slog=slog)
    conso.delete()
    user=request.user
    return redirect(reverse("visualise",kwargs={'username': user.username}))

def agenda(nutritions,day):
        days={"Lundi":0,"Mardi":1,"Mercredi":2,"Jeudi":3,"Vendredi":4,"Samedi":5,"Dimanche":6}
        data_hpb=[]
        data_food=[]
        for i in range(7):
            data_hpb+=[{}]
            data_food+=[{}]
        for nutrition in nutritions:
            num_day=days[nutrition.day_of_week]
            if nutrition.food in data_food[num_day].keys():
                data_food[num_day][nutrition.food.name]+=1
            else:
                data_food[num_day][nutrition.food.name]=1
        num_day=days[day]
        total=0
        c=0
        while (data_food[num_day]=={})and(c<=6):
            if num_day>0:
                num_day-=1
            else:
                num_day=6
            c+=1
        if c<=6:
            for Key in data_food[num_day].keys():
                if data_food[num_day][Key]==max(data_food[num_day].values()):
                    maxKey=Key
                total+=data_food[num_day][Key]
            proba1=data_food[num_day][maxKey]*100/total
            return f"Vous avez {round(proba1,2)}% de chance de consommer le {maxKey} les {day}" 
        else :
            return "Votre agenda nutritionnel est vide nous ne pouvons pas faire de prédiction..."

def predict_view(request,username):
    user=get_object_or_404(Personne,username=username)
    prediction=""
    if request.method=="POST":
        day_of_week=request.POST.get("day_of_week")
        nutritions=Nutritional_Diary.objects.filter(personne=user)
        prediction=agenda(nutritions,day_of_week)
    return render(request, 'predict/predict.html', context={'user': user, 'prediction': prediction})

def modif_user_view(request):
    user=request.user
    if request.method=="POST":
        sex=request.POST.get("sex")
        date_of_birth=request.POST.get("date_of_birth")
        first_name=request.POST.get("first_name")
        image=request.POST.get("image")
        last_name=request.POST.get("last_name")
        user.sex=sex
        user.date_of_birth=date_of_birth
        user.first_name=first_name
        user.last_name=last_name
        user.image=image
        user.save()
        username=user.username
        return redirect(reverse("predict",kwargs={"username": username}))
    return render(request,'predict/modif_user.html', context={"user":user})
