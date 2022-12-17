from django.shortcuts import render, redirect
from .models import Livros, Emprestimos, Categorias
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
			'emprestimos': emprestimos
		}
		return render(request, 'livro.html', context)
	else:
		return redirect('/usuario/login/?status=4')