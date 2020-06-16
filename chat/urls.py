from django.urls import path
from . import views

urlpatterns = [
    path('', views.connexion, name="connexion"),
    path('connexionapi', views.connexionapi, name="connexionapi"),
    path('chat', views.index, name="index"),
]