# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginForm(forms.Form):

    required_css_class = "error-class"
    error_css_class    = "error-class"

    username           = forms.EmailField(
        label          = 'E-mail',
        max_length     = 30,
        widget         = forms.TextInput(attrs =
            {
                'class' : 'form-control',
                'style' : 'width:300px'


            })
    )


    password           = forms.CharField(
        label          ='Senha',
        max_length     = 30,
        widget         = forms.PasswordInput(attrs =
            {
                'class' : "form-control",
                'style' : "width:300px"

            })
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username = username):
            raise forms.ValidationError(u'E-mail não encontrado.')
        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username = username, password = password):
            raise forms.ValidationError(u'Senha incorreta.')
        return password

    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        return authenticate(username = username, password = password)


# Formulário de Registro.
class RegisterForm(forms.Form):
    # TODO: Define form fields here
    required_css_class = "error-class"
    error_css_class    = "error-class"


    username           = forms.EmailField(
        label          = 'E-mail',
        max_length     = 30,
        widget         = forms.TextInput(attrs=
            {
                'class':'form-control',
                'style':'width:300px',
                'placeholder':'insira seu e-mail'

            })
    )


    password            = forms.CharField(
        label           = 'Senha',
        max_length      = 30,
        widget          = forms.PasswordInput(attrs=
            {
                'class'       : "form-control",
                'style'       : "width:300px",
                'placeholder' : 'crie uma senha'

            })
    )

    conf_password = forms.CharField(
        label='Confirmação de Senha',
        max_length=30,
        widget=forms.PasswordInput(attrs=
            {
                'class'       : "form-control",
                'style'       : "width:300px",
                'placeholder' : 'Confirme sua senha'

            })
    )

    plataforma  = forms.ChoiceField(
        label   = 'Plataforma',
        choices =[('opt', 'Selecione sua Plataforma'),('opt1', 'Loja Integrada')],
        widget = forms.Select(attrs={
            'onChange':'teste()',
            'id'      : 'combo',
            'class'   : "form-control",
            'style'   : "width:300px"
        })

    )






    conta_nome          = forms.CharField(
        label           = 'Loja',
        max_length      = 30,
        widget          = forms.TextInput(attrs=
            {
                'id'          : 'loja',
                'class'       : "form-control",
                'style'       : "width:300px; display:none",
                'placeholder' : 'Insira o nome da sua loja'

            })
    )

    chave_api           = forms.CharField(
        label           = 'Chave de API',
        max_length      = 130,
        widget          = forms.TextInput(attrs=
            {
                'id'         : 'chave_api',
                'class'      : "form-control",
                'style'      : "width:300px;display:none",
                'placeholder': 'Insira a chave de API'

            })
    )


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username = username):
            raise forms.ValidationError(u'E-mail já cadastrado.')
        return username


    def clean_conf_password(self):
        conf_password = self.cleaned_data.get('conf_password')
        if self.cleaned_data.get('password') != conf_password:
            raise forms.ValidationError(u'Senhas não conferem')
        return conf_password


    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        return authenticate(username = username, password = password)
