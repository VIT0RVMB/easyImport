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

    return render(request,'appPainel/home.html')


def sair(request):
    logout(request)
    return HttpResponseRedirect(reverse('appPainel_logar'))