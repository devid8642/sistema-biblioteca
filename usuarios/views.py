from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password

def login(request):
	return HttpResponse('login')

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
		
		return redirect('/usuario/login/')

	return render(request, 'cadastro.html', {'status': status})