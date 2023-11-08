"""
URL configuration for food project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from predict import views
from django.conf.urls.static import static
from food import settings
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_view, name="accueil"),
    path("predict/<str:username>/", views.index_view, name="predict"),
    path("login/", views.login_view,name='login'),
    path("createuser/", views.newuser_view,name='creer_user'),
    path("logout/", views.logout_user,name='logout'),
    path("enreg_consol/<str:username>/", views.enreg_conso_view,name='enreg_consol'),
    path("enreg_food/<str:username>/", views.enreg_food_view,name='enreg_food'),
    path("enreg_hpb/<str:username>/", views.enreg_hpb_view,name='enreg_hpb'),
    path("visualise/<str:username>/", views.visualise_view,name='visualise'),
    path("prediction/<str:username>/", views.predict_view,name='prediction'),
    path("modif_conso/<str:slog>/", views.modif_conso_view,name='modif_conso'),
    path("supp_conso/<str:slog>/", views.supp_conso_view,name='supp_conso'),
    path("modif_user/", views.modif_user_view, name="modif_user"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

