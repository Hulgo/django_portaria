from django.shortcuts import render, redirect
from django.contrib import auth, messages

def index(request):
    """ Verifica se  usuário está autenticado e o envia para o Home. """
    if request.user.is_authenticated:
        return render(request, 'home/index.html')
    else:
        return render(request, 'login/index.html')

def login(request):
    """ Encaminbha o usuário para a tela de login caso nào esteja logado. """
    if request.user.is_authenticated:
        return render(request, 'home/index.html')
    else:
        return render(request, 'login/index.html')

def logout(request):
    """ Realiza o Logout do usuário. """
    auth.logout(request)
    return redirect('index')