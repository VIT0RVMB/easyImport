# -*- coding:utf-8 -*-
# Create your views here.
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from appPainel.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from appPainel.sincronizador import Sincronizador
from appPainel.models import Conta, Categoria, Plataforma


def index(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user_db = User()

            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/home/')

    form = RegisterForm()
    return render(request, 'appPainel/register.html', {'form': form})






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
    return render(request, 'appPainel/home.html',
                  {
                      'chave_api': '7c5a8002-2b27-49c4-9ccb-b4e317a8b00d '  # str(conta[1].chave_api),
                      # 'plataforma':plataforma.plataforma_nome,

                  }
                  )


def sair(request):
    logout(request)
    return HttpResponseRedirect(reverse('appPainel_logar'))


def sincronizar(request):
    conta = Conta.objects.get(id=1)
    sync = Sincronizador()
    sincronizar_categorias(conta.id, 0)
    return HttpResponseRedirect(reverse('appPainel_home'))
