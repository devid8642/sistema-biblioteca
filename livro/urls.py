from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('livro/<int:id>/', views.livro, name = 'livro'),
	path('cadastrar/livro/', views.cadastrar_livro, name = 'cadastrar_livro'),
	path('cadastrar/categoria/', views.cadastrar_categoria, name = 'cadastrar_categoria')
]