from django.db import models
from appPainel import Plataforma, Conta, Categoria
import requests
import json


class Sincronizador(models.Model):
	data_sincronizacao=models.DateField()
	produtos_sincronizados=models.IntegerField(null=True)
	grades_sincronizadas=models.IntegerField(null=True)
	categorias_sincronizadas=models.IntegerField(null=True)


	def sincronizar_categorias(plataforma_id, conta_id, offset=0):
		plataforma=Plataforma.objects.get(plataforma_id=id)
		conta=Conta.objects.get(conta_id=id)
		
		request=requests.get(plataforma.endpoint
			+'?chave_api='+plataforma.chave_api
			+'&chave_aplicacao='+plataforma.chave_aplicacao
			+'&offset='+str(offset))
		conteudo_json=str(request.content)
		conteudo_json=json.loads(conteudo_json)
		for i in conteudo_json['object']:
			if Categoria.objects.filter(plataforma_id=i['id']):
				categoria=Categoria.objects.get(plataforma_id=i['id'])
			else:
				categoria=Categoria()
			categoria.categoria_descricao=i['descricao']
			categoria.nome=i['nome']
			categoria.plataforma_id=i['id']
			categoria.categoria_pai_resource_uri=i['categoria_pai']
			if not categoria.categoria_pai_resource_uri==null:
				categoria.pai_id=categoria.categoria_pai_resource_uri[18:]

			categoria.resource_uri=i['resource_uri']
			categoria.seo=i['seo']
			categoria.url=i['url']
			categoria.conta_id=conta.id

			#Recursividade para Paginação 
			if conteudo_json['meta']['next']!=None:
				new_offset+=conteudo_json['meta']['limit']
				sincronizar_categorias(plataforma_id, conta_id, new_offset)








