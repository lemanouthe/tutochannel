from django.shortcuts import render
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'chat.html')

def connexion(request):
    return render(request, 'connexion.html')

def connexionapi(request):
    statut = False
    message = ""
    if request.method == 'POST':
        postdata = json.loads(request.body.decode('utf-8'))
        
        username = postdata['username']
        password = postdata['password']
        print(username)
        print(password)

        try:
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)

            statut = True,
            message = "Connexion réussite"
        except Exception as e:
            statut = False
            print(e)
            message = "Connexion echouée"
    data = {
        'success': statut,
        'message': message
    }

    return JsonResponse(data=data, safe=False)