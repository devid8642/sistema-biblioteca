from django import template
from datetime import date

register = template.Library()

@register.filter
def duracao_emprestimo(data_devolucao, data_emprestimo):
	return (data_devolucao - data_emprestimo).days

@register.filter
def duracao_emprestimo_hoje(data_emprestimo):
	return (date.today() - data_emprestimo).days