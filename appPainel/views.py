# -*- coding:utf-8 -*-
# Create your views here.
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from appPainel.forms import LoginForm
from django.contrib.auth.models import User
from appPainel.sincronizador import Sincronizador
from appPainel.models import Conta, Categoria, Plataforma
def index(request):
    
    return render(request, 'landingPage.html')





def logar(request):


        next = request.REQUEST.get('next', '/home/')
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return HttpResponseRedirect(next)
        else:
            form = LoginForm()
        return render(request, 'appPainel/index.html', 
            {
                'form': form,
                'next': next,
            }
        )

@login_required
def home(request):
    user=User.objects.get(id=request.user.id)

    conta=Conta.objects.get(user=user.id)#Por algum motivo o user.id tá retornando long
                                              #Por isso converti pra INT
    
    return render(request,'appPainel/home.html',
            {
                'chave_api':conta.chave_api,
                #'plataforma':plataforma.plataforma_nome,



            }
        )



def sair(request):
    logout(request)
    return HttpResponseRedirect(reverse('appPainel_logar'))




def sincronizar(request):
    conta=Conta.objects.get(id=1)
    sync=Sincronizador()
    sync.sincronizar_categorias(conta.id, 0)
    return HttpResponseRedirect(reverse('appPainel_home'))