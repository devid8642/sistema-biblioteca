from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password

def entrar(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		senha = request.POST.get('senha')
		usuario = authenticate(request, username = email, password = senha)
		if usuario is not None:
			login(request, usuario)
			return redirect('/livro/')
		else:
			return redirect('/usuario/login/?status=3')
	status = request.GET.get('status')
	return render(request, 'login.html', {'status': status})

def cadastro(request):
	status = request.GET.get('status')
	if request.method == 'POST':
		nome = request.POST.get('nome')
		email = request.POST.get('email')
		senha = request.POST.get('senha')

		try:
			validate_email(email)
		except:
			return redirect('/usuario/cadastro/?status=2')
		else:
			if len(nome.replace(' ', '')) == 0:
				return redirect('/usuario/cadastro/?status=1')
			u = User(username = nome, password = senha)
			try:
				validate_password(senha, user = u)
			except:
				return redirect('/usuario/cadastro/?status=3')

		usuario = User.objects.filter(username = email)

		if not usuario:
			usuario = User.objects.create_user(username = email, first_name = nome, password = senha)
			return redirect('/usuario/login/?status=1')
		return redirect('/usuario/login/?status=2')

	return render(request, 'cadastro.html', {'status': status})

def sair(request):
	logout(request)
	return redirect('/usuario/login/')