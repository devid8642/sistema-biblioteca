from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('livro/<int:id>/', views.livro, name = 'livro'),
	path('cadastrar/livro/', views.cadastrar_livro, name = 'cadastrar_livro'),
	path('cadastrar/categoria/', views.cadastrar_categoria, name = 'cadastrar_categoria'),
	path('deletar/livro/<int:id>', views.deletar_livro, name = 'deletar_livro'),
	path('emprestimos/', views.emprestimos, name = 'emprestimos'),
	path('cadastrar/emprestimo/', views.cadastrar_emprestimo, name = 'cadastrar_emprestimo'),
	path('finalizar/emprestimo/<int:id>', views.finalizar_emprestimo, name = 'finalizar_emprestimo')
]