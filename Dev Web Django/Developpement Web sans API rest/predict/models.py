from django.db import models
#from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Personne(AbstractUser):
    username = models.CharField(max_length=80, primary_key=True, blank=False, null=False)
    password = models.CharField(max_length=12000, blank=False, null=False)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=120)
    sex = models.CharField(max_length=10)
    date_of_birth = models.DateTimeField(null=False,default=now())
    image=models.ImageField(upload_to="user_img", blank=False, null=False)

    def __str__(self):
        age = now().year - self.date_of_birth.year
        return f"{self.first_name} {self.last_name} ({age} ans)"


class Health_Problem(models.Model):
    name = models.CharField(max_length=100, blank=False, primary_key=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100, blank=False, primary_key=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="food_img", blank=True, null=True)

    def __str__(self):
        return self.name


class Nutritional_Diary(models.Model):
    slog=models.CharField(null=False, default="")
    date = models.DateField(null=False, default=now)
    day_of_week = models.CharField(max_length=10)
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)
    health_pb = models.ForeignKey(Health_Problem, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.pk}, {self.day_of_week}, {self.personne.first_name}, {self.food.name}, {self.health_pb.name}"
    