from django.shortcuts import render, redirect
from .models import Livros, Emprestimos, Categorias
from datetime import date

# Create your views here.

def home(request):
	usuario = request.user

	if usuario.is_authenticated:
		livros = Livros.objects.all()
		emprestimos = Emprestimos.objects.all()

		context = {
			'livros': livros,
			'emprestimos': emprestimos,
			'usuario': True
		}

		return render(request, 'home.html', context)
	else:
		return redirect('/usuario/login/?status=4')

def livro(request, id):
	usuario = request.user

	if usuario.is_authenticated:
		try:
			livro = Livros.objects.get(id = id)
		except:
			return redirect('/')
		if request.method == 'POST':
			nome_livro = request.POST.get('nome_livro')
			autor_livro = request.POST.get('autor_livro')
			co_autor = request.POST.get('co_autor')
			categoria = nome = request.POST.get('categoria')

			if len(nome_livro) > 250:
				return redirect(f'/livro/{livro.id}/?status=1')
			elif len(autor_livro) > 250 or len(co_autor) > 250:
				return redirect(f'/livro/{livro.id}/?status=2')
			elif len(nome_livro) == 0 or len(autor_livro) == 0:
				return redirect(f'/livro/{livro.id}/?status=3')

			try:
				categoria = Categorias.objects.get(nome = categoria)
			except:
				return redirect(f'/livro/{livro.id}')

			livro.nome = nome_livro
			livro.autor = autor_livro
			livro.co_autor = co_autor
			livro.categoria = categoria

			livro.save(update_fields = ['nome', 'autor', 'co_autor', 'categoria'])

			return redirect('/')
		status = request.GET.get('status')
		categorias = Categorias.objects.all()
		emprestimos = Emprestimos.objects.filter(livro_emprestado = livro)
		context = {
			'livro': livro,
			'categorias': categorias,
			'status': status,
			'emprestimos': emprestimos,
			'usuario': True
		}
		return render(request, 'livro.html', context)
	else:
		return redirect('/usuario/login/?status=4')

def cadastrar_livro(request):
	usuario = request.user

	if usuario.is_authenticated:
		if request.method == 'POST':
			nome = request.POST.get('nome')
			autor = request.POST.get('autor')
			co_autor = request.POST.get('co_autor')
			categoria = request.POST.get('categoria')

			if len(nome) > 250:
				return redirect('/cadastrar/livro/?status=1')
			elif len(autor) > 250 or len(co_autor) > 250:
				return redirect('/cadastrar/livro/?status=1')
			elif len(nome) == 0 or len(autor) == 0:
				return redirect('/cadastrar/livro/?status=2')

			try:
				categoria = Categorias.objects.get(id = categoria)
			except:
				return redirect('/cadastrar/livro/?status=3')

			novo_livro = Livros(nome = nome, autor = autor, co_autor = co_autor, categoria = categoria)
			novo_livro.save()
			return redirect('/?status=1')
		categorias = Categorias.objects.all()
		context = {
			'usuario': True,
			'categorias': categorias
		}
		return render(request, 'cadastrar_livro.html', context)

	return redirect('/usuario/login/?status=4')

def cadastrar_categoria(request):
	usuario = request.user

	if usuario.is_authenticated and request.method == 'POST':
		nome = request.POST.get('nome')
		descricao = request.POST.get('descricao')

		if len(nome) > 250:
			return redirect('/?status=2')
		elif len(nome) == 0:
			return redirect('/?status=3')

		cat = Categorias(nome = nome, descricao = descricao)
		cat.save()
		return redirect('/?status=4')

	return redirect('/usuario/login/?status=4')

def deletar_livro(request, id):
	usuario = request.user

	if usuario.is_authenticated:
		livro = Livros.objects.get(id = id)
		livro.delete()
		return redirect('/?status=5')

	return redirect('/usuario/login/?status=4')

def emprestimos(request):
	usuario = request.user

	if usuario.is_authenticated:
		emprestimos = Emprestimos.objects.filter(ativo = True)
		livros = Livros.objects.filter(emprestado = False)

		context = {
			'usuario': True,
			'emprestimos': emprestimos,
			'livros': livros
		}

		return render(request, 'emprestimos.html', context)

	return redirect('/usuario/login/?status=4')

def cadastrar_emprestimo(request):
	usuario = request.user

	if usuario.is_authenticated and request.method == 'POST':
		nome = request.POST.get('nome')
		livro_id = request.POST.get('livro')

		if len(nome) > 255:
			return redirect('/emprestimos/?status=1')
		elif len(nome) == 0:
			return redirect('/emprestimos/?status=2')

		try:
			livro = Livros.objects.get(id = livro_id)
		except:
			return redirect('/emprestimos/?status=3')

		empr = Emprestimos(nome_emprestado = nome, livro_emprestado = livro)
		empr.save()
		livro.emprestado = True
		livro.save(update_fields = ['emprestado'])
		return redirect('/emprestimos/')

	return redirect('/usuario/login/?status=4')

def finalizar_emprestimo(request, id):
	usuario = request.user

	if usuario.is_authenticated:
		try:
			empr = Emprestimos.objects.get(id = id, ativo = True)
			livro = Livros.objects.get(id = empr.livro_emprestado.id, emprestado = True)
		except:
			return redirect('/emprestimos/?status=4')
		else:
			empr.ativo = False
			empr.data_devolucao = date.today()
			empr.save(update_fields = ['ativo', 'data_devolucao'])
			livro.emprestado = False
			livro.save(update_fields = ['emprestado'])
			return redirect('/emprestimos/?status=5')


	return redirect('/usuario/login/?status=4')