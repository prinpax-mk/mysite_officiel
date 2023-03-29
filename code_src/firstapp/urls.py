from django.urls import path
from . import views

app_name = "firstapp"
urlpatterns = [
    
    path("index", views.index, name="index"),
    path("connexion", views.connexion, name="connexion"),
    path("inscription", views.inscription, name="inscription"),
]