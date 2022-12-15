from django.urls import path
from . import views

urlpatterns = [
	path('login/', views.entrar, name = 'login'),
	path('cadastro/', views.cadastro, name = 'cadastro'),
	path('sair/', views.sair, name = 'sair')
]