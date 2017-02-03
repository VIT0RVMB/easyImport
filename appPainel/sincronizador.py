# -*- coding:utf-8 -*-
from django.db import models
from appPainel.models import Plataforma, Conta, Categoria
import requests
import json


class Sincronizador(models.Model):
	
	data_sincronizacao       = models.DateField()
	produtos_sincronizados   = models.IntegerField(null = True)
	grades_sincronizadas     = models.IntegerField(null = True)
	categorias_sincronizadas = models.IntegerField(null = True)


	def sincronizar_categorias(request,id, offset = 0):
		conta         = Conta.objects.get(id = id)
		
		plataforma    = Plataforma.objects.get(id = conta.plataforma_id)
		
		request       = requests.get(plataforma.plataforma_url_api + 'categoria'
			+ '?chave_api=' + conta.chave_api
			+ '&chave_aplicacao=' + plataforma.plataforma_chave_aplicacao
			+ '&offset='+str(offset))
		conteudo_json = str(request.content)
		conteudo_json = json.loads(conteudo_json)

		for i in conteudo_json['objects']:
			if Categoria.objects.filter(plataforma_id = i['id']):
				categoria = Categoria.objects.get(plataforma_id = i['id'])
			else:
				categoria                        = Categoria()
			categoria.categoria_descricao        = i['descricao']
			categoria.nome                       = i['nome']
			categoria.plataforma_id              = i['id']
			categoria.categoria_pai_resource_uri = i['categoria_pai']
			if not categoria.categoria_pai_resource_uri == None:
				categoria.pai_id = categoria.categoria_pai_resource_uri[18:]
			else:
				pass
			categoria.resource_uri = i['resource_uri']
			categoria.seo          = i['seo']
			categoria.url          = i['url']
			categoria.conta_id     = conta
			categoria.save()

			#Recursividade para Paginação 
			if conteudo_json['meta']['next'] != None:
				new_offset += conteudo_json['meta']['limit']
				sincronizar_categorias(plataforma_id, conta_id, int(new_offset))








