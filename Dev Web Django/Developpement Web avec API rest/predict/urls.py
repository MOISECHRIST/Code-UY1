from rest_framework import routers
from predict.views import *

router = routers.DefaultRouter()
router.register('Personne', PersonneViewset)
router.register('Food', FoodViewset)
router.register('Health_Problem', Health_ProblemViewset)
router.register('Nutritional_Diary', Nutritional_DiaryViewset)