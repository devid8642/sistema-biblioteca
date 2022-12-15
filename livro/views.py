from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Livros, Emprestimos
from datetime import date

# Create your views here.

def home(request):
	usuario = request.user

	if usuario.is_authenticated:
		livros = Livros.objects.all()

		context = {
			'livros': livros,
		}

		return render(request, 'home.html', context)
	else:
		return redirect('/usuario/login/?status=4')