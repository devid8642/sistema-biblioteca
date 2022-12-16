from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Categorias(models.Model):
	nome = models.CharField(max_length = 250)
	descricao = models.TextField(blank = True, null = True)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'Categoria'

class Livros(models.Model):
	nome = models.CharField(max_length = 250)
	autor = models.CharField(max_length = 250)
	co_autor = models.CharField(max_length = 250, blank = True, null = True)
	data_cadastro = models.DateField(auto_now_add = True)
	emprestado = models.BooleanField(default = False)
	categoria = models.ForeignKey(Categorias, on_delete = models.SET_NULL, null = True)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'Livro'

class Emprestimos(models.Model):
	pessoa_emprestado = models.ForeignKey(User, on_delete = models.DO_NOTHING)
	livro_emprestado = models.ForeignKey(Livros, on_delete = models.DO_NOTHING)
	data_emprestimo = models.DateField(auto_now_add = True)
	data_devolucao = models.DateField(blank = True, null = True)

	def __str__(self):
		return self.nome_emprestado

	def duracao_emprestimo(self):
		return (date.today() - self.data_emprestimo).days

	class Meta:
		verbose_name = 'Emprestimo'