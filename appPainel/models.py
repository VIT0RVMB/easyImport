# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Plataforma(models.Model):
    plataforma_nome            = models.CharField(max_length=140)
    plataforma_url_api         = models.CharField(max_length=240)
    plataforma_chave_aplicacao = models.CharField(max_length=140)

    def __unicode__(self):
        return self.plataforma_nome




class Conta(models.Model):
    conta_nome = models.CharField(max_length=130)
    plataforma = models.ForeignKey(Plataforma)
    user       = models.ManyToManyField(User)
    chave_api  = models.CharField(max_length=140)

    def __unicode__(self):
        return self.conta_nome




class Categoria(models.Model):
    plataforma_id               = models.IntegerField(null = True, unique = True)
    pai_id                      = models.IntegerField(null = True)
    conta_id                    = models.ForeignKey(Conta)
    categoria_nome                        = models.CharField(max_length = 50)
    descricao                   = models.TextField()
    categoria_pai_resource_uri  = models.CharField(max_length = 100, null = True)
    resource_uri                = models.CharField(max_length = 100)
    seo                         = models.CharField(max_length = 100)
    url                         = models.URLField(verify_exists = 'false')



    def __unicode__(self):
        return self.categoria_nome




