# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
   
    required_css_class = "error-class"
    error_css_class = "error-class"

    username = forms.EmailField(
        label='E-mail',
        max_length=30,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )


    password = forms.CharField(
        label='Senha',
        max_length=30,
        widget=forms.PasswordInput(attrs={'class':"form-control"})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username):
            raise forms.ValidationError(u'E-mail não encontrado.')
        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            raise forms.ValidationError(u'Senha incorreta.')
        return password

    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        return authenticate(username=username, password=password)
