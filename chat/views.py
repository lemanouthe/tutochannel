from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import models
from django.utils.safestring import mark_safe
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


# Create your views here.
@login_required(login_url='connexion')
def index(request):
    salon = models.salon.objects.filter(status=True)
    data = {
        'salon': salon
    }
    return render(request, 'index.html', data)

@login_required(login_url='connexion')
def chat(request, slug):
    layer = get_channel_layer()
    first = User.objects.get(username=request.user.username)
    if first:
        mess = models.Message.objects.filter(status=True, salon__slug=slug, author__username=first)
    else:
        mess = models.Message.objects.filter(status=True, salon__slug=slug).exclude(author__username=request.user.username)
    data = {
        'message': mess,
        'slug': slug
    }
    async_to_sync(layer.group_send)('chat_salut', {
        'type': 'chat_message',
        'message': data
    })
    return render(request, 'chat.html', data)

def connexion(request):
    try:
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'connexion.html')
    except:
        return redirect('index')

def connexionapi(request):
    statut = False
    message = ""
    if request.method == 'POST':
        postdata = json.loads(request.body.decode('utf-8'))
        
        username = postdata['username']
        password = postdata['password']

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