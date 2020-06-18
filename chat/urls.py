from django.urls import path
from . import views

urlpatterns = [
    path('', views.connexion, name="connexion"),
    path('connexionapi', views.connexionapi, name="connexionapi"),
    path('index', views.index, name="index"),
    path('chat/<slug:slug>', views.chat, name="chat"),
    
]