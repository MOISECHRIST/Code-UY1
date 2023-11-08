from predict.models import *
from rest_framework import serializers

class PersonneSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Personne
        fields = '__all__'


class FoodSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'


class Health_ProblemSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Health_Problem
        fields = '__all__'


class Nutritional_DiarySerialiser(serializers.ModelSerializer):
    
    class Meta:
        model = Nutritional_Diary
        fields = '__all__'