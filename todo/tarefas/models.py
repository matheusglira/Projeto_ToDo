from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
	nome = models.CharField(max_length=100, verbose_name='Nome')
	descricao = models.TextField(verbose_name='Descrição')

	def __str__(self):
		return self.nome

class Tarefa(models.Model):
	PRIORIDADE_CHOICES = (
		('B', 'Baixa'),
		('M', 'Média'),
		('A', 'Alta'),
	)
	nome = models.CharField(u'Nome', max_length=100)
	descricao = models.TextField(u'Descrição', blank=True)
	data_final = models.DateField(u'Data Final')
	prioridade = models.CharField(u'Prioridade', max_length=1, choices=PRIORIDADE_CHOICES)
	categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, verbose_name='Categoria')
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.nome