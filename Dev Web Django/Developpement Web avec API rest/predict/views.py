from rest_framework import viewsets
from predict.models import *
from predict.serializes import *
from rest_framework.permissions import IsAuthenticated

class PersonneViewset(viewsets.ModelViewSet ):
    queryset=Personne.objects.all()
    serializer_class=PersonneSerialiser
    permission_class=(IsAuthenticated, )
    search_fields=['first_name','last_name','date_of_birth','sex']
    filterset_fields=['first_name','last_name','date_of_birth','sex']

class FoodViewset(viewsets.ModelViewSet ):
    queryset=Food.objects.all()
    serializer_class=FoodSerialiser
    permission_class=(IsAuthenticated, )
    search_fields=['name']
    filterset_fields=['name']

class Health_ProblemViewset(viewsets.ModelViewSet ):
    queryset=Health_Problem.objects.all()
    serializer_class=Health_ProblemSerialiser
    permission_class=(IsAuthenticated, )
    filterset_fields=['name']
    search_fields=['name']


class Nutritional_DiaryViewset(viewsets.ModelViewSet ):
    queryset=Nutritional_Diary.objects.all()
    serializer_class=Nutritional_DiarySerialiser
    permission_class=(IsAuthenticated, )
    search_fields=['date','day_of_week','slog']
    filterset_fields=['date','day_of_week','personne','food','health_pb']
