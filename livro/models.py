from django.db import models
from datetime import date


class Livros(models.Model):
	nome = models.CharField(max_length = 100)
	autor = models.CharField(max_length = 30)
	co_autor = models.CharField(max_length = 30, blank = True, null = True)
	data_cadastro = models.DateField(default = date.today())
	emprestado = models.BooleanField(default = False)


	def __str__(self):
		return self.nome


class Emprestimos(models.Model):
	nome_emprestado = models.CharField(max_length = 30)
	livro_emprestado = models.ForeignKey(Livros, on_delete = models.CASCADE)
	data_emprestimo = models.DateField()
	data_devolucao = models.DateField(null = True)

	def __str__(self):
		return self.nome_emprestado